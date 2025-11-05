#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "boto3>=1.34.0",
#     "langchain>=0.1.0",
#     "langchain-aws>=0.1.0",
#     "langgraph>=0.0.40",
#     "crewai>=0.1.0",
#     "crewai-tools>=0.1.0",
# ]
# ///
"""
AWS Bedrock Multi-LLM Provider and Agent Framework Integration Demo

This script demonstrates:
1. Using multiple LLM providers via AWS Bedrock (Anthropic Claude, Amazon Titan, Meta Llama)
2. Integration with CrewAI agent framework
3. Integration with LangGraph agent framework
"""

import os

try:
    from langchain_aws import ChatBedrock
    from crewai import Agent, Task, Crew
    from langgraph.graph import StateGraph, END
    from typing_extensions import TypedDict
except ImportError as e:
    print(f"⚠️  Import error: {e}")
    print("This demo requires AWS credentials and the specified dependencies.")
    print("Please install with: uv run python main_aws_bedrock_agents.py")
    exit(1)


# =============================================================================
# PART 1: AWS BEDROCK WITH MULTIPLE LLM PROVIDERS
# =============================================================================


def demo_multiple_llm_providers():
    """
    Demonstrates using multiple LLM providers through AWS Bedrock.
    Lines 45-85: Multiple provider setup and invocation
    """
    print("=" * 80)
    print("PART 1: AWS BEDROCK - MULTIPLE LLM PROVIDERS")
    print("=" * 80)

    # Available model IDs on AWS Bedrock
    providers = {
        "Anthropic Claude 3 Sonnet": "anthropic.claude-3-sonnet-20240229-v1:0",
        "Anthropic Claude 3.5 Sonnet": "anthropic.claude-3-5-sonnet-20240620-v1:0",
        "Amazon Titan Text Express": "amazon.titan-text-express-v1",
        "Meta Llama 3 8B": "meta.llama3-8b-instruct-v1:0",
        "AI21 Jamba Instruct": "ai21.jamba-instruct-v1:0",
    }

    prompt = "Explain what AWS Bedrock is in one sentence."

    # Line 65: Iterate through different providers
    for provider_name, model_id in providers.items():
        print(f"\n📍 Provider: {provider_name}")
        print(f"   Model ID: {model_id}")

        try:
            # Line 72: Initialize Bedrock client for specific model
            llm = ChatBedrock(
                model_id=model_id,
                region_name=os.getenv("AWS_REGION", "us-east-1"),
                model_kwargs={
                    "max_tokens": 200,
                    "temperature": 0.7,
                },
            )

            # Line 82: Invoke the model
            response = llm.invoke(prompt)
            print(f"   Response: {response.content[:150]}...")

        except Exception as e:
            print(f"   ⚠️  Error with {provider_name}: {str(e)[:100]}")

    print("\n✅ Multiple provider demonstration complete\n")


# =============================================================================
# PART 2: CREWAI INTEGRATION WITH AWS BEDROCK
# =============================================================================


def demo_crewai_integration():
    """
    Demonstrates CrewAI framework with AWS Bedrock models.
    Lines 100-155: CrewAI agent setup and execution
    """
    print("=" * 80)
    print("PART 2: CREWAI FRAMEWORK INTEGRATION")
    print("=" * 80)

    try:
        # Line 109: Initialize Bedrock LLM for CrewAI
        bedrock_llm = ChatBedrock(
            model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
            region_name=os.getenv("AWS_REGION", "us-east-1"),
            model_kwargs={"max_tokens": 1000, "temperature": 0.7},
        )

        # Line 117: Create specialized agents
        print("\n📍 Creating CrewAI agents with Bedrock LLMs...")

        researcher = Agent(
            role="AI Research Analyst",
            goal="Research and explain AI concepts clearly",
            backstory="Expert in artificial intelligence and cloud computing",
            llm=bedrock_llm,
            verbose=True,
        )

        writer = Agent(
            role="Technical Writer",
            goal="Write clear technical documentation",
            backstory="Experienced technical writer specializing in cloud technologies",
            llm=bedrock_llm,
            verbose=True,
        )

        # Line 136: Define tasks for agents
        print("\n📍 Defining tasks...")

        research_task = Task(
            description="Research AWS Bedrock's key features and benefits",
            expected_output="A list of 3 key features of AWS Bedrock",
            agent=researcher,
        )

        writing_task = Task(
            description="Write a brief summary of AWS Bedrock based on the research",
            expected_output="A 2-sentence summary of AWS Bedrock",
            agent=writer,
        )

        # Line 151: Create and execute crew
        print("\n📍 Executing CrewAI crew...")

        crew = Crew(
            agents=[researcher, writer],
            tasks=[research_task, writing_task],
            verbose=True,
        )

        result = crew.kickoff()

        print("\n✅ CrewAI Result:")
        print(f"   {result}")

    except Exception as e:
        print(f"\n⚠️  CrewAI demo error: {str(e)}")
        print("   Note: This requires valid AWS credentials with Bedrock access")

    print("\n✅ CrewAI integration demonstration complete\n")


# =============================================================================
# PART 3: LANGGRAPH INTEGRATION WITH AWS BEDROCK
# =============================================================================


class AgentState(TypedDict):
    """State definition for LangGraph agent"""

    messages: list
    next_action: str


def demo_langgraph_integration():
    """
    Demonstrates LangGraph framework with AWS Bedrock models.
    Lines 190-260: LangGraph state machine setup and execution
    """
    print("=" * 80)
    print("PART 3: LANGGRAPH FRAMEWORK INTEGRATION")
    print("=" * 80)

    try:
        # Line 199: Initialize Bedrock LLM for LangGraph
        bedrock_llm = ChatBedrock(
            model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
            region_name=os.getenv("AWS_REGION", "us-east-1"),
            model_kwargs={"max_tokens": 500, "temperature": 0.5},
        )

        # Line 207: Define agent nodes
        def research_node(state: AgentState) -> AgentState:
            """Research node: Gathers information"""
            print("\n📍 LangGraph Node: RESEARCH")
            prompt = "List 3 benefits of using AWS Bedrock for AI applications."
            response = bedrock_llm.invoke(prompt)

            state["messages"].append({"role": "research", "content": response.content})
            state["next_action"] = "analyze"

            print(f"   Research Output: {response.content[:100]}...")
            return state

        def analyze_node(state: AgentState) -> AgentState:
            """Analysis node: Processes research"""
            print("\n📍 LangGraph Node: ANALYZE")
            research_content = state["messages"][-1]["content"]
            prompt = f"Based on this research: '{research_content[:200]}', provide a one-sentence key insight."
            response = bedrock_llm.invoke(prompt)

            state["messages"].append({"role": "analysis", "content": response.content})
            state["next_action"] = "end"

            print(f"   Analysis Output: {response.content}")
            return state

        # Line 242: Build state graph
        print("\n📍 Building LangGraph state machine...")

        workflow = StateGraph(AgentState)

        # Line 247: Add nodes
        workflow.add_node("research", research_node)
        workflow.add_node("analyze", analyze_node)

        # Line 251: Define edges (transitions)
        workflow.set_entry_point("research")
        workflow.add_edge("research", "analyze")
        workflow.add_edge("analyze", END)

        # Line 256: Compile and execute
        app = workflow.compile()

        print("\n📍 Executing LangGraph workflow...")
        initial_state: AgentState = {"messages": [], "next_action": "research"}

        final_state = app.invoke(initial_state)

        print("\n✅ LangGraph Final State:")
        for msg in final_state["messages"]:
            print(f"   [{msg['role'].upper()}]: {msg['content'][:150]}...")

    except Exception as e:
        print(f"\n⚠️  LangGraph demo error: {str(e)}")
        print("   Note: This requires valid AWS credentials with Bedrock access")

    print("\n✅ LangGraph integration demonstration complete\n")


# =============================================================================
# MAIN EXECUTION
# =============================================================================


def main():
    """Main execution function"""
    print("\n" + "=" * 80)
    print("AWS BEDROCK: MULTI-LLM PROVIDERS & AGENT FRAMEWORKS DEMO")
    print("=" * 80)
    print("\nThis demo showcases:")
    print("  1. Multiple LLM providers via AWS Bedrock")
    print("  2. CrewAI agent framework integration")
    print("  3. LangGraph agent framework integration")
    print("\n" + "=" * 80 + "\n")

    # Check for AWS credentials
    if not os.getenv("AWS_ACCESS_KEY_ID") and not os.path.exists(
        os.path.expanduser("~/.aws/credentials")
    ):
        print("⚠️  WARNING: AWS credentials not detected!")
        print("   Set AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_REGION")
        print("   Or configure AWS CLI with 'aws configure'")
        print(
            "\n   Running in demonstration mode (will show structure but may fail API calls)\n"
        )

    # Run demonstrations
    demo_multiple_llm_providers()
    demo_crewai_integration()
    demo_langgraph_integration()

    print("=" * 80)
    print("DEMO COMPLETE")
    print("=" * 80)
    print("\n📚 Key Takeaways:")
    print("   • AWS Bedrock provides unified access to multiple LLM providers")
    print("   • CrewAI enables multi-agent collaboration with role-based agents")
    print("   • LangGraph offers state machine-based agent orchestration")
    print("   • All frameworks seamlessly integrate with Bedrock models\n")


if __name__ == "__main__":
    main()
