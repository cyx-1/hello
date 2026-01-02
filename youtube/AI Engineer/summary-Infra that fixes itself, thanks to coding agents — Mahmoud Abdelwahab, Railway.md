# Infra that fixes itself, thanks to coding agents — Mahmoud Abdelwahab, Railway

**Video URL:** https://www.youtube.com/watch?v=Q5IVm_CxN2w

---

## Executive Summary

Mahmoud Abdelwahab from Railway demonstrates a groundbreaking approach to infrastructure management where coding agents automatically detect, diagnose, and fix production issues. Instead of engineers being woken up by alerts and manually debugging problems, the system monitors application health, detects anomalies, and autonomously generates pull requests with fixes. The demo showcases a workflow that combines Railway's metrics API, durable execution patterns using Inngest, and OpenCode (an open-source coding agent) to create a self-healing infrastructure system.

---

## Main Topics

### [Introduction: The Problem with Current Infrastructure Monitoring](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=0s)
- **[00:00](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=0s)** - Traditional infrastructure issues: memory leaks, high error rates, slow response times
- **[00:13](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=13s)** - Example: Service with memory leak showing continuously growing memory usage
- **[00:32](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=32s)** - High number of 500 errors (94% error rate) and multi-second response times
- **[01:03](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=63s)** - Not all problems are obvious - some require deeper investigation
- **[01:28](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=88s)** - Example: Slow database queries causing 30+ second page load times

### [Traditional Alerting vs. Automated Fixing](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=120s)
- **[02:00](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=120s)** - Current approach: Set thresholds, get alerted, then manually investigate
- **[02:20](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=140s)** - Manual process: Dig through logs, metrics, traces to understand the issue
- **[02:33](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=153s)** - Proposed solution: Coding agent monitors infrastructure and ships fixes automatically
- **[02:53](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=173s)** - New workflow: Review a pull request instead of debugging from scratch

### [System Architecture Overview](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=186s)
- **[03:06](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=186s)** - Goal: Go from "issue detected" to "pull request opened" automatically
- **[03:26](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=206s)** - First workflow: Scheduled job (every 10-30 minutes) to monitor health
- **[03:37](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=217s)** - Step 1: Fetch application architecture (services, frontends, backends, crons, queues)
- **[03:52](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=232s)** - Step 2: Fetch resource metrics (CPU, memory utilization)
- **[03:57](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=237s)** - Step 3: Fetch HTTP metrics (error rates, failed requests, 400/500 errors)
- **[04:14](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=254s)** - Step 4: Return list of affected services that exceeded thresholds

### [Why Scheduled Polling Over Alert-Based Systems](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=261s)
- **[04:21](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=261s)** - Why not webhooks/alerts? Better to analyze a slice of time
- **[04:39](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=279s)** - Alert-based systems can be noisy with spiky workloads
- **[04:47](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=287s)** - Example: 80% CPU spike might be normal, not worthy of investigation
- **[04:57](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=297s)** - Need bigger picture context to determine if there's a real issue

### [Contextual Analysis and Root Cause Investigation](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=306s)
- **[05:09](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=309s)** - Pull additional context for suspected services
- **[05:24](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=324s)** - High resource utilization might just mean success/high usage
- **[05:33](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=333s)** - Check logs to confirm if errors exist or everything is fine
- **[05:44](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=344s)** - Advanced: Scan codebase to infer upstream providers (e.g., payment processors)
- **[05:53](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=353s)** - Automatically check status pages of dependencies
- **[06:02](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=362s)** - Agent can advise to "wait out" issues caused by third-party outages

### [Creating a Detailed Fix Plan](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=367s)
- **[06:07](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=367s)** - Combine all gathered information into a detailed plan
- **[06:12](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=372s)** - Example insights: High 500 requests + high memory usage + specific endpoint errors
- **[06:31](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=391s)** - Generate plan with architecture, affected services, and context
- **[06:40](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=400s)** - Agent process: Clone repo, create todo list, implement fixes, open PR
- **[06:55](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=415s)** - Complete flow: Issue detected → Pull request opened

### [Durable Execution with Inngest](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=420s)
- **[07:05](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=425s)** - Using durable workflows for reliable execution
- **[07:11](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=431s)** - Favorite abstraction: Simplifies complex logic while improving reliability
- **[07:19](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=439s)** - Example workflow: Process video upload (transcript → summary → database)
- **[07:30](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=450s)** - Workflow listens on "video uploaded" event
- **[07:55](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=475s)** - All steps prone to failure but automatically retried
- **[08:05](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=485s)** - Automatic retry with no extra code needed
- **[08:12](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=492s)** - Configurable: Exponential backoff, custom retry schedules, failure handlers
- **[08:25](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=505s)** - Each successful step is cached
- **[08:36](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=516s)** - Resume from failure point without repeating work
- **[08:45](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=525s)** - Benefits: Faster execution and more cost-effective

### [OpenCode: The Coding Agent](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=552s)
- **[09:12](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=552s)** - OpenCode: AI agent built for the terminal
- **[09:18](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=558s)** - Alternative to Claude Code, but fully open source
- **[09:22](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=562s)** - Choose any LLM provider or model
- **[09:35](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=575s)** - Architecture: Runs as both terminal UI and server
- **[09:40](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=580s)** - Server implementation exposes API for headless operation
- **[09:54](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=594s)** - Command "opencode" starts terminal UI + server
- **[10:05](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=605s)** - Can bring your own client to talk to the server
- **[10:12](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=612s)** - Deploy OpenCode server on Railway with all necessary tools
- **[10:22](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=622s)** - Install tools: Git, GitHub CLI, configure everything
- **[10:27](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=627s)** - Agent can open pull requests and navigate file systems

### [Implementation Details](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=638s)
- **[10:40](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=640s)** - Project: "railway-autofix" with two directories (API + OpenCode)
- **[10:51](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=651s)** - OpenCode: Single server using Bun runtime
- **[10:57](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=657s)** - Calls `createOpenCodeServer()` function
- **[11:06](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=666s)** - Runs on port 40496
- **[11:13](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=673s)** - Dockerfile defines the environment
- **[11:18](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=678s)** - Installs curl, jq, bash, Git, GitHub CLI
- **[11:30](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=690s)** - Configures Git and authenticates GitHub CLI
- **[11:41](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=701s)** - Code repo will be linked in description

### [Live Demo Walkthrough](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=709s)
- **[11:55](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=715s)** - API running on localhost:3000 with Inngest UI
- **[12:03](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=723s)** - Inngest UI useful for debugging workflows
- **[12:09](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=729s)** - Each function is a workflow with multiple steps
- **[12:20](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=740s)** - Production: "Monitor project health" runs on schedule
- **[12:26](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=746s)** - If issue detected → Pull service context → Generate fix
- **[12:40](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=760s)** - Demo run: Monitor health → Pull context → Generate fix
- **[12:55](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=775s)** - Railway-specific environment variables automatically available

### [Workflow Execution Details](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=781s)
- **[13:06](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=786s)** - First step: Get project architecture
- **[13:14](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=794s)** - Returns all databases, services, configuration details
- **[13:26](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=806s)** - Shows repo locations for each service
- **[13:30](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=810s)** - High-level overview of application infrastructure
- **[13:38](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=818s)** - Steps running in parallel for efficiency
- **[13:44](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=824s)** - Database resources: Max CPU (0.9), memory stats
- **[13:54](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=834s)** - Formatted summary for coding agent
- **[14:05](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=845s)** - Memory usage: 31.96 GB out of 32 GB max (very high)
- **[14:24](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=864s)** - Pull HTTP metrics for each service
- **[14:37](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=877s)** - Error rate percentages, latency, status counts
- **[14:50](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=890s)** - Request error rates and latency summaries

### [Service Context and Log Analysis](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=905s)
- **[15:08](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=908s)** - Pull service context function gathers comprehensive info
- **[15:19](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=919s)** - Fetch HTTP logs, build logs, deployment logs for affected services
- **[15:27](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=927s)** - Function payload shows passed information
- **[15:36](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=936s)** - Architecture summary: Nicely formatted markdown
- **[15:42](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=942s)** - Lists services in production environment, databases, volumes

### [AI Analysis and Fix Generation](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=962s)
- **[16:07](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=967s)** - Generate fix workflow called with all context
- **[16:16](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=976s)** - Analyze with AI: Pass project architecture and performance data to LLM
- **[16:28](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=988s)** - LLM receives: Architecture, data, performance metrics
- **[16:38](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=998s)** - Output: Detailed plan with debugging steps
- **[16:42](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=1002s)** - Example: "Reproduce locally with same load"
- **[16:50](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=1010s)** - Agent detects errors and attempts fixes
- **[16:55](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=1015s)** - Recommendations included in plan
- **[17:02](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=1022s)** - Create session: Each session is its own chat
- **[17:09](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=1029s)** - Multiple repos = multiple sessions
- **[17:17](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=1037s)** - Expected outcome: Pull request opened

### [Results and Conclusion](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=1047s)
- **[17:27](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=1047s)** - Success! Pull request opened automatically
- **[17:32](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=1052s)** - PR contains all changes from the agent
- **[17:37](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=1057s)** - PR description: Summary of changes, analysis, root causes, fixes
- **[17:43](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=1063s)** - Engineer reviews and merges if everything looks good
- **[17:49](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=1069s)** - Closing remarks and contact info
- **[17:54](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=1074s)** - Reach out on X/Twitter for questions
- **[17:59](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=1079s)** - Repo link available in description
- **[18:05](https://www.youtube.com/watch?v=Q5IVm_CxN2w&t=1085s)** - Thank you and see you next time

---

## Key Takeaways

1. **Self-Healing Infrastructure**: Coding agents can monitor production systems and autonomously generate fixes, shifting the developer workflow from "debug and fix" to "review and merge"

2. **Durable Workflows**: Using tools like Inngest provides automatic retries, caching, and resilience for complex multi-step processes without manual error handling

3. **OpenCode Architecture**: The server-client separation allows headless deployment of coding agents in production environments with full tool access (Git, GitHub CLI, etc.)

4. **Context is King**: The system gathers comprehensive context (metrics, logs, architecture) before generating fixes, enabling more accurate root cause analysis

5. **Time-Slice Analysis**: Scheduled monitoring with time-window analysis is more effective than alert-based systems for reducing noise and false positives

6. **Production-Ready Pattern**: The combination of metrics monitoring, durable workflows, and autonomous coding agents represents a viable path toward self-healing production systems
