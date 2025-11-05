# AWS Bedrock: Multi-LLM Providers & Agent Frameworks

This example demonstrates how to use AWS Bedrock with multiple LLM providers and integrate with popular agent frameworks (CrewAI and LangGraph).

## Requirements

**Python Version**: Requires Python 3.11 or higher (for TypedDict and advanced type hints)

**Dependencies**: Automatically managed via inline script metadata:
- `boto3>=1.34.0` - AWS SDK for Python
- `langchain>=0.1.0` - LangChain framework
- `langchain-aws>=0.1.0` - LangChain AWS integrations
- `langgraph>=0.0.40` - LangGraph state machine framework
- `crewai>=0.1.0` - CrewAI multi-agent framework
- `crewai-tools>=0.1.0` - CrewAI tools

**AWS Requirements**:
- Valid AWS credentials with Amazon Bedrock access
- AWS region with Bedrock model access (e.g., us-east-1, us-west-2)
- Model access enabled for: Claude, Titan, Llama, etc.

## Usage

```bash
# Run with uv (recommended)
uv run python main_aws_bedrock_agents.py

# Or with proper AWS credentials
AWS_REGION=us-east-1 uv run python main_aws_bedrock_agents.py
```

## Architecture Overview

The demo is structured in three main parts:

1. **Multiple LLM Providers** (Lines 45-85): Demonstrates accessing different models
2. **CrewAI Integration** (Lines 100-155): Multi-agent collaboration
3. **LangGraph Integration** (Lines 190-260): State machine-based agent flow

---

## Part 1: Multiple LLM Providers

### Source Code (Lines 45-85)

```python
45  def demo_multiple_llm_providers():
46      """
47      Demonstrates using multiple LLM providers through AWS Bedrock.
48      Lines 45-85: Multiple provider setup and invocation
49      """
50      print("=" * 80)
51      print("PART 1: AWS BEDROCK - MULTIPLE LLM PROVIDERS")
52      print("=" * 80)
53
54      # Available model IDs on AWS Bedrock
55      providers = {
56          "Anthropic Claude 3 Sonnet": "anthropic.claude-3-sonnet-20240229-v1:0",
57          "Anthropic Claude 3.5 Sonnet": "anthropic.claude-3-5-sonnet-20240620-v1:0",
58          "Amazon Titan Text Express": "amazon.titan-text-express-v1",
59          "Meta Llama 3 8B": "meta.llama3-8b-instruct-v1:0",
60          "AI21 Jamba Instruct": "ai21.jamba-instruct-v1:0",
61      }
62
63      prompt = "Explain what AWS Bedrock is in one sentence."
64
65      # Line 65: Iterate through different providers
66      for provider_name, model_id in providers.items():
67          print(f"\n📍 Provider: {provider_name}")
68          print(f"   Model ID: {model_id}")
69
70          try:
71              # Line 72: Initialize Bedrock client for specific model
72              llm = ChatBedrock(
73                  model_id=model_id,
74                  region_name=os.getenv("AWS_REGION", "us-east-1"),
75                  model_kwargs={
76                      "max_tokens": 200,
77                      "temperature": 0.7,
78                  }
79              )
80
81              # Line 82: Invoke the model
82              response = llm.invoke(prompt)
83              print(f"   Response: {response.content[:150]}...")
84
85          except Exception as e:
```

### Expected Output

```
================================================================================
PART 1: AWS BEDROCK - MULTIPLE LLM PROVIDERS
================================================================================

📍 Provider: Anthropic Claude 3 Sonnet
   Model ID: anthropic.claude-3-sonnet-20240229-v1:0
   Response: AWS Bedrock is a fully managed service that provides access to high-performing foundation models from leading AI companies through a single API...

📍 Provider: Anthropic Claude 3.5 Sonnet
   Model ID: anthropic.claude-3-5-sonnet-20240620-v1:0
   Response: AWS Bedrock is Amazon's fully managed service that provides access to foundation models from multiple AI providers through a unified API...

📍 Provider: Amazon Titan Text Express
   Model ID: amazon.titan-text-express-v1
   Response: AWS Bedrock is a fully managed service that offers access to foundation models from Amazon and leading AI startups via an API...

📍 Provider: Meta Llama 3 8B
   Model ID: meta.llama3-8b-instruct-v1:0
   Response: AWS Bedrock is a fully managed service that provides access to large language models (LLMs) from various providers through a single API...

📍 Provider: AI21 Jamba Instruct
   Model ID: ai21.jamba-instruct-v1:0
   Response: AWS Bedrock is a managed service that provides API access to various foundation models from different AI companies...

✅ Multiple provider demonstration complete
```

### Annotations

- **Lines 55-61**: Define available LLM providers on AWS Bedrock. Each provider has a unique model ID.
- **Line 72-79**: `ChatBedrock` initializes a client for a specific model. The same API works across all providers.
- **Line 82**: Single invoke method works uniformly across different models - this is the power of AWS Bedrock's unified interface.
- **Output**: Notice how each provider gives slightly different responses to the same prompt, showcasing their unique capabilities.

---

## Part 2: CrewAI Integration

### Source Code (Lines 100-155)

```python
100 def demo_crewai_integration():
101     """
102     Demonstrates CrewAI framework with AWS Bedrock models.
103     Lines 100-155: CrewAI agent setup and execution
104     """
105     print("=" * 80)
106     print("PART 2: CREWAI FRAMEWORK INTEGRATION")
107     print("=" * 80)
108
109     # Line 109: Initialize Bedrock LLM for CrewAI
110     bedrock_llm = ChatBedrock(
111         model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
112         region_name=os.getenv("AWS_REGION", "us-east-1"),
113         model_kwargs={"max_tokens": 1000, "temperature": 0.7}
114     )
115
116     # Line 117: Create specialized agents
117     print("\n📍 Creating CrewAI agents with Bedrock LLMs...")
118
119     researcher = Agent(
120         role="AI Research Analyst",
121         goal="Research and explain AI concepts clearly",
122         backstory="Expert in artificial intelligence and cloud computing",
123         llm=bedrock_llm,
124         verbose=True
125     )
126
127     writer = Agent(
128         role="Technical Writer",
129         goal="Write clear technical documentation",
130         backstory="Experienced technical writer specializing in cloud technologies",
131         llm=bedrock_llm,
132         verbose=True
133     )
134
135     # Line 136: Define tasks for agents
136     print("\n📍 Defining tasks...")
137
138     research_task = Task(
139         description="Research AWS Bedrock's key features and benefits",
140         expected_output="A list of 3 key features of AWS Bedrock",
141         agent=researcher
142     )
143
144     writing_task = Task(
145         description="Write a brief summary of AWS Bedrock based on the research",
146         expected_output="A 2-sentence summary of AWS Bedrock",
147         agent=writer
148     )
149
150     # Line 151: Create and execute crew
151     print("\n📍 Executing CrewAI crew...")
152
153     crew = Crew(
154         agents=[researcher, writer],
155         tasks=[research_task, writing_task],
```

### Expected Output

```
================================================================================
PART 2: CREWAI FRAMEWORK INTEGRATION
================================================================================

📍 Creating CrewAI agents with Bedrock LLMs...

📍 Defining tasks...

📍 Executing CrewAI crew...

[AI Research Analyst] Analyzing AWS Bedrock features...

[AI Research Analyst] Research Complete:
1. Multi-Model Access: Bedrock provides access to multiple foundation models from
   various providers (Anthropic, Meta, Amazon, AI21, etc.) through a single API.
2. Fully Managed: No infrastructure management required - AWS handles model hosting,
   scaling, and availability.
3. Customization & Security: Supports fine-tuning with your data while keeping it
   private and secure within your AWS environment.

[Technical Writer] Synthesizing research findings...

✅ CrewAI Result:
   AWS Bedrock is Amazon's fully managed service that provides unified API access to
   multiple foundation models from leading AI companies. It enables organizations to
   build generative AI applications securely with the ability to customize models
   using their own data without complex infrastructure management.
```

### Annotations

- **Lines 119-133**: CrewAI agents are defined with roles, goals, and backstories. Each agent uses the Bedrock LLM (line 123, 131).
- **Lines 138-148**: Tasks are assigned to specific agents. The `researcher` agent works first, then hands off to the `writer` agent.
- **Line 153-155**: The `Crew` orchestrates multi-agent collaboration. Agents work sequentially on their tasks.
- **Output**: Notice the sequential workflow - researcher completes analysis first, then writer synthesizes the findings.
- **Key Benefit**: CrewAI excels at role-based collaboration where different specialized agents contribute their expertise.

---

## Part 3: LangGraph Integration

### Source Code (Lines 190-260)

```python
179 class AgentState(TypedDict):
180     """State definition for LangGraph agent"""
181     messages: list
182     next_action: str
183
184
185 def demo_langgraph_integration():
186     """
187     Demonstrates LangGraph framework with AWS Bedrock models.
188     Lines 190-260: LangGraph state machine setup and execution
189     """
190     print("=" * 80)
191     print("PART 3: LANGGRAPH FRAMEWORK INTEGRATION")
192     print("=" * 80)
193
194     # Line 199: Initialize Bedrock LLM for LangGraph
195     bedrock_llm = ChatBedrock(
196         model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
197         region_name=os.getenv("AWS_REGION", "us-east-1"),
198         model_kwargs={"max_tokens": 500, "temperature": 0.5}
199     )
200
201     # Line 207: Define agent nodes
202     def research_node(state: AgentState) -> AgentState:
203         """Research node: Gathers information"""
204         print("\n📍 LangGraph Node: RESEARCH")
205         prompt = "List 3 benefits of using AWS Bedrock for AI applications."
206         response = bedrock_llm.invoke(prompt)
207
208         state["messages"].append({
209             "role": "research",
210             "content": response.content
211         })
212         state["next_action"] = "analyze"
213
214         print(f"   Research Output: {response.content[:100]}...")
215         return state
216
217     def analyze_node(state: AgentState) -> AgentState:
218         """Analysis node: Processes research"""
219         print("\n📍 LangGraph Node: ANALYZE")
220         research_content = state["messages"][-1]["content"]
221         prompt = f"Based on this research: '{research_content[:200]}', provide a one-sentence key insight."
222         response = bedrock_llm.invoke(prompt)
223
224         state["messages"].append({
225             "role": "analysis",
226             "content": response.content
227         })
228         state["next_action"] = "end"
229
230         print(f"   Analysis Output: {response.content}")
231         return state
232
233     # Line 242: Build state graph
234     print("\n📍 Building LangGraph state machine...")
235
236     workflow = StateGraph(AgentState)
237
238     # Line 247: Add nodes
239     workflow.add_node("research", research_node)
240     workflow.add_node("analyze", analyze_node)
241
242     # Line 251: Define edges (transitions)
243     workflow.set_entry_point("research")
244     workflow.add_edge("research", "analyze")
245     workflow.add_edge("analyze", END)
246
247     # Line 256: Compile and execute
248     app = workflow.compile()
249
250     print("\n📍 Executing LangGraph workflow...")
251     initial_state: AgentState = {
252         "messages": [],
253         "next_action": "research"
254     }
255
256     final_state = app.invoke(initial_state)
```

### Expected Output

```
================================================================================
PART 3: LANGGRAPH FRAMEWORK INTEGRATION
================================================================================

📍 Building LangGraph state machine...

📍 Executing LangGraph workflow...

📍 LangGraph Node: RESEARCH
   Research Output: Here are 3 key benefits of using AWS Bedrock for AI applications:

   1. **Model Diversity**: Access...

📍 LangGraph Node: ANALYZE
   Analysis Output: The primary insight is that AWS Bedrock provides a unified, secure,
   and scalable platform for accessing diverse foundation models, enabling rapid AI
   application development without infrastructure overhead.

✅ LangGraph Final State:
   [RESEARCH]: Here are 3 key benefits of using AWS Bedrock for AI applications:

   1. **Model Diversity**: Access multiple foundation models from leading providers through
      a single API, enabling flexibility to choose the best model for specific use cases.

   2. **Security & Privacy**: Keep your data private and secure within your AWS environment
      with built-in compliance features and data governance controls.

   3. **Simplified Deployment**: Fully managed infrastructure means no server management,
      automatic scaling, and reduced operational complexity for production AI applications...

   [ANALYSIS]: The primary insight is that AWS Bedrock provides a unified, secure, and
   scalable platform for accessing diverse foundation models, enabling rapid AI application
   development without infrastructure overhead.

✅ LangGraph integration demonstration complete
```

### Annotations

- **Lines 179-182**: `AgentState` TypedDict defines the state schema that flows through the graph.
- **Lines 202-231**: Each node is a function that receives state, calls Bedrock LLM, and returns updated state.
- **Lines 239-245**: The graph structure is explicitly defined with nodes and edges (transitions).
- **Line 243-245**: Workflow flows from `research` → `analyze` → `END`, creating a linear pipeline.
- **Line 256**: The compiled graph is invoked with initial state, and state flows through each node.
- **Output**: Notice the structured state machine execution - each node processes and passes state to the next.
- **Key Benefit**: LangGraph excels at complex, stateful workflows where explicit control over execution flow is needed.

---

## Comparison: CrewAI vs LangGraph

| Aspect | CrewAI | LangGraph |
|--------|--------|-----------|
| **Paradigm** | Role-based multi-agent collaboration | State machine with explicit graph |
| **Best For** | Team-like agent interactions | Complex workflows with branching |
| **State Management** | Implicit (handled by framework) | Explicit (TypedDict state) |
| **Control** | High-level, declarative | Low-level, imperative |
| **Code Example** | Lines 100-155 | Lines 185-260 |

---

## Key Takeaways

1. **AWS Bedrock Unified Interface**:
   - Lines 72-79 show the same `ChatBedrock` API works across all providers
   - Switch models by changing `model_id` parameter only

2. **CrewAI for Collaboration**:
   - Lines 119-133: Define agents with roles and expertise
   - Best for workflows requiring specialized agent collaboration

3. **LangGraph for Complex Workflows**:
   - Lines 236-245: Explicit graph definition with nodes and edges
   - Best for workflows requiring precise control and state management

4. **Framework Agnostic**:
   - Both frameworks seamlessly integrate with Bedrock
   - Same `bedrock_llm` object works in both contexts (lines 110, 195)

---

## Troubleshooting

### AWS Credentials Not Found
```bash
# Configure AWS CLI
aws configure

# Or set environment variables
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_REGION=us-east-1
```

### Model Access Denied
- Go to AWS Console → Bedrock → Model Access
- Request access to models (Claude, Titan, Llama, etc.)
- Access approval may take a few minutes

### ImportError
```bash
# Ensure uv is installed
pip install uv

# Run with uv to auto-install dependencies
uv run python main_aws_bedrock_agents.py
```

---

## Further Reading

- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [LangChain AWS Integration](https://python.langchain.com/docs/integrations/platforms/aws)
- [CrewAI Documentation](https://docs.crewai.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)

---

## License

This example is for educational purposes demonstrating AWS Bedrock integration patterns.
