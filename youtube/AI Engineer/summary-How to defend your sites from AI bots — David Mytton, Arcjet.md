# How to defend your sites from AI bots — David Mytton, Arcjet

**Video URL:** https://www.youtube.com/watch?v=Gi4V8viBGYQ

---

## Executive Summary

David Mytton from Arcjet presents a comprehensive guide on defending websites from AI bots. With nearly 50% of web traffic now coming from automated clients (60% in gaming), AI crawlers are significantly increasing bandwidth costs and infrastructure load. The talk covers the spectrum of bots from good (search indexers) to bad (malicious scrapers), with AI crawlers occupying a nuanced middle ground. Mytton walks through practical defense mechanisms including robots.txt, user-agent verification, rate limiting, CAPTCHAs, and browser fingerprinting, while emphasizing the importance of understanding what traffic you want to allow versus block.

---

## Main Topics

### [**00:00**](https://www.youtube.com/watch?v=Gi4V8viBGYQ&t=0s) - Introduction and The Bot Problem
- David introduces Arcjet, a security SDK for developers
- Almost 50% of web traffic is automated clients (60% in gaming)
- Bot traffic has existed since the internet began, but AI is making it worse
- Expensive requests can lead to cost problems, especially on serverless platforms
- Bandwidth costs and denial of service attacks are major concerns

### [**02:25**](https://www.youtube.com/watch?v=Gi4V8viBGYQ&t=145s) - Is AI Making Things Worse?
- Real-world examples of AI crawler impact:
  - Diaspora: 24% of traffic from GPTBot (OpenAI's crawler)
  - Read the Docs: Reduced bandwidth from 800GB/day to 200GB/day by blocking AI crawlers
  - Wikipedia: 35% of traffic serving automated clients
- AI scrapers are not behaving nicely - making hundreds of thousands of requests without following rules

### [**03:50**](https://www.youtube.com/watch?v=Gi4V8viBGYQ&t=230s) - Good Bots vs Bad Bots vs AI Bots
- **Good bots**: Google bot - you get traffic in exchange for being indexed
- **Bad bots**: Obvious scrapers downloading images, content, files
- **AI crawlers**: The nuanced middle ground - sometimes good, sometimes bad
- OpenAI has at least 4 different bot types:
  1. **OpenAI Search Bot**: Like Google bot, indexes for ChatGPT search (you get citations and traffic)
  2. **ChatGPT User**: Real-time queries from users (not for training, may not cite)
  3. **GPTBot**: Original training crawler (no direct benefit, often no citation)
  4. **Computer Use/Operator**: Autonomous agents acting on behalf of users (challenging to detect)

### [**07:32**](https://www.youtube.com/watch?v=Gi4V8viBGYQ&t=452s) - Defense #1: Robots.txt
- Entirely voluntary - well-behaved bots will respect it
- Good for understanding your site structure and crawler policies
- Can specify different rules for different crawlers
- Major AI companies provide documentation on their bots
- **Problem**: Only works if bots choose to respect it

### [**09:31**](https://www.youtube.com/watch?v=Gi4V8viBGYQ&t=571s) - Defense #2: Verifying User Agents
- User-agent string identifies the bot
- Can verify legitimacy through DNS/IP verification:
  - Reverse DNS lookup on IP address
  - Check domain matches expected domain
  - Forward DNS lookup to verify
- **Problem**: User agents can be spoofed, so verification is essential

### [**11:14**](https://www.youtube.com/watch?v=Gi4V8viBGYQ&t=674s) - Defense #3: Rate Limiting
- Basic defense to limit request frequency
- Simple to implement but can interfere with legitimate usage
- Distributed systems make IP-based rate limiting less effective
- Need to think about rate limiting at different levels (IP, user, API key)
- **Challenge**: Finding the right balance between security and user experience

### [**12:45**](https://www.youtube.com/watch?v=Gi4V8viBGYQ&t=765s) - Defense #4: CAPTCHAs and Challenges
- Most people dislike CAPTCHAs (bad user experience)
- Modern alternatives: passive challenges that don't require user interaction
- Cloudflare's approach: invisible verification using browser signals
- **Trade-off**: Security vs user experience

### [**14:30**](https://www.youtube.com/watch?v=Gi4V8viBGYQ&t=870s) - Defense #5: Browser Fingerprinting and Bot Detection
- Advanced technique: analyzing browser behavior and characteristics
- Signals include: TLS fingerprint, HTTP headers, JavaScript execution, mouse movements
- Can detect headless browsers and automation frameworks
- **Sophisticated approach**: Combine multiple signals to score bot likelihood
- **Problem**: Arms race - bots are getting better at mimicking real browsers

### [**16:45**](https://www.youtube.com/watch?v=Gi4V8viBGYQ&t=1005s) - Defense #6: Business Logic and Patterns
- Look at actual behavior patterns, not just technical signals
- Examples:
  - Account creation patterns
  - Transaction velocity
  - Unusual access patterns to specific endpoints
- Combine with other defenses for layered security
- **Important**: Understand your application's normal behavior patterns

### [**18:20**](https://www.youtube.com/watch?v=Gi4V8viBGYQ&t=1100s) - Best Practices and Recommendations
- Start with robots.txt as a baseline (easy wins with well-behaved bots)
- Implement user-agent verification for known bots
- Add rate limiting as a fundamental defense layer
- Consider your use case - not all bot traffic is bad
- Think about what you want to allow vs block
- Layer multiple defenses for comprehensive protection
- Monitor and analyze your traffic to understand patterns
- Be prepared for the autonomous agent revolution

### [**20:15**](https://www.youtube.com/watch?v=Gi4V8viBGYQ&t=1215s) - Q&A Highlights
- Discussion on legal approaches vs technical approaches
- Robots.txt is a gentleman's agreement, not legally binding in most cases
- AI companies are starting to offer commercial APIs (e.g., Wikipedia negotiations)
- Balance between being open and protecting resources
- Future considerations: how to handle autonomous agents at scale

---

## Key Takeaways

1. **AI is significantly increasing bot traffic** - not just hypothetical, with concrete examples showing 20-35% of traffic from AI crawlers
2. **Not all bots are equal** - distinguish between indexing bots (potential traffic source), training bots (resource drain), and autonomous agents (complex)
3. **Layered defense is essential** - no single solution works; combine robots.txt, user-agent verification, rate limiting, and behavioral analysis
4. **User experience matters** - balance security with usability; passive challenges better than intrusive CAPTCHAs
5. **The landscape is evolving** - autonomous agents and computer-use bots are the next frontier, harder to detect than traditional crawlers
6. **Know what you want** - decide your policy on AI crawlers based on your business model and values
7. **Monitor and adapt** - continuously analyze traffic patterns and adjust defenses accordingly
