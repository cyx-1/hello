# Vision: Zero Bugs — Johann Schleier-Smith, Temporal

**Video URL:** https://www.youtube.com/watch?v=qLqttdO33UM

---

## Executive Summary

Johann Schleier-Smith from Temporal presents a compelling vision for achieving zero-bug software through proven aerospace engineering techniques, formal methods, and AI-powered development. Drawing on case studies from the Airbus A320, Space Shuttle, and Curiosity Rover, he demonstrates that bug-free software is achievable through rigorous processes and verification techniques. He argues that agentic coding, combined with formal methods like the Daphne language, can produce high-assurance software 100 times more cheaply than traditional methods, making zero-bug software economically viable for mainstream applications.

---

## Main Topics

### [Introduction and Vision of Zero Bugs](https://www.youtube.com/watch?v=qLqttdO33UM&t=2s)
- Software bugs create constant stress for developers through on-call responses, cloud outages, and critical application errors
- Most users rarely notice bugs in popular apps (social media, banking, cameras), but they have real impact when they occur
- Personal anecdote: mini-golf reservation system bug created emotional roller coaster but ultimately worked
- The vision: achieving literally zero bugs in software, not just "a few bugs"
- This talk focuses on proven techniques from aerospace and formal methods, not on Temporal's products

### [Objections to Zero-Bug Software](https://www.youtube.com/watch?v=qLqttdO33UM&t=229s)
- **Incidents happen**: Cloud outages and bugs occur regularly, and we generally recover from them
- **Good enough software**: Maybe software is already reliable enough in situations where it matters
- **Theoretical impossibility**: Millions of lines of code are too complex; specifications have inherent ambiguity
- **Real-world unpredictability**: Unexpected events happen (e.g., self-driving vehicle concerns)
- **Computational limits**: Some problems are computationally intractable for verification
- **Economic barriers**: Competitors who don't prioritize quality may win in the marketplace
- **ROI concerns**: Fixing every bug may not provide sufficient return on investment
- **Cynical view**: Some companies may benefit from selling support for buggy software

### [Case Study: Airbus A320](https://www.youtube.com/watch?v=qLqttdO33UM&t=426s)
- Control software developed in the 1980s with zero serious incidents attributed to software failures
- **N-version programming**: Critical systems built with different processors (x86, Motorola), different operating systems, and separate development teams
- **Specification-based design**: Extensive documentation that could be analyzed for provable guarantees
- **Independent verification teams**: Complete separation between code writers and code verifiers
- **Defensive programming**: No runtime memory allocation, simple explicit error handling, static analysis
- **Zero-defect tolerance**: Software treated as a certified component like a turbine fan blade
- **System-level approach**: Decades of mechanical engineering experience applied to software development

### [Quality Through Process](https://www.youtube.com/watch?v=qLqttdO33UM&t=606s)
- Process is critical for keeping agents "on the rails" and doing what we want
- Key steps: planning, requirements, design, implementation, integration testing, certification by external agencies
- Integration testing particularly important for software interfacing with physical systems
- Feedback loops refine each process step and ensure proper interfaces between steps
- Aerospace industry rich in examples of super-reliable software built through rigorous process

### [Case Study: Space Shuttle](https://www.youtube.com/watch?v=qLqttdO33UM&t=689s)
- Last three versions had 420,000 lines of code each with only one error per version
- 11 versions total had only 17 errors combined
- Approximately 1,000 times fewer bugs per line of code than typical commercial software
- No space shuttles lost to software problems (some lost to other causes)
- Demonstrates that extremely high reliability is achievable even with large codebases

### [Case Study: Curiosity Rover](https://www.youtube.com/watch?v=qLqttdO33UM&t=731s)
- Developed in the 2000s for Mars mission with millions at stake and limited intervention ability
- Shows evolution from A320 approach: used identical redundant systems instead of N-version programming
- Used commercial off-the-shelf real-time operating system rather than custom OS
- Demonstrates adaptation of high-assurance techniques to newer technologies and constraints

### [Other High-Assurance Industries](https://www.youtube.com/watch?v=qLqttdO33UM&t=764s)
- Chemical industry, automotive industry, medical software, nuclear power, security systems
- Each provides lessons for building effectively zero-bug software
- High-assurance software is critical across many domains beyond aerospace

### [Advances in Computer Science: High-Level Languages](https://www.youtube.com/watch?v=qLqttdO33UM&t=791s)
- 1950s-1980s transition from assembly language to high-level languages
- 5-10x productivity gain from abstraction
- **Data abstraction**: Working with problem-domain data structures instead of memory locations
- **Preserving essential complexity**: Focusing on problem-relevant aspects while removing machine-specific implementation details
- Assembly language replaced by machine code generated by machines for machines

### [Structured Programming](https://www.youtube.com/watch?v=qLqttdO33UM&t=912s)
- Advocated by Edsger Dijkstra in the 1960s, broadly accepted in 1970s
- Basic control structures: sequences, selection (if-then-else), iteration
- Eliminated goto statements and flowchart-based programming
- **Compositional reasoning**: Hierarchical decomposition mitigates complexity
- Allows programmers to focus on one piece of code at a time
- Eliminates spaghetti code through structured control flow
- Just as valuable for LLM-generated code as for human-written code

### [Modularity](https://www.youtube.com/watch?v=qLqttdO33UM&t=1019s)
- David Parnas's concept from the 1970s
- Best known through object-oriented programming but applies more broadly (libraries, etc.)
- Enables sub-exponential or linear scaling rather than exponential complexity growth
- Local reasoning at every level makes complexity manageable regardless of system size
- Critical for verification whether done by humans, LLMs, or formal methods

### [Why LLMs Should Generate High-Level Code](https://www.youtube.com/watch?v=qLqttdO33UM&t=1090s)
- **Context limitations**: LLM context is scarce resource, just like human working memory
- **Library value**: Getting AI-generated library code properly tested and verified is challenging
- Better to use reliable, trusted components and modules to build systems
- Same reasons that applied to human programmers decades ago apply to LLMs today
- Temporal pitch: Abstracts away cloud reliability concerns through durable execution

### [Formal Methods and Daphne Language Demonstrations](https://www.youtube.com/watch?v=qLqttdO33UM&t=1200s)
- **Daphne language**: Custom programming language that generates output to JavaScript, Python, C, etc.
- Allows proofs inline with code, enabling theorem-proving software to verify correctness
- **Demo 1**: IndexOf method to search array with assertions about array length and return values
- Running Daphne verifier confirms "no bugs" before generating Python code
- **Demo 2**: Introducing a bug causes verifier to throw error, preventing buggy code from running
- Verification only as good as the specification - incomplete specs create bug opportunities

### [Commercial Formal Methods Success Stories](https://www.youtube.com/watch?v=qLqttdO33UM&t=1334s)
- **seL4 microkernel**: Fully verified operating system for embedded and security-critical applications
- **CompCert C compiler**: Fully verified compiler ensuring generated code matches C program specifications
- **Project Everest**: Verified cryptography libraries widely deployed protecting internet traffic
- **Microprocessor verification**: Formal methods used for decades to ensure correctness of processor designs
- Tremendous progress in size and speed of verification over last 20+ years

### [Verification Benchmarks Progress](https://www.youtube.com/watch?v=qLqttdO33UM&t=1440s)
- Success rates increased from ~30% to nearly 100%
- Runtime decreased by factor of 50 or more
- Benchmarks shape industry by giving focus for improvement
- Demonstrates rapid advancement in formal verification capabilities

### [Types of Verification Tools](https://www.youtube.com/watch?v=qLqttdO33UM&t=1477s)
- **Static verification**: Type systems as simple form; can attach more checks to type systems
- **Tight coupling**: Daphne, Spark Ada couple theorems directly with code
- **Separate theorem proving**: Lean and similar tools provide powerful proving but require ensuring code matches proofs
- **Model checking**: Proves properties about finite state machines
- **Theorem proving**: More powerful than model checking, handles non-finite cases through automated reasoning

### [Practical Techniques for Agentic Coding](https://www.youtube.com/watch?v=qLqttdO33UM&t=1559s)
- **Standard practices**: Detailed specifications, type languages, modular code
- **Risk analysis**: Ask LLM to perform explicit risk analysis on code
- **Safety cases**: Document what could go wrong and how it's mitigated (qualitative reasoning)
- **Separate verification**: Different prompts for testing vs. coding (inspired by high-assurance teams)
- **Multiple model providers**: One foundation model for tests, another for code (N-version approach)
- **Formal methods for critical sections**: Apply proofs around most important code
- **Keep code small**: Outsource to well-tested libraries whenever possible

### [Software 3.0 and Future Implications](https://www.youtube.com/watch?v=qLqttdO33UM&t=1690s)
- Andrej Karpathy's concept: prompts as programs
- Programming through AI/LLMs creates new world of coding
- LLMs are fundamentally non-deterministic with huge state spaces
- Traditional verification techniques don't apply to Software 3.0
- **New resilience opportunities**: LLMs can respond to unanticipated inputs and handle ambiguity
- **Architectural possibilities**: Pure agentic systems or LLMs invoked for specific error conditions
- Could protect against software faults in simple, interesting ways

### [Cost Analysis of Agentic Coding](https://www.youtube.com/watch?v=qLqttdO33UM&t=1803s)
- **Personal example**: Simple game generated for ~$2 using GPT-4 with Code Execution
- 600K input tokens, 3.5M cached tokens, 48K reasoning tokens, 28K output tokens
- Only 15% of cost in output generation; 85% in input/reasoning (like human development time)
- **High-assurance code costs** (traditional):
  - Space Shuttle: $1,000/line in 1990 dollars = $2,500/line in 2025 dollars
  - Security high-assurance: up to $3,000/line
- **Typical software**: $10-100/line for production code
- **Low-cost contractors**: $1-10/line
- **Agentic coding**: $0.001-1/line (varies by model and iteration)
- **Gap analysis**: 1,000-10,000x cheaper than traditional development

### [Vision of Zero Bugs](https://www.youtube.com/watch?v=qLqttdO33UM&t=2016s)
- Software reliability is a solved problem in aerospace and critical industries
- Agentic coding can make high-assurance code 100x cheaper than typical software today
- This makes bug-free experiences economically viable for mainstream applications
- Zero-bug vision addresses current limitations of agentic coding around code quality
- **Adoption tipping point**: When agentic coding routinely produces fewer defects than human-written code
- We've known how to build reliable software for decades - now we can make it economically accessible

### [Closing: Tardigrades and Temporal](https://www.youtube.com/watch?v=qLqttdO33UM&t=2111s)
- Ziggy the tardigrade is Temporal's mascot (not a bug!)
- Tardigrades are extremely resilient animals that can survive in outer space
- Temporal sent Ziggy to space to prove the point
- Temporal builds durable execution as reliable foundation for modern software
- Invitation to collaborate on building more reliable software systems

---

## Key Takeaways

1. **Zero-bug software is achievable** - proven by aerospace industry (Airbus A320, Space Shuttle, Curiosity Rover)

2. **Cost barrier is falling** - agentic coding can produce high-assurance code 100x cheaper than traditional methods

3. **Formal methods work** - Daphne, seL4, CompCert demonstrate practical verification at commercial scale

4. **Process matters** - quality through rigorous engineering processes (specification, verification, testing)

5. **Modularity scales** - essential for managing complexity in both human and AI-generated code

6. **Economic viability** - gap between high-assurance and typical software (100x) smaller than efficiency gains from AI (1000-10,000x)

7. **Practical techniques available now** - risk analysis, safety cases, separate verification prompts, formal methods for critical sections

8. **Software 3.0 challenges** - LLMs are non-deterministic but offer new forms of resilience through handling ambiguity

9. **Adoption accelerator** - when AI routinely produces fewer defects than humans, expect massive adoption

10. **Historical lessons apply** - high-level languages, structured programming, and modularity as valuable for LLMs as for humans
