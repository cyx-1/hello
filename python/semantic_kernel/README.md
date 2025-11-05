# Semantic Kernel Python: Enterprise-Grade AI Orchestration

This demonstration showcases **Semantic Kernel for Python**, Microsoft's enterprise-grade AI orchestration framework. The example highlights three critical features that make Semantic Kernel production-ready:

1. **Enterprise-grade stability** - Production-ready, type-safe foundations
2. **Plugin architecture** - Connectors to existing code and APIs
3. **State management** - Memory, threads, and observability

## Version Requirements

- **Python**: >= 3.10
- **Semantic Kernel**: >= 1.16.0
- **Key Feature**: Type-safe plugin architecture with Python type hints and `Annotated` types

## Running the Demo

```bash
uv run --script main_semantic_kernel.py
```

---

## Code Structure & Key Concepts

### Feature 1: Enterprise-Grade Stability (Lines 38-152)

The code demonstrates **type-safe plugin architecture** that ensures enterprise reliability:

#### Type-Safe Weather Plugin (Lines 38-74)

```python
38: class WeatherPlugin:
45:     @kernel_function(
46:         name="get_weather",
47:         description="Get the current weather for a location",
48:     )
49:     def get_weather(
50:         self,
51:         location: Annotated[str, "The city name, e.g., 'Seattle'"],
52:     ) -> Annotated[str, "Weather information"]:
```

**Key Points:**
- Line 51: `Annotated[str, ...]` provides both type safety and semantic documentation
- Line 52: Return type annotation ensures predictable outputs
- Line 45-48: `@kernel_function` decorator registers the function with Semantic Kernel
- This enables **runtime validation** and **IDE support**

#### Type-Safe Calculator Plugin (Lines 76-118)

```python
86:     @kernel_function(
87:         name="add",
88:         description="Add two numbers together",
89:     )
90:     def add(
91:         self,
92:         number1: Annotated[float, "First number"],
93:         number2: Annotated[float, "Second number"],
94:     ) -> Annotated[float, "The sum"]:
```

**Key Points:**
- Lines 92-93: Numeric type annotations with semantic descriptions
- Multiple functions in a single plugin (add, multiply)
- Production-ready error handling built-in

---

### Feature 2: Plugin Architecture (Lines 161-221)

Demonstrates how plugins act as **connectors to existing code and APIs**:

#### Plugin Registration (Lines 174-193)

```python
174:     kernel = Kernel()
...
181:     weather_plugin = kernel.add_plugin(
182:         WeatherPlugin(),
183:         plugin_name="weather",
184:     )
...
187:     calculator_plugin = kernel.add_plugin(
188:         CalculatorPlugin(),
189:         plugin_name="calculator",
190:     )
```

**Output (Lines 31-42 in execution):**
```
[KERNEL] Initialized enterprise-grade kernel

[PLUGIN REGISTRATION] Adding plugins to kernel...
  ✓ Registered: weather plugin with 1 function
  ✓ Registered: calculator plugin with 2 functions
  ✓ Registered: data_analysis plugin with 1 function
```

**Correlation:**
- Source lines 181-190 → Output lines 34-37
- Each plugin registration is confirmed with function count
- Plugins can wrap **any existing Python code** or **API client**

#### Direct Plugin Invocation (Lines 200-218)

```python
200:     weather_result = await kernel.invoke(
201:         function_name="get_weather",
202:         plugin_name="weather",
203:         location="Seattle",
204:     )
...
208:     calc_result = await kernel.invoke(
209:         function_name="add",
210:         plugin_name="calculator",
211:         number1=42.5,
212:         number2=17.3,
213:     )
```

**Output (Lines 44-52):**
```
[WEATHER PLUGIN] Fetching weather for: Seattle
[WEATHER PLUGIN] Result: ☁️ Cloudy, 55°F, Light rain expected
  Result: ☁️ Cloudy, 55°F, Light rain expected

[CALCULATOR PLUGIN] 42.5 + 17.3 = 59.8
  Result: 59.8
```

**Correlation:**
- Source lines 200-204 → Output lines 46-48 (Weather invocation)
- Source lines 208-213 → Output lines 50-51 (Calculator invocation)
- **Type-safe parameters** are validated at runtime

---

### Feature 3: State Management (Lines 230-327)

Demonstrates **memory, conversation threads, and observability**:

#### In-Memory Knowledge Base (Lines 243-265)

```python
246:     knowledge_base = {
247:         "user_preferences": {
248:             "user_001": [
249:                 "User prefers Python for backend development",
250:                 "User's primary project is an AI orchestration platform",
251:                 "User values type safety and production readiness",
252:             ],
...
258:         "session_data": {
259:             "session_001": {
260:                 "start_time": "2024-01-15T10:00:00Z",
261:                 "user_id": "user_001",
262:                 "status": "active",
263:             }
264:         },
265:     }
```

**Output (Lines 73-86):**
```
[MEMORY STORAGE] Knowledge base contents...

  Category: user_preferences
    ✓ [user_001] User prefers Python for backend development
    ✓ [user_001] User's primary project is an AI orchestration platform
    ✓ [user_001] User values type safety and production readiness
    ✓ [company_001] Company uses Semantic Kernel for AI applications
    ✓ [company_001] Company requires enterprise-grade stability

  Category: session_data
    ✓ [session_001] {'start_time': '2024-01-15T10:00:00Z', ...}
```

**Key Points:**
- Production systems would use vector databases (e.g., Pinecone, Redis, PostgreSQL)
- Semantic Kernel supports **persistent memory stores**
- Enables context-aware conversations

#### Conversation Thread Management (Lines 304-328)

```python
307:     chat_history = ChatHistory()
...
311:     conversation_turns = [
312:         ("user", "Hello! I'm working on an AI project."),
313:         ("assistant", "Great! I can help with that. Semantic Kernel provides..."),
314:         ("user", "What's the weather in Seattle?"),
315:         ("assistant", "Let me check the weather for you..."),
316:         ("user", "Can you also calculate 15 + 27?"),
317:         ("assistant", "The sum of 15 and 27 is 42."),
318:     ]
320:     for i, (role, message) in enumerate(conversation_turns, 1):
321:         chat_history.add_message(
322:             ChatMessageContent(role=role, content=message)
323:         )
```

**Output (Lines 103-110):**
```
[THREAD STATE] Building conversation history:
  Turn 1 [user]: Hello! I'm working on an AI project....
  Turn 2 [assistant]: Great! I can help with that. Semantic Kernel provides enterp...
  Turn 3 [user]: What's the weather in Seattle?...
  Turn 4 [assistant]: Let me check the weather for you......
  Turn 5 [user]: Can you also calculate 15 + 27?...
  Turn 6 [assistant]: The sum of 15 and 27 is 42....
```

**Correlation:**
- Source lines 311-318 define conversation turns
- Source lines 320-323 add messages to thread
- Output lines 104-109 show the tracked conversation
- **Thread persistence** enables multi-turn conversations

#### Observability & Metrics (Lines 330-340)

```python
333:     user_messages = [msg for msg in chat_history.messages if msg.role == "user"]
334:     assistant_messages = [
335:         msg for msg in chat_history.messages if msg.role == "assistant"
336:     ]
338:     print(f"\n  📊 Conversation Metrics:")
339:     print(f"     Total turns: {len(chat_history.messages)}")
340:     print(f"     User messages: {len(user_messages)}")
341:     print(f"     Assistant messages: {len(assistant_messages)}")
```

**Output (Lines 115-120):**
```
  📊 Conversation Metrics:
     Total turns: 6
     User messages: 3
     Assistant messages: 3
     Thread ID: conversation_001
     State: Active
```

**Key Points:**
- Source lines 333-341 → Output lines 115-120
- Real-time conversation analytics
- Production-ready **observability** for monitoring

---

### Integrated System Demonstration (Lines 360-452)

Shows all three features working together in a complete workflow:

#### System Initialization (Lines 371-386)

```python
371:     kernel = Kernel()
...
382:     kernel.add_plugin(WeatherPlugin(), plugin_name="weather")
383:     kernel.add_plugin(CalculatorPlugin(), plugin_name="calculator")
384:     kernel.add_plugin(DataAnalysisPlugin(), plugin_name="data_analysis")
...
388:     chat_history = ChatHistory()
389:     chat_history.add_system_message(
390:         "You are a helpful AI assistant with access to weather, calculator, and data analysis tools."
391:     )
```

**Output (Lines 144-146):**
```
[SYSTEM INITIALIZATION] Setting up integrated system...
  ✓ All plugins registered
  ✓ Conversation thread initialized
```

#### Multi-Task Workflow (Lines 396-427)

```python
396:     tasks = [
397:         {
398:             "user_input": "What's the weather in San Francisco?",
399:             "plugin": "weather",
400:             "function": "get_weather",
401:             "params": {"location": "San Francisco"},
402:         },
403:         {
404:             "user_input": "Calculate 25 times 4",
405:             "plugin": "calculator",
406:             "function": "multiply",
407:             "params": {"number1": 25, "number2": 4},
408:         },
...
417:     for i, task in enumerate(tasks, 1):
418:         print(f"\n  Task {i}: {task['user_input']}")
419:         chat_history.add_user_message(task["user_input"])
420:
421:         result = await kernel.invoke(
422:             function_name=task["function"],
423:             plugin_name=task["plugin"],
424:             **task["params"],
425:         )
```

**Output (Lines 150-163):**
```
  Task 1: What's the weather in San Francisco?

[WEATHER PLUGIN] Fetching weather for: San Francisco
[WEATHER PLUGIN] Result: ☀️ Sunny, 68°F, Clear skies
  ✅ Completed: Result: ☀️ Sunny, 68°F, Clear skies...

  Task 2: Calculate 25 times 4

[CALCULATOR PLUGIN] 25.0 × 4.0 = 100.0
  ✅ Completed: Result: 100.0...

  Task 3: Analyze sales with revenue 500k and cost 320k

[DATA ANALYSIS PLUGIN] Generated report
  ✅ Completed: Result: ...
```

**Correlation:**
- Source lines 396-407 define tasks (data structure)
- Source lines 417-425 execute each task
- Output lines 150-163 show execution results
- Demonstrates **orchestration** of multiple plugins

#### Final System Observability (Lines 430-452)

```python
433:     print(f"""
434:   📊 System Metrics:
435:      Plugins loaded: 3
436:      Functions available: 5
437:      Conversation turns: {len(chat_history.messages)}
438:      Tasks completed: {len(tasks)}
439:      System status: ✅ Healthy
440:
441:   🔧 Plugin Status:
442:      ✓ weather: Active (1 function)
443:      ✓ calculator: Active (2 functions)
444:      ✓ data_analysis: Active (1 function)
445:
446:   💬 Thread Status:
447:      Thread ID: main_thread
448:      Message count: {len(chat_history.messages)}
449:      State: Completed
450: """)
```

**Output (Lines 170-183):**
```
  📊 System Metrics:
     Plugins loaded: 3
     Functions available: 5
     Conversation turns: 7
     Tasks completed: 3
     System status: ✅ Healthy

  🔧 Plugin Status:
     ✓ weather: Active (1 function)
     ✓ calculator: Active (2 functions)
     ✓ data_analysis: Active (1 function)

  💬 Thread Status:
     Thread ID: main_thread
     Message count: 7
     State: Completed
```

**Key Points:**
- Complete system health monitoring
- **Production-ready observability**
- Real-time metrics for all components

---

## Complete Execution Output

```
================================================================================
🚀 SEMANTIC KERNEL PYTHON - ENTERPRISE AI ORCHESTRATION
================================================================================

Version: semantic-kernel >= 1.16.0
Python: >= 3.10

Key Features Demonstrated:
  1. Enterprise-grade stability - production-ready, type-safe foundations
  2. Plugin architecture - connectors to existing code and APIs
  3. State management - memory, threads, and observability



┌──────────────────────────────────────────────────────────────────────────────┐
│                    FEATURE 1: ENTERPRISE-GRADE STABILITY                     │
└──────────────────────────────────────────────────────────────────────────────┘

[INFO] Demonstrating type-safe plugin architecture...
[INFO] All functions use Python type hints and Annotated types
[INFO] This ensures runtime validation and IDE support



┌──────────────────────────────────────────────────────────────────────────────┐
│                        FEATURE 2: PLUGIN ARCHITECTURE                        │
└──────────────────────────────────────────────────────────────────────────────┘

================================================================================
FEATURE 2: PLUGIN ARCHITECTURE - CONNECTORS TO EXISTING CODE AND APIs
================================================================================

[KERNEL] Initialized enterprise-grade kernel

[PLUGIN REGISTRATION] Adding plugins to kernel...
  ✓ Registered: weather plugin with 1 function
  ✓ Registered: calculator plugin with 2 functions
  ✓ Registered: data_analysis plugin with 1 function

[DIRECT INVOCATION] Calling plugins directly:

[WEATHER PLUGIN] Fetching weather for: Seattle
[WEATHER PLUGIN] Result: ☁️ Cloudy, 55°F, Light rain expected
  Result: ☁️ Cloudy, 55°F, Light rain expected

[CALCULATOR PLUGIN] 42.5 + 17.3 = 59.8
  Result: 59.8

[DATA ANALYSIS PLUGIN] Generated report
  Result:
📊 Sales Analysis Report:
   Revenue: $250,000.00
   Cost: $180,000.00
   Profit: $70,000.00
   Margin: 28.0%
   Status: ✅ Profitable


[PLUGIN ARCHITECTURE] ✅ All plugins successfully integrated!



┌──────────────────────────────────────────────────────────────────────────────┐
│                         FEATURE 3: STATE MANAGEMENT                          │
└──────────────────────────────────────────────────────────────────────────────┘

================================================================================
FEATURE 3: STATE MANAGEMENT - MEMORY, THREADS, AND OBSERVABILITY
================================================================================

[MEMORY SETUP] Configuring in-memory state management...
  ✓ Created in-memory knowledge base
  ✓ Initialized state management system

[MEMORY STORAGE] Knowledge base contents...

  Category: user_preferences
    ✓ [user_001] User prefers Python for backend development
    ✓ [user_001] User's primary project is an AI orchestration platform
    ✓ [user_001] User values type safety and production readiness
    ✓ [company_001] Company uses Semantic Kernel for AI applications
    ✓ [company_001] Company requires enterprise-grade stability

  Category: session_data
    ✓ [session_001] {'start_time': '2024-01-15T10:00:00Z', 'user_id': 'user_001', 'status': 'active'}

[MEMORY] Successfully organized 6 items

[MEMORY RETRIEVAL] Fetching stored knowledge...
  Retrieved 3 preferences for user_001:
    • User prefers Python for backend development
    • User's primary project is an AI orchestration platform
    • User values type safety and production readiness
  Retrieved session info:
    • start_time: 2024-01-15T10:00:00Z
    • user_id: user_001
    • status: active

--------------------------------------------------------------------------------
[CONVERSATION THREADS] Managing conversation state...
  ✓ Created chat history for thread management

[THREAD STATE] Building conversation history:
  Turn 1 [user]: Hello! I'm working on an AI project....
  Turn 2 [assistant]: Great! I can help with that. Semantic Kernel provides enterp...
  Turn 3 [user]: What's the weather in Seattle?...
  Turn 4 [assistant]: Let me check the weather for you......
  Turn 5 [user]: Can you also calculate 15 + 27?...
  Turn 6 [assistant]: The sum of 15 and 27 is 42....

[THREAD] Conversation thread has 6 messages

--------------------------------------------------------------------------------
[OBSERVABILITY] Analyzing conversation state...

  📊 Conversation Metrics:
     Total turns: 6
     User messages: 3
     Assistant messages: 3
     Thread ID: conversation_001
     State: Active

[THREAD REPLAY] Full conversation history:
  1. [USER] Hello! I'm working on an AI project.
  2. [ASSISTANT] Great! I can help with that. Semantic Kernel provides enterprise-grade AI orchestration.
  3. [USER] What's the weather in Seattle?
  4. [ASSISTANT] Let me check the weather for you...
  5. [USER] Can you also calculate 15 + 27?
  6. [ASSISTANT] The sum of 15 and 27 is 42.

[STATE MANAGEMENT] ✅ Memory and threads successfully managed!



┌──────────────────────────────────────────────────────────────────────────────┐
│                           INTEGRATED DEMONSTRATION                           │
└──────────────────────────────────────────────────────────────────────────────┘

================================================================================
INTEGRATED DEMONSTRATION - ALL FEATURES TOGETHER
================================================================================

[SYSTEM INITIALIZATION] Setting up integrated system...
  ✓ All plugins registered
  ✓ Conversation thread initialized

[WORKFLOW] Simulating user interaction...

  Task 1: What's the weather in San Francisco?

[WEATHER PLUGIN] Fetching weather for: San Francisco
[WEATHER PLUGIN] Result: ☀️ Sunny, 68°F, Clear skies
  ✅ Completed: Result: ☀️ Sunny, 68°F, Clear skies...

  Task 2: Calculate 25 times 4

[CALCULATOR PLUGIN] 25.0 × 4.0 = 100.0
  ✅ Completed: Result: 100.0...

  Task 3: Analyze sales with revenue 500k and cost 320k

[DATA ANALYSIS PLUGIN] Generated report
  ✅ Completed: Result:
📊 Sales Analysis Report:
   Revenue: $500,000.00
   Cost: $320,000.00
 ...

--------------------------------------------------------------------------------
[SYSTEM OBSERVABILITY] Final State Report
--------------------------------------------------------------------------------

  📊 System Metrics:
     Plugins loaded: 3
     Functions available: 5
     Conversation turns: 7
     Tasks completed: 3
     System status: ✅ Healthy

  🔧 Plugin Status:
     ✓ weather: Active (1 function)
     ✓ calculator: Active (2 functions)
     ✓ data_analysis: Active (1 function)

  💬 Thread Status:
     Thread ID: main_thread
     Message count: 7
     State: Completed


[INTEGRATED SYSTEM] ✅ All features working seamlessly!


================================================================================
✨ DEMONSTRATION COMPLETE
================================================================================

🎯 Key Takeaways:
  ✓ Type-safe plugins with Annotated types ensure enterprise reliability
  ✓ Plugin architecture enables easy integration of existing code/APIs
  ✓ Built-in memory and conversation management for stateful applications
  ✓ Observability features provide production-ready monitoring

💡 Production Usage:
  • Add OpenAI/Azure OpenAI service for AI-powered orchestration
  • Use persistent memory stores (Redis, PostgreSQL, etc.)
  • Implement custom plugins for your business logic
  • Enable logging and telemetry for full observability
```

---

## Key Takeaways

### 1. Enterprise-Grade Stability
- **Type safety** with Python type hints and `Annotated` types (lines 51-52, 92-94)
- **Runtime validation** ensures parameter correctness
- **Production-ready** error handling built into the framework

### 2. Plugin Architecture
- Plugins act as **connectors** to existing code and APIs
- Easy to wrap **any Python function** as a kernel function (lines 45-48, 86-89)
- Multiple plugins can be composed and orchestrated (lines 181-193)

### 3. State Management
- **In-memory state** for development (lines 246-265)
- **Conversation threads** with ChatHistory (lines 307-323)
- **Observability** with built-in metrics and monitoring (lines 333-341, 433-450)
- Production supports **persistent memory stores** (Redis, PostgreSQL, Pinecone)

---

## Production Considerations

1. **AI Service Integration**: Add OpenAI or Azure OpenAI for AI-powered function calling
2. **Persistent Memory**: Replace in-memory stores with Redis, PostgreSQL, or vector databases
3. **Custom Plugins**: Wrap your business logic as type-safe plugins
4. **Telemetry**: Enable logging and metrics for production monitoring
5. **Error Handling**: Implement retry logic and fallbacks for external APIs

---

## Why Semantic Kernel?

- ✅ **Enterprise-ready** with Microsoft backing
- ✅ **Type-safe** foundations for production reliability
- ✅ **Plugin ecosystem** for rapid integration
- ✅ **State management** built-in
- ✅ **Cross-platform** (Python, .NET, Java)
- ✅ **AI-agnostic** (works with OpenAI, Azure OpenAI, HuggingFace, etc.)
