# Building Agents (the hard parts!) - Rita Kozlov, Cloudflare

**Video URL:** https://www.youtube.com/watch?v=j_TKDweOsYE

---

## Executive Summary

Rita Kozlov, VP of Product for Cloudflare's developer platform, delivers a comprehensive technical talk on building production-ready AI agents. She addresses the infrastructure challenges developers face when building agents, specifically focusing on four core components: client interfaces, AI reasoning, workflows, and tools. The presentation emphasizes practical solutions using Cloudflare's Agents SDK and the Model Context Protocol (MCP), demonstrating how to overcome common challenges like OAuth implementation, state management, long-running workflows, and human-in-the-loop approvals. Rita showcases real-world examples including a book recommendation system and a credit card approval workflow, highlighting how modern infrastructure can simplify agent development from months of work to minutes of deployment.

---

## Main Topics

### 1. **Introduction to Cloudflare and AI Paradigm Shift** ([00:17](https://www.youtube.com/watch?v=j_TKDweOsYE&t=17s) - [03:03](https://www.youtube.com/watch?v=j_TKDweOsYE&t=183s))

- Cloudflare handles ~20% of internet traffic and provides developer services including functions, storage, compute, and AI inference
- AI adoption has accelerated dramatically: 44% of developers used AI a year ago, now over 76% use it daily
- Knowledge worker AI adoption already surpassed Gartner's 2030 predictions (75% vs predicted 50%)
- Industry shift from training workloads to inference workloads (OpenAI O1, DeepSeek models)
- The next evolution: moving from augmentation to full automation with agentic workflows

**Key Quote:** "We have the opportunity to not just augment people's work... but what's really powerful is to go and say hey I have a campaign I want to run. Grab me a full list of customers... draft me up the email... send it to me for approval... ping me when the customer responds."

### 2. **The Business Impact of AI Agents** ([03:43](https://www.youtube.com/watch?v=j_TKDweOsYE&t=223s) - [05:14](https://www.youtube.com/watch?v=j_TKDweOsYE&t=314s))

Early adopters are seeing significant results:
- **20% revenue increases** from sales automation agents
- **90% faster response times** to support queries
- **50-75% time savings** across various workflows

These metrics demonstrate that agents are already reshaping business operations, not just theoretical improvements.

### 3. **The Four Components of Agent Architecture** ([05:16](https://www.youtube.com/watch?v=j_TKDweOsYE&t=316s) - [06:06](https://www.youtube.com/watch?v=j_TKDweOsYE&t=366s))

Rita breaks down agent architecture into four essential pieces:

1. **Client** - The interface for human interaction (voice via WebRTC, chat UI)
2. **AI** - The reasoning/thinking component (LLM that decides next actions)
3. **Workflows** - The executive branch that tracks and executes actions
4. **Tools** - Access to APIs, browsers, databases, and services needed to take actions

**Example Workflow:** CRM agent that contacts conference attendees
- Client: Voice interface or chat UI
- AI: Determines which contacts to reach, drafts personalized emails
- Workflow: Manages the sequence of getting contacts → drafting → approval → sending
- Tools: Access to CRM database, email services, notification systems

### 4. **Tools Layer: Model Context Protocol (MCP)** ([07:38](https://www.youtube.com/watch?v=j_TKDweOsYE&t=458s) - [10:06](https://www.youtube.com/watch?v=j_TKDweOsYE&t=606s))

**MCP Overview:**
- Introduced by Anthropic in November, standardizes how LLMs interact with tools
- The real breakthrough: LLMs became exceptionally good at tool calling
- Respects traditional client-server architecture with multiple client support

**Four Core MCP Concepts:**
1. **Resources** - File contents, database records, data sources
2. **Prompts** - Pre-defined interaction patterns (you can prompt your agent better than anyone else)
3. **Tooling** - Actual executable functions and queries
4. **Sampling** - Allows LLM to use shorthand and complete reasoning (not widely adopted yet)

**The Hard Parts of Building MCP:**
- Transport protocol over SSE and WebSockets
- OAuth authentication implementation
- Memory/state management

### 5. **Cloudflare Agents SDK - The Cheat Code** ([10:06](https://www.youtube.com/watch?v=j_TKDweOsYE&t=606s) - [14:29](https://www.youtube.com/watch?v=j_TKDweOsYE&t=869s))

**Key Features:**
- **MCP Server Hosting** - Built-in MCP class with OAuth, HTTP streaming, transport all included
- **State Management via Durable Objects** - Serverless functions with attached state (no database setup required)
- **Real-time WebSocket Communication** - Makes chat interfaces trivial
- **React Integration Hooks** - Frontend integration made easy
- **Basic Chat Capabilities** - Common patterns built-in

**Deployment Speed:** "Less than a minute to get your initial MCP server up and running" with a "Deploy to Cloudflare" button.

**Enterprise Adoption:** Companies like Atlassian, Asana, Stripe, and Intercom are building MCP servers using this approach.

### 6. **Practical Example: Book Recommendation MCP Server** ([11:51](https://www.youtube.com/watch?v=j_TKDweOsYE&t=711s) - [13:57](https://www.youtube.com/watch?v=j_TKDweOsYE&t=837s))

**Implementation Details:**
```typescript
class BookRecommendationMCP extends MCPAgent {
  // Initial empty state
  state = { genres: [], books: [] }

  // Tool: Add genre preference
  addGenre(genre) {
    this.state.genres.push(genre)
    // Automatically persisted!
  }

  // Tool: Get recommendations
  getRecommendations() {
    // Uses stored preferences
    return recommendations
  }

  // Personalized prompt for recommendations
  prompt: "Recommend books to someone who likes ${genres} and has read ${books}"
}
```

**Key Advantages:**
- Memory persists across all interactions and all MCP clients
- No separate database setup needed
- Scales automatically
- Runs close to AI agent (low latency)
- Infrastructure abstraction - just write logic

**Traditional Approach vs. MCP Agent:**
- Traditional: Set up database, manage connections, handle scaling, added latency
- MCP Agent: Memory built-in, automatic scaling, low latency, zero infrastructure management

### 7. **Workflows Layer: Long-Running Tasks & Human-in-the-Loop** ([14:29](https://www.youtube.com/watch?v=j_TKDweOsYE&t=869s) - [18:45](https://www.youtube.com/watch?v=j_TKDweOsYE&t=1125s))

**Challenges:**
- Reasoning LLMs can take several minutes to respond
- Humans in the loop can take minutes, hours, days, or months
- Need to maintain WebSocket persistence
- Require retry logic
- Must handle horizontal scaling

**Real-World Example: Knock Credit Card Approval Agent** ([15:29](https://www.youtube.com/watch?v=j_TKDweOsYE&t=929s))

**Workflow Steps:**
1. User requests new card via chat interface
2. Agent uses `issueCard` tool wrapped in `requireHumanInput`
3. Knock sends approval notification (email/Slack/in-app)
4. Tool call deferred until approval received
5. Approval routes back to correct agent via durable object
6. Card issued and user notified
7. State management prevents duplicate approvals

**Implementation Highlights:**
```typescript
// Frontend: React integration
import { useAgent } from '@cloudflare/agents-react'
const chat = useAgent({ /* config */ })

// Backend: Require human approval
requireHumanInput(issueCardTool)

// Routing: Handle approvals
async handleApproval(userId, status) {
  const agent = getAgentByUserId(userId)
  if (status === 'approved') {
    agent.resumeDeferredToolCall()
  }
}

// State: Prevent duplicates
if (this.state.cardRequested && this.state.approved) {
  return // Already processed
}
```

**Key Benefits:**
- Durable objects handle routing to correct agent automatically
- State prevents duplicate actions
- WebSocket persistence built-in
- No manual infrastructure management

### 8. **AI/Reasoning Layer** ([18:47](https://www.youtube.com/watch?v=j_TKDweOsYE&t=1127s) - [19:15](https://www.youtube.com/watch?v=j_TKDweOsYE&t=1155s))

Rita deliberately skips this section, noting:
- The entire conference covers model selection and evaluation better than she could
- References Logan's Gemini talk as excellent coverage
- Multiple sessions on evals provide comprehensive guidance
- Focus remains on the infrastructure challenges unique to agent deployment

### 9. **Client Layer: Meeting Users Where They Are** ([19:15](https://www.youtube.com/watch?v=j_TKDweOsYE&t=1155s) - [20:47](https://www.youtube.com/watch?v=j_TKDweOsYE&t=1247s))

**The MCP Advantage:** Build your server once, support multiple clients

**No-Code Options:**
- **Cursor** - Supports remote MCP servers (for developer users)
- **Claude** - Native remote MCP support
- **ChatGPT** - Remote MCP integration
- Users can interact with your agent instantly through tools they already use

**Custom Client Options:**
- Build your own MCP client for custom workflows
- Control over both client and server enables sophisticated agentic patterns
- Not limited to UI - can use **voice interfaces** via WebRTC
- Cloudflare provides WebRTC-to-WebSocket translation tools
- MCP clients easily understand these connections

**Key Insight:** "You don't have to build a UI yourself at all" if your users are already on platforms supporting remote MCP.

### 10. **Summary and Getting Started** ([20:47](https://www.youtube.com/watch?v=j_TKDweOsYE&t=1247s) - [21:03](https://www.youtube.com/watch?v=j_TKDweOsYE&t=1263s))

**The Four Essential Pieces:**
1. Client (voice, chat, existing tools)
2. AI (reasoning layer)
3. Workflows (execution and state management)
4. Tools (MCP servers)

**Recommendation:** Start with Cloudflare Agents SDK to get running in minutes rather than months.

**Resources:** Blog post with "Deploy to Cloudflare" button for immediate hands-on experience.

---

## Key Takeaways

1. **Agent adoption is accelerating faster than predicted** - 76% of developers already using AI, surpassing 2030 estimates by 2024

2. **The hard parts of agent building are infrastructure, not AI** - OAuth, state management, WebSocket persistence, and workflow orchestration are the real challenges

3. **MCP is game-changing for tool integration** - Standardizes how LLMs interact with tools, and LLMs are now exceptionally good at tool calling

4. **State management should be built-in, not bolted-on** - Durable objects provide serverless functions with attached state, eliminating database complexity

5. **Human-in-the-loop requires special handling** - Long-running tasks with variable latency (minutes to months) need sophisticated workflow management

6. **Build once, deploy everywhere** - MCP servers work with multiple clients (Cursor, Claude, ChatGPT, custom apps)

7. **Time-to-production drastically reduced** - From months of infrastructure work to minutes with proper abstractions

8. **Real business impact is measurable** - 20% revenue increases, 90% faster support, 50-75% time savings

---

## Technical Architecture Summary

```
┌─────────────────────────────────────────────────────────┐
│                         CLIENT                          │
│  (Voice/WebRTC, Chat UI, Cursor, Claude, ChatGPT)      │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                      AI REASONING                       │
│         (LLM with Gateway, Caching, Evals)             │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                      WORKFLOWS                          │
│    (Durable Objects - State + Execution Logic)         │
│    - Long-running tasks                                 │
│    - Human-in-the-loop approvals                       │
│    - WebSocket persistence                             │
│    - Duplicate prevention                              │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                        TOOLS                            │
│              (MCP Servers on Durable Objects)          │
│    - Resources (files, databases)                      │
│    - Prompts (interaction patterns)                    │
│    - Tools (executable functions)                      │
│    - Sampling (LLM shortcuts)                          │
│    Connected to: APIs, Browsers, Vector DBs, Services  │
└─────────────────────────────────────────────────────────┘
```

---

**Last Updated:** 2026-01-03
