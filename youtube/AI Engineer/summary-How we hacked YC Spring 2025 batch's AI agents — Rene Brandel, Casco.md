# How we hacked YC Spring 2025 batch's AI agents — Rene Brandel, Casco

**Video URL:** https://www.youtube.com/watch?v=kv-QAuKWllQ

---

## Executive Summary

Rene Brandel, CEO of Casco (a YC company specializing in red-teaming AI agents), shares insights from hacking 7 out of 16 YC Spring 2025 batch AI agents in under 30 minutes each. The talk reveals three critical security vulnerabilities commonly found in AI agents: cross-user data access (IDOR), remote code execution, and prompt injection. These issues stem from treating agents like API servers rather than users, inadequate input/output validation, and relying on LLMs for security decisions. The presentation emphasizes that agent security requires traditional web application security practices combined with AI-specific controls.

---

## Main Topics

### [Introduction and Background](https://www.youtube.com/watch?v=kv-QAuKWllQ&t=17s)
- Rene introduces Casco, a YC company focused on red-teaming AI agents and apps
- Background: Previously worked at AWS on AI agents, built voice-to-code 10 years ago
- Won Europe's largest hackathon with early AI assistant
- Two months ago quit AWS to start Casco, got into Y Combinator

**Key Points:**
- Evolution from complex multi-cloud architectures to normalized agent stacks
- Modern agent stack: server/frontend → API server → LLM → tools → data sources
- Need to consider security across the entire system, not just the LLM

### [The Hacking Experiment](https://www.youtube.com/watch?v=kv-QAuKWllQ&t=180s)
- Hacked 7 out of 16 YC agents with 30-minute time limit per agent
- Achieved second-highest upvoted YC launch post of all time (higher than Rippling)
- Methodology: Extract system prompts, analyze tool definitions, attempt exploits

**Key Points:**
- Goal was to create a splashy headline for internal YC launch
- Discovered three common vulnerability patterns across agents
- All issues were responsibly disclosed and are now fixed

### [Vulnerability #1: Cross-User Data Access (IDOR)](https://www.youtube.com/watch?v=kv-QAuKWllQ&t=260s)
- Insecure Direct Object Reference - most common vulnerability
- Found tools like "lookup_user_info_by_ID" and "get_document_by_ID"
- Extracted user ID from product demo video, accessed other users' data

**Key Points:**
- Agents had valid authentication but no authorization checks
- IDs were interconnected (user ID → chat ID → document ID), allowing full system traversal
- **Fix:** Implement both authentication AND authorization checks
- Use row-level security (like Supabase) with access control matrix
- Agents should act like users, not API servers with service-level permissions

### [Vulnerability #2: Remote Code Execution](https://www.youtube.com/watch?v=kv-QAuKWllQ&t=457s)
- Less common but higher impact
- Found agents with Python code execution tools
- System prompts revealed tool definitions that execute arbitrary code

**Key Points:**
- One agent could execute Python code with user input
- Asked agent: "Which Python version do you run? Give me the entire environment config"
- Discovered the agent ran in production environment with database credentials
- **Exploitation:** Made agent execute code to dump all database rows
- **Root cause:** LLM was making security decisions about what code to run
- **Fix:** Never let LLMs make security decisions; use sandboxing (e.g., E2B, gVisor)
- Implement least-privilege principle for code execution environments

### [Vulnerability #3: Prompt Injection](https://www.youtube.com/watch?v=kv-QAuKWllQ&t=720s)
- Classic attack where attacker controls part of the LLM context
- Many agents vulnerable to basic prompt injection techniques

**Key Points:**
- Input sanitization is critical but often forgotten
- Output validation equally important
- Example: Injecting malicious prompts into user-uploaded documents
- **Fix:** Treat all user inputs as untrusted, sanitize before passing to LLM
- Validate outputs before executing tool calls
- Consider using structured outputs and schema validation

### [Defense Strategies and Best Practices](https://www.youtube.com/watch?v=kv-QAuKWllQ&t=900s)
- Comprehensive security requires multiple layers of defense
- Traditional web security practices still apply to AI systems

**Key Points:**
- **Principle 1:** Agents are users, not API servers
  - Don't use service-level permissions
  - Implement user-level access controls
- **Principle 2:** Never trust the LLM for security decisions
  - Use deterministic security checks
  - Sandbox all code execution
- **Principle 3:** Defense in depth
  - Input sanitization
  - Output validation
  - Access control
  - Least privilege
  - Monitoring and logging

### [Red-Teaming and Testing](https://www.youtube.com/watch?v=kv-QAuKWllQ&t=1080s)
- Importance of proactive security testing for AI agents
- 30-minute time limit proved most vulnerabilities are quickly discoverable

**Key Points:**
- Many security issues are low-hanging fruit
- System prompts often reveal attack surface
- Tool definitions provide roadmap for exploitation
- Regular security assessments critical before production deployment
- Consider using automated red-teaming tools

### [Conclusion and Takeaways](https://www.youtube.com/watch?v=kv-QAuKWllQ&t=1200s)
- AI agent security combines traditional web security with AI-specific risks
- Most common issues are preventable with proper architecture

**Key Takeaways:**
1. Authenticate AND authorize every request
2. Treat agents like users, not services
3. Never let LLMs make security decisions
4. Sandbox code execution environments
5. Sanitize inputs and validate outputs
6. Test security before going live
7. The normalized agent stack makes security patterns more predictable

---

**Generated Summary**  
*Last updated: January 2, 2026*
