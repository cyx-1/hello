# How to Secure Agents using OAuth — Jared Hanson (Keycard, Passport.js)

**Video URL:** https://www.youtube.com/watch?v=blmAkayzE8M

---

## Executive Summary

Jared Hanson, creator of Passport.js and co-founder of Keycard, discusses how to properly secure AI agents using OAuth. He explains the fundamental problems with current MCP (Model Context Protocol) server authorization approaches, traces the evolution of the MCP authorization specification from its initial flawed design to the current improved draft, and outlines the future security challenges for AI agents including agent-to-agent communication, identity management, attestation, transactional authorization, chain of custody, and async interactions. The talk emphasizes that while OAuth for MCP client-to-server connections is a good start, it's only scratching the surface of what's needed for fully secure AI interactions.

---

## Topics

### [Introduction and Background](https://www.youtube.com/watch?v=blmAkayzE8M&t=16s)
**[00:16 - 00:59]**

- Jared Hanson introduces himself as co-founder of Keycard and creator of Passport.js
- Previously worked at Auth0 and Okta on identity infrastructure
- Focus on securing agents using OAuth, described as one of the most important topics for AI

### [The Security Problem with Current Agent Approaches](https://www.youtube.com/watch?v=blmAkayzE8M&t=60s)
**[01:00 - 01:43]**

- More connected agents are more useful, but create security risks
- Current impossible choice: broad access with security risks vs. limited capabilities with reduced value
- MCP servers today use long-lived, broadly-scoped API keys in configuration files
- Scaling this pattern to hundreds/thousands of agents creates major security problems

### [OAuth Introduction and Fundamentals](https://www.youtube.com/watch?v=blmAkayzE8M&t=106s)
**[01:46 - 03:00]**

- OAuth is a relatively complicated protocol but has straightforward principles
- Protocol for applications (clients) to request access to APIs (resource servers)
- Requests mediated by authorization server
- Example: Calendly connecting to Google Calendar
- Key components: access tokens, refresh tokens, authorization code flows

### [OAuth vs OpenID Connect](https://www.youtube.com/watch?v=blmAkayzE8M&t=180s)
**[03:00 - 05:00]**

- OAuth is for authorization, but often used for authentication (sign-in with Google/Facebook)
- Special case: API replaced with user info API returning user claims
- OpenID Connect: formal identity layer on top of OAuth
- Introduces ID tokens (JWT) as cryptographically signed statements about user identity
- Different terminology: authorization servers become identity providers, applications become relying parties

### [OAuth's Three-Role Architecture](https://www.youtube.com/watch?v=blmAkayzE8M&t=300s)
**[05:00 - 06:18]**

- Three roles: client, resource server, authorization server
- Authorization server mediates access by issuing tokens
- Main benefit: APIs don't need to handle authentication (passwords, MFA, consent flows)
- Centralized policy enables ecosystems of apps and APIs
- All protected by a central authorization location

### [Applying OAuth to MCP and Agents](https://www.youtube.com/watch?v=blmAkayzE8M&t=378s)
**[06:18 - 06:59]**

- Applications replaced by chatbots/agents like Claude
- MCP clients and servers should be authorized via OAuth
- Should be simple, but "nothing with OAuth is ever so simple"

### [MCP Authorization: Version 1 (No OAuth)](https://www.youtube.com/watch?v=blmAkayzE8M&t=419s)
**[06:59 - 07:29]**

- First version (7 months old) had no authorization at all
- Primarily designed for local MCP servers
- Some notion of remote servers but no authorization
- Spurred community discussion on adding authorization

### [MCP Authorization: First Attempt at OAuth](https://www.youtube.com/watch?v=blmAkayzE8M&t=449s)
**[07:29 - 09:00]**

- Latest draft published in late March 2025
- Major flaw: MCP servers had to implement both resource server AND authorization server
- Collapsed OAuth authorization server into MCP server
- Missing the crucial third role in OAuth's three-role architecture
- Not recommended to read current authorization spec - gives misinformed view of OAuth

### [Community Backlash and Corrections](https://www.youtube.com/watch?v=blmAkayzE8M&t=505s)
**[08:25 - 09:56]**

- 5 days after spec release, Christian Posta's viral blog post: "MCP authorization spec is a mess for the enterprise"
- Aaron Parecki followed up with "Let's fix OAuth and MCP"
- Problem: treating MCP server as both resource server and authorization server
- PR with 400+ comments proposed fixing the architecture
- Jared had recommended proper OAuth modeling back in January

### [MCP Authorization: Fixed Version (Draft)](https://www.youtube.com/watch?v=blmAkayzE8M&t=600s)
**[10:00 - 10:42]**

- Current draft models OAuth cleanly and correctly
- OAuth authorization server is separate entity
- Major benefit for MCP server builders: only need to verify tokens
- All other responsibilities handed off to OAuth server
- Back to a good place for authorizing MCP client-to-server connections

### [Future Challenge 1: Agent-to-Agent Communication](https://www.youtube.com/watch?v=blmAkayzE8M&t=642s)
**[10:42 - 11:24]**

- Current focus: authorization code flow for end-user delegation
- Need: client credentials flow for agents acting on their own behalf
- Agents communicating with other agents or MCP servers without user involvement

### [Future Challenge 2: Agent Identity](https://www.youtube.com/watch?v=blmAkayzE8M&t=686s)
**[11:26 - 12:46]**

- Traditional OAuth: manual registration via developer portal, client ID/secret
- Too much friction for MCP's standard protocol approach
- Dynamic client registration: applications request credentials at runtime
- Problem: 10 years old, no meaningful adoption, makes agents anonymous
- Hard to build trust with uncredentialed registration requests

### [Future Challenge 3: Public Clients and Push Registration](https://www.youtube.com/watch?v=blmAkayzE8M&t=766s)
**[12:46 - 13:23]**

- For public clients: use "push client registration" specification
- Well-known string to identify public clients
- Skips registration process and state storage
- Simpler approach that can carry client metadata in requests

### [Future Challenge 4: Authenticated Agent Identity with URLs and PKI](https://www.youtube.com/watch?v=blmAkayzE8M&t=803s)
**[13:23 - 14:09]**

- Proposal: use URLs and PKI for agent identity
- Reuse existing identifiers people associate with apps
- Example: agent.com as client identity in OAuth flows
- Authenticate via cryptographic signatures using JWT assertions or HTTP message signatures
- Verify with corresponding public keys

### [Future Challenge 5: Agent Attestation](https://www.youtube.com/watch?v=blmAkayzE8M&t=849s)
**[14:09 - 14:59]**

- Agents connected to resources also send data to LLMs
- Need awareness and control over where data goes
- Limited technique: treat LLM as another API (works in protected environments)
- For edge-deployed agents (desktop/mobile): need remote attestation
- IETF work on remote attestation and supply chain security
- Attest to device state, software running, which LLM receives data
- Incorporate into OAuth authorization flows

### [Future Challenge 6: Transactional Authorization](https://www.youtube.com/watch?v=blmAkayzE8M&t=899s)
**[14:59 - 16:02]**

- Current OAuth: scopes provide better permissions than passwords (read vs. write)
- Problem: too coarse-grained and long-lived for many use cases
- Need increasingly transactional authorization for agents
- Examples: financial transactions, commercial transactions
- Authorize on transaction basis with specific amounts or budgets
- Solution: "Rich Authorization Requests" specification for more dynamic access

### [Future Challenge 7: Chain of Custody](https://www.youtube.com/watch?v=blmAkayzE8M&t=962s)
**[16:02 - 16:58]**

- MCP covers first leg: authorized agent-to-MCP-server connections
- Second leg unspecified: MCP server to internal APIs
- Technique: OAuth token exchange for same-domain API calls
- Special case: MCP servers to third-party APIs
- Solution: identity chaining across domains via identity assertion grant
- Need end-to-end visibility for authorization flows along agent graphs

### [Future Challenge 8: Async Interactions](https://www.youtube.com/watch?v=blmAkayzE8M&t=1033s)
**[17:13 - 17:39]**

- OAuth typically assumes user sitting in front of browser
- Agents work in background while users walk away
- Need agents to reach back to users for additional permissions
- Move beyond browser-based flows to real-time channels (SMS, push notifications)

### [Future Challenge 9: Voice, Video, and Background Interactions](https://www.youtube.com/watch?v=blmAkayzE8M&t=1059s)
**[17:39 - 18:08]**

- AI interacting via voice, video, or completely in background
- How to think about security in these contexts?
- Frontier of security and interaction
- Prior art in real-time communities: SIP, XMPP, WebRTC

### [Conclusion and Keycard Introduction](https://www.youtube.com/watch?v=blmAkayzE8M&t=1091s)
**[18:08 - 18:51]**

- All these challenges are important for safe and secure AI future
- Keycard: identity and access management platform for AI
- Connects co-pilots, custom agents, and third-party agents to apps/services/infrastructure
- Uses standards-compliant protocols: OIDC, MCP, OAuth
- Hiring and looking for partners to secure agents
- Website: keycard.ai

---

## Key Takeaways

1. **MCP Authorization Evolution**: The MCP specification went through a flawed first attempt that collapsed OAuth's authorization server into MCP servers, but has been fixed in the current draft to properly separate concerns.

2. **Three-Role Architecture is Critical**: OAuth's three roles (client, resource server, authorization server) must be properly separated. MCP servers should only be resource servers that verify tokens, not handle authentication.

3. **Beyond Basic OAuth**: Securing MCP client-to-server connections is just the beginning. The future requires solutions for:
   - Agent-to-agent communication (client credentials flow)
   - Agent identity (URLs + PKI instead of manual registration)
   - Agent attestation (knowing which LLM receives data)
   - Transactional authorization (fine-grained, short-lived permissions)
   - Chain of custody (token exchange, identity chaining)
   - Async and real-time interactions (SMS, push, voice, video)

4. **Standards Over Custom Solutions**: Use existing and emerging OAuth/OIDC specifications rather than reinventing security mechanisms:
   - Push client registration for public clients
   - Rich Authorization Requests for transactional access
   - Token exchange for chain of custody
   - Identity assertion grants for cross-domain authorization

5. **Current Approach is Insecure**: Using long-lived, broadly-scoped API keys in configuration files doesn't scale and creates major security vulnerabilities when deploying hundreds or thousands of agents.

---

**Last Updated:** 2026-01-02
