# Government Agents: AI Agents Meet Tough Regulations — Mark Myshatyn, Los Alamos National Lab

**Video URL:** https://www.youtube.com/watch?v=TnSGx36Ly0Q

---

## Executive Summary

Mark Myshatyn, Enterprise AI Architect at Los Alamos National Laboratory, discusses how the lab is applying AI agents to nuclear science research while navigating strict government regulations. With nearly 70 years of machine learning experience, Los Alamos is using agentic AI to accelerate scientific discovery - from designing fusion capsules to managing their nuclear stockpile. The presentation covers their partnerships with frontier AI labs, their Venado supercomputer infrastructure, and the critical trust and security requirements for deploying AI in high-stakes government environments where data leaks could have geopolitical and kinetic consequences.

---

## Key Topics

### [00:14](https://www.youtube.com/watch?v=TnSGx36Ly0Q&t=14s) - Introduction: Los Alamos' 70-Year AI History
- Los Alamos has been doing applied AI/ML for almost 70 years
- Historical example: 1956 Los Alamos chess on MANIAC 1 supercomputer (played without bishops due to memory constraints)
- Early pioneers in Monte Carlo methods development
- AI agents represent a significant new opportunity for accelerating science

### [01:24](https://www.youtube.com/watch?v=TnSGx36Ly0Q&t=84s) - Agentic AI for Fusion Capsule Design
- Demonstration of AI agent designing an inertial confinement fusion (ICF) capsule for Lawrence Livermore Lab
- Agent reads scientific papers, identifies tangential research, and generates hypotheses
- Not just chatbot code generation - executes thermodynamic/hydrodynamic tests on high-performance computing (HPC) assets
- Leverages 50-60+ years of nuclear stockpile stewardship math and science
- Successfully designed and simulated an optimized fusion capsule

### [03:20](https://www.youtube.com/watch?v=TnSGx36Ly0Q&t=200s) - Los Alamos Scale and Mission
- 40 square miles of labs, test sites, and test plants
- 13 nuclear facilities
- 20,000+ researchers
- Three-pronged AI strategy:
  1. Push the science of AI forward (develop own models)
  2. Partner with commercial industry and academia
  3. Integrate AI into workflows (payroll, procurement, cybersecurity, etc.)

### [04:32](https://www.youtube.com/watch?v=TnSGx36Ly0Q&t=272s) - Strategic Partnerships
- Academic partnerships including UC family of schools
- Working with all frontier labs (OpenAI, Anthropic, etc.)
- Chemical and biological safety work with OpenAI
- "We're a safe place to do dangerous things" - decades of experience
- Frontier labs partner with Los Alamos for unique data and expertise

### [05:21](https://www.youtube.com/watch?v=TnSGx36Ly0Q&t=321s) - Venado Supercomputer Infrastructure
- 2,500+ nodes of NVIDIA GraceHopper super chips
- Partnership with NVIDIA and HPE
- Brought OpenAI models up to classified networks
- Enables AI research on classified national security problems

### [05:54](https://www.youtube.com/watch?v=TnSGx36Ly0Q&t=354s) - Government AI Regulations and Trust
- OMB Memorandum M25-21 and M25-22 (released April 2024)
- Codifies government AI system requirements
- Mandates government move faster with AI
- "We are not a t-shirt company" - data leaks have geopolitical/kinetic consequences
- 25-page comprehensive guidance on bringing AI into government missions

### [07:19](https://www.youtube.com/watch?v=TnSGx36Ly0Q&t=439s) - Data Classification and Responsibility
- Multiple classification levels: open/public, controlled, classified, restricted
- Physics of nuclear weapons "born classified" - never expires
- Trust requirements increase with classification level
- Partners must accept increased responsibility for securing sensitive data

### [08:04](https://www.youtube.com/watch?v=TnSGx36Ly0Q&t=484s) - Fedramp and Cloud Security Requirements
- Fedramp: Federal Risk and Authorization Management Program
- Three impact levels (low, moderate, high) based on data sensitivity
- 400+ controls for high-impact systems
- Takes 12-18+ months for authorization
- Massive complexity: one vendor had 76,000 pages of documentation
- Continuous monitoring and audit requirements

### [10:08](https://www.youtube.com/watch?v=TnSGx36Ly0Q&t=608s) - AI-Specific Government Requirements (M25-21)
- Requirements for safety-impacting and rights-impacting AI systems
- Defines "AI actors" including developers, deployers, owners
- Impact assessments required before deployment
- Performance testing and ongoing monitoring mandated
- Human review and decision-making oversight
- Opt-out provisions for individuals affected by AI decisions

### [11:42](https://www.youtube.com/watch?v=TnSGx36Ly0Q&t=702s) - Challenges for AI Startups Selling to Government
- Compliance burden disproportionately affects smaller companies
- Example: Audio transcription vendor couldn't meet security requirements
- Had to build internal solution or use less capable tools
- Large vendors (Microsoft, Google, AWS) already compliant, but may lack specialized AI capabilities
- Innovation vs. security compliance tradeoff

### [13:15](https://www.youtube.com/watch?v=TnSGx36Ly0Q&t=795s) - AI Agent Security Concerns
- Tool use authorization: What can agents access?
- Prompt injection and jailbreaking risks
- Model vulnerabilities and adversarial attacks
- Agent actions must be auditable and traceable
- Need to validate agent behavior before deployment
- Challenges unique to government: can't just "patch and iterate"

### [15:37](https://www.youtube.com/watch?v=TnSGx36Ly0Q&t=937s) - Balancing Innovation and Security
- Government needs cutting-edge AI capabilities
- Can't wait 18 months for Fedramp authorization
- Exploring alternative deployment models:
  - On-premise deployment of commercial models
  - Hybrid architectures
  - Sandboxed environments for testing
- Partnership models where vendors maintain compliance

### [16:49](https://www.youtube.com/watch?v=TnSGx36Ly0Q&t=1009s) - Recommendations for AI Companies
- Understand government customer requirements early
- Build security and compliance into product from start
- Consider government-specific deployment options
- Partner with system integrators already in government space
- Be transparent about model capabilities and limitations
- Document everything - auditability is critical

### [18:22](https://www.youtube.com/watch?v=TnSGx36Ly0Q&t=1102s) - Future Outlook
- Government AI adoption accelerating despite regulatory burden
- Los Alamos committed to both innovation and security
- Need for new partnership models between government and AI startups
- Opportunity for companies that can navigate compliance requirements
- AI will be critical for national security missions

### [19:15](https://www.youtube.com/watch?v=TnSGx36Ly0Q&t=1155s) - Q&A and Closing
- Audience questions about specific compliance scenarios
- Discussion of model deployment strategies
- Resources for learning more about government AI requirements
- Contact information for partnering with Los Alamos

---

## Key Takeaways

1. **High Stakes Environment**: Los Alamos operates where mistakes have geopolitical and kinetic consequences - data security is paramount
2. **Massive Compliance Burden**: Fedramp high authorization requires 400+ controls and 12-18 months, creating barriers for AI startups
3. **Government Moving Fast**: Despite regulations, new OMB memoranda (M25-21, M25-22) mandate rapid AI adoption across government
4. **Agent-Specific Risks**: AI agents introduce unique security challenges around tool use, prompt injection, and auditability
5. **Partnership Opportunities**: Government needs cutting-edge AI but startups must build compliance in from the start
6. **Infrastructure Investment**: Venado supercomputer shows government commitment to world-class AI research capabilities
7. **Mission-Critical AI**: Moving beyond productivity tools to core mission applications (fusion research, nuclear stockpile stewardship)
8. **Long AI History**: Nearly 70 years of ML experience positions Los Alamos uniquely to evaluate and deploy modern AI safely

---

**Last Updated:** January 1, 2026
