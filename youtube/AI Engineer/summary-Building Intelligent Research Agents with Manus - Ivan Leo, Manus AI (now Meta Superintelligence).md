# Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)

**Video URL:** https://www.youtube.com/watch?v=xz0-brt56L8

---

## Executive Summary

Ivan Leo from Manus AI presents a comprehensive workshop on building intelligent research agents using the Manus platform and its newly launched API. The session demonstrates how Manus goes beyond simple chatbots to become a general AI agent capable of executing tasks, automating workflows, and meeting users across multiple platforms (web, Slack, API, mobile, browser extensions). Through live demos and hands-on coding examples, Ivan shows how to build custom applications ranging from French language learning tools to event scrapers, while covering core API concepts like authentication, file handling, webhooks, and Slack integration.

---

## Main Topics

### [00:23 - 03:09] Introduction to Manus Platform and Capabilities
https://www.youtube.com/watch?v=xz0-brt56L8&t=23s

Ivan introduces Manus as an "action engine that goes beyond answers to execute tasks, automate workflows, and extend human reach." Key announcements include:
- **Manus 1.5 Flight**: Faster performance with increased quality and user satisfaction
- **Multiple access points**: Web app, Slack integration, API, browser operator, Microsoft 365 integration, and mobile app
- **Philosophy**: Building a general AI agent instead of verticalized products allows for much more flexibility

**Demo 1 - French Learning App**: Ivan demonstrates a custom French learning application he built with Manus that:
- Accepts daily journal entries in French
- Provides inline corrections with structured outputs
- Creates user profiles based on entries
- Uses text-to-speech (11 Labs integration) for pronunciation

### [06:00 - 09:00] Browser Operator and Remote Browser Control
https://www.youtube.com/watch?v=xz0-brt56L8&t=360s

**Demo 2 - Remote Browser Operator**:
- Manus can control a browser tab on your local computer
- Enables access to authenticated platforms (LinkedIn, Instagram, etc.) that sandboxed browsers can't reach
- Example shown: Finding nearby coffee shops on Google Maps
- Use case: Schedule tasks on a Mac Mini to automate daily workflows
- Critical for platforms requiring login credentials

**Demo 3 - AIE Event Scraper**:
- Built a brutalist-themed website to organize AI Engineer conference events
- Manus scraped all events from the conference website into JSON
- Created searchable interface with event details, descriptions, and Google Calendar integration
- Features event recommendations using Chroma vector database for similarity matching
- Demonstrates integration with external platforms (Chroma, OpenAI embeddings)

### [12:00 - 14:45] Manus API Overview and Philosophy
https://www.youtube.com/watch?v=xz0-brt56L8&t=720s

**Key API Principles**:
- **Unified billing**: API costs exactly the same as using the web chat interface
- **Platform agnostic**: Use Manus wherever you are (Slack, API, web, mobile)
- **General agent first**: Built as a general AI agent with web development capabilities second
- **Full Docker images**: Unlike other platforms, Manus ships full applications enabling complex integrations (webhooks, Redis, Stripe, etc.)

**Workshop Resources**:
- GitHub notebooks available at: `tinyurl.com/manis-api-workshop`
- Requires three environment variables: MANUS_API_KEY, SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET

### [14:45 - 19:18] API Fundamentals: Authentication and First Task
https://www.youtube.com/watch?v=xz0-brt56L8&t=885s

**Getting Started**:
1. Obtain Manus API key from account settings
2. Test connection using files API endpoint
3. Create first task with simple query

**Two Model Options**:
- **Manus 1.5**: For complex tasks like building websites (both demos used this)
- **Manus 1.5 Light**: For simpler, faster queries

**Key Features**:
- Unlimited context management with smart KV caching
- High cache hit rates for fast responses
- Automatic routing between simple chat and full agent based on query complexity

### [19:18 - 22:23] Task Lifecycle and Polling
https://www.youtube.com/watch?v=xz0-brt56L8&t=1158s

**Four Task States**:
1. **Running**: Task is actively being processed
2. **Pending**: Requires more input from user
3. **Completed**: Task finished successfully
4. **Error**: Something went wrong (rare)

**Polling Pattern**:
- Simple pattern for prototyping: check task status every 20 seconds
- Retrieve task details including credits used, responses, and message history
- Can push follow-up messages to the same task ID to maintain context
- Example shown: Weather lookup with follow-up question about planning activities

### [22:23 - 31:00] File Handling and Context Management
https://www.youtube.com/watch?v=xz0-brt56L8&t=1343s

**Three Ways to Provide Context**:

1. **Files API** (for large/sensitive files):
   - Upload files via S3 pre-signed URLs
   - Automatic deletion after 48 hours for security
   - Example: Rick and Morty character dataset (JSON) → generated interactive website with gender distribution, character status, visualizations

2. **Public URL Attachments**:
   - Direct links to publicly accessible files
   - Automatic file type detection (PDF, JSON, images)
   - Example: Warren Buffett investor letter analysis

3. **Base64 Encoded Images**:
   - Inline image attachments for screenshots, diagrams
   - Example: Bug investigation with 404 page screenshot → Manus analyzed the issue

**Supported File Types**:
- PDFs (auto-parsed)
- Images (multimodal content)
- JSON files
- All files processed with appropriate handlers out of the box

**Connector Integration**:
- Pre-configured connectors (Gmail, Notion, etc.) work via UID
- Copy connector UID from settings to enable in API calls

### [31:00 - 34:50] Webhooks for Production Scale
https://www.youtube.com/watch?v=xz0-brt56L8&t=1860s

**Why Webhooks**:
- Polling works for prototyping but not at scale
- Webhooks notify when tasks are created and completed
- More efficient for long-running tasks (typical: 3-5 minutes)
- Eliminates need for constant polling workers

**Implementation**:
- Register webhook endpoint with Manus API
- Receives notifications on task.created and task.stopped events
- Example deployment using Modal (serverless Python)
- Webhook appears in Manus settings under "Integrations built with Manus API"

**Best Practices**:
- Use webhooks for production applications
- Polling acceptable for testing and prototyping
- Reduces infrastructure costs significantly

### [34:50 - 01:16:23] Advanced Integration: Building a Slack Bot
https://www.youtube.com/watch?v=xz0-brt56L8&t=2090s

**Slackbot Implementation** (Notebook 5 - most complex demo):
- Reproduces the original Manus Slack integration
- Handles Slack events (app_mention, message events)
- Signature verification for security
- Thread support for organized conversations
- File attachment handling

**Architecture**:
1. User mentions bot in Slack
2. Slack sends event to webhook endpoint
3. Verify Slack signature
4. Create Manus task with user message
5. Poll or use webhooks for task completion
6. Post response back to Slack thread

**Key Considerations**:
- Slack requires quick response (3 seconds) to event webhook
- Use background processing for Manus tasks
- Thread support keeps conversations organized
- File attachments automatically forwarded to Manus

**Technical Details**:
- Uses Modal for deployment
- FastAPI for webhook endpoints
- Slack SDK for API interactions
- Environment variables for secure credential management

### [01:16:23 - 01:21:28] Q&A Session Highlights
https://www.youtube.com/watch?v=xz0-brt56L8&t=4583s

**Data Privacy & Security**:
- User chats are private and not read by Manus team
- Exception: When users report issues and share chats for debugging
- All data housed in the United States
- Files auto-deleted after 48 hours

**Interesting Use Cases**:
- **Pickleball court booking**: Python script with 6 Selenium instances scraping government website to find available slots in Singapore
- **Research and data analysis**: Most common API use case
- Demonstrates the power of general agent with its own sandbox

**Roadmap Features**:
- **My Browser API access**: Coming soon with improved permission system
- **Export formats**: Markdown to PDF, PPTX file exports (within 2 weeks)
- **Feature parity**: Ensuring API has same capabilities as UI
- **Memory system**: Cross-conversation context (actively being explored)

**Best Practices**:
- Try what the agent can do first, then build workflows around it
- Use appropriate model (1.5 vs 1.5 Light) based on complexity
- For complex multi-step operations, use general agent capabilities rather than hardcoded workflows

---

## Key Takeaways

1. **Platform Philosophy**: Manus differentiates by building a general AI agent first, then adding specialized capabilities, rather than creating verticalized products

2. **Developer Experience**: API billing matches web interface usage - no surprises or complicated pricing models

3. **Full Stack Capabilities**: Unlike other platforms, Manus provides full Docker images enabling complex integrations like webhooks, database connections, and payment processing

4. **Production Ready**: With webhooks, proper file handling, and robust error states, the API is designed for production deployments, not just prototypes

5. **Multi-Platform Strategy**: Meet users where they are - web, Slack, API, mobile, browser extensions, and Microsoft 365 integration

6. **Security First**: Automatic file deletion, private chats, US-based data hosting, and upcoming enhanced permission systems

7. **Rapid Development**: Examples shown were built in hours/days, not weeks - demonstrating the platform's ability to accelerate development

---

## Additional Resources

- **Workshop Notebooks**: tinyurl.com/manis-api-workshop
- **API Documentation**: api.mmanis.ai
- **Manus Platform**: open.mmanis.ai
- **Support**: Manus team available for integration assistance with various AI frameworks (AI SDK, Copilot, AG UI, etc.)
