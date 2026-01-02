# Compilers in the Age of LLMs — Yusuf Olokoba, Muna

**Video URL:** https://www.youtube.com/watch?v=q2nHsJVy4FE

---

## Executive Summary

Yusuf Olokoba from Muna presents an innovative approach to AI deployment: building a Python compiler that enables developers to write simple Python inference code and convert it into self-contained binaries that run anywhere. The talk covers the motivation for building a compiler (simplicity and hybrid inference), the technical implementation (tracing, type propagation, LLM-assisted code generation), and demonstrates how to compile a Google Gemma embedding model into C++/Rust code that can be consumed via an OpenAI-style client interface. This infrastructure enables running any AI model in more places beyond just server-side, particularly on edge devices and consumer hardware.

---

## Topics

### [Introduction: The AI Engineer's Daily Struggle](https://www.youtube.com/watch?v=q2nHsJVy4FE&t=0s)
**[00:00 - 01:40]**

- **Current AI development pain points**: Multiple browser tabs, playground repos, agentic workflows built with HTTP calls
- **The fundamental problem**: How to use more models in more places without constantly rebuilding infrastructure
- **Example complexity**: Trying a new open-source model requires writing Dockerfiles, spinning up containers, managing infrastructure, and exposing tools to agents via MCP
- **What developers actually want**: A simple OpenAI-style client that works with any model (local, remote, different runtimes) with minimal code changes
- **The compiler solution**: Convert plain Python code into tiny self-contained binaries that run anywhere (cloud, Apple Silicon, edge devices)

### [Motivation for Building a Python Compiler](https://www.youtube.com/watch?v=q2nHsJVy4FE&t=134s)
**[02:14 - 04:05]**

- **First reason - Simplicity**: Need an extremely simple, standardized way for developers to bring AI models (internal or open-source) into their codebase
  - When a new OpenAI model drops, you just change the model argument
  - Goal: Recreate this experience for all models
  - Requires ingesting Python inference code and outputting something executable in user environments

- **Second reason - Hybrid inference future**: Preparing for smaller models running locally/at edge + larger cloud models with better reasoning
  - Developers need to move beyond "cages of Python code and Docker containers"
  - Need something lower-level, closer to hardware, more responsive

### [Example: Compiling Google's Gemma Embedding Model](https://www.youtube.com/watch?v=q2nHsJVy4FE&t=245s)
**[04:05 - 05:20]**

- **Model selection**: Google's Gemma 270M parameter text embedding model
  - Used for text search, RAG, document retrieval
  - Small enough to run on cloud GPUs AND consumer hardware

- **Compilation goal**:
  1. Take Python function running the embedding model
  2. Generate equivalent C++ and Rust code (lower-level, portable)
  3. Compile binary containing model + dependencies
  4. Consume via familiar `client.embeddings.create` experience

### [Step 1: Tracing - Generating Graph Representation](https://www.youtube.com/watch?v=q2nHsJVy4FE&t=320s)
**[05:20 - 07:00]**

- **What is tracing?**: Converting Python function into graph representation describing everything that happens

- **Initial approach - PyTorch 2**:
  - Tried using Torch FX (runs code with fake inputs, produces graph)
  - **Problem 1**: PyTorch tracer only focused on PyTorch code, doesn't handle NumPy, OpenCV, etc.
  - **Problem 2**: Fake inputs work for tensors but hard for images, dictionaries, arbitrary types

- **Why they abandoned PyTorch**: Too limited for arbitrary Python code with diverse data types

### [LLM-Based Tracing Attempt](https://www.youtube.com/watch?v=q2nHsJVy4FE&t=420s)
**[07:00 - 07:36]**

- **First custom attempt**: Using LLMs with structured outputs to generate traces
  - Give LLM code and schema, ask it to produce trace
  - **Result**: ~100% accuracy in testing
  - **Fatal flaw**: Took way too much time

- **Final solution - Traditional AST approach**:
  - Analyze Abstract Syntax Tree (AST) of Python code
  - Use internal heuristics to build Internal Representation (IR)
  - Result: Simple IR with input nodes, tokenizer calls, model calls, output returns

### [Step 2: Type Propagation](https://www.youtube.com/watch?v=q2nHsJVy4FE&t=456s)
**[07:36 - 11:36]**

- **The challenge**: Python is dynamically typed, C++/Rust require static types
  - Python: `x = 5`, then `x = "hello"` is valid
  - C++/Rust: Variable type must be declared and never changes

- **Type propagation technique**:
  - Start with input types from function signature
  - Example: String concatenation `prefix + text`
    - Input: Two strings
    - Generate C++ function for `operator.add` on strings
    - Output: Also a string
  - Propagate type information through every operation in the IR graph

- **Example walkthrough**: List comprehension adding prefixes
  - Input `text` is `list[string]` from annotation
  - `task_prefix_map` contains strings
  - Addition of two strings → output is string
  - Type flows through entire function

### [Handling the Variety Problem with LLMs](https://www.youtube.com/watch?v=q2nHsJVy4FE&t=696s)
**[11:36 - 13:48]**

- **Challenge**: Don't we need to manually implement every Python operation in C++?
  - **Answer**: Yes, but it's now tractable for two reasons:

- **Reason 1 - Composability**:
  - Variety in code comes from combining operations in different ways
  - Only need to cover base set of elementary functions
  - Can stack/combine them in C++ same way as Python

- **Reason 2 - LLM Code Generation**:
  - Don't have to manually write equivalent native code anymore
  - LLMs can generate code translating Python → C++/Rust
  - Enables "mass production" of operation translations
  - Covers everything: addition, subtraction, exponentiation, NumPy ops, PyTorch ops

### [Step 3: C++ Code Generation](https://www.youtube.com/watch?v=q2nHsJVy4FE&t=828s)
**[13:48 - 14:54]**

- **Final code generation**: With typed IR graph, can generate correct, compilable C++ code
- **Side-by-side comparison**:
  - List comprehension for prefixes → C++ equivalent
  - Tokenizer call → C++ tokenization
  - Model inference → C++ model execution
  - Return embeddings → C++ return

- **Universal compilation**:
  - C++ code compiles to run natively on any device/platform
  - Every technology has a C/C++ compiler
  - Enables conversion of high-level Python to self-contained, portable binaries

- **Output**: Dynamic library (shared object) that can be loaded and executed

### [Step 4: Cross-Language Integration (JavaScript Example)](https://www.youtube.com/watch?v=q2nHsJVy4FE&t=894s)
**[14:54 - 16:06]**

- **Goal**: Invoke compiled model from any language on any device
- **Example**: JavaScript on Node.js

- **Using FFI (Foreign Function Interface)**:
  - Design bindings declaring native library location
  - Specify function name and signature
  - Load compiled library into process
  - Invoke like any other function
  - **Result**: Get embedding matrix directly in JavaScript

### [Step 5: OpenAI-Style Client Interface](https://www.youtube.com/watch?v=q2nHsJVy4FE&t=966s)
**[16:06 - 17:18]**

- **Final piece**: Expose compiled model through familiar OpenAI API

- **Implementation**:
  1. Create `Client` class with nested `Embeddings` class
  2. Implement `create()` function mirroring OpenAI API
  3. Map model name → path to compiled binary
  4. Load library using FFI infrastructure
  5. Execute to get embedding matrix
  6. Massage outputs to match OpenAI client format

- **Achievement**: Recreated OpenAI client with access to any open-source model that can be expressed as a Python function

---

## Key Takeaways

1. **Compiler approach solves AI deployment complexity**: Converting Python to self-contained binaries eliminates Docker containers, infrastructure management, and deployment overhead

2. **Hybrid inference is the future**: Small models at the edge + large models in the cloud working together

3. **LLMs enable compiler development**: While too slow for tracing, LLMs excel at mass-producing operation translations from Python to C++/Rust

4. **Type propagation bridges dynamic/static gap**: Technique enables converting dynamically-typed Python to statically-typed compiled languages

5. **Universal API abstraction**: OpenAI-style client interface works for any model (cloud or local) with minimal code changes

6. **Portability through C++**: Every platform has C/C++ compilers, making compiled AI models truly portable

---

## Technical Architecture Summary

```
Python Function
    ↓
[Tracing via AST Analysis]
    ↓
Internal Representation (IR Graph)
    ↓
[Type Propagation]
    ↓
Typed IR Graph
    ↓
[LLM-Assisted Code Generation]
    ↓
C++ / Rust Source Code
    ↓
[Native Compilation]
    ↓
Self-Contained Binary (.so / .dll)
    ↓
[FFI Integration]
    ↓
OpenAI-Style Client Interface
    ↓
Run Anywhere (Cloud, Edge, Mobile, etc.)
```
