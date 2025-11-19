# Telegram Bot Basic Workflow

This example demonstrates fundamental Telegram bot operations using the `python-telegram-bot` library (v21+).

## Prerequisites

1. Create a Telegram bot via [@BotFather](https://t.me/botfather)
2. Get your bot token
3. Set environment variable:
   ```bash
   export TELEGRAM_BOT_TOKEN="your-token-here"
   ```

## Running the Bot

```bash
uv run python main_telegram_bot.py
```

## Key Source Code

### Inline Script Metadata (Lines 1-6)

```python
1  # /// script
2  # requires-python = ">=3.9"
3  # dependencies = [
4  #     "python-telegram-bot>=21.0",
5  # ]
6  # ///
```

**Annotation**: Uses PEP 723 inline script metadata to specify dependencies. The `python-telegram-bot` library v21+ uses async/await patterns exclusively.

---

### Imports and Logger Setup (Lines 21-35)

```python
21  import logging
22  import os
23  from telegram import Update
24  from telegram.ext import (
25      Application,
26      CommandHandler,
27      MessageHandler,
28      ContextTypes,
29      filters,
30  )
31
32  # Configure logging to see bot activity
33  logging.basicConfig(
34      format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
35      level=logging.INFO,
36  )
37  logger = logging.getLogger(__name__)
```

**Annotation**:
- `Update` (line 23): Contains all incoming update data from Telegram
- `Application` (line 25): Main entry point for the bot (replaces older `Updater`)
- `CommandHandler` (line 26): Handles `/command` messages
- `MessageHandler` (line 27): Handles regular text messages
- `filters` (line 29): Filter messages by type (text, photo, etc.)

---

### Command Handler - /start (Lines 40-52)

```python
40  async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
41      """Handle /start command - Welcome new users."""
42      user = update.effective_user
43      welcome_message = (
44          f"Hello {user.first_name}! I'm a demo bot.\n\n"
45          "Available commands:\n"
46          "/start - Show this welcome message\n"
47          "/help - Get help information\n"
48          "/echo <text> - Echo back your message\n"
49          "/format - Show formatting examples\n\n"
50          "Or just send me any message and I'll echo it back!"
51      )
52      await update.message.reply_text(welcome_message)
53      logger.info(f"User {user.id} ({user.username}) started the bot")
```

**Annotation**:
- Line 40: All handlers must be `async` functions in v21+
- Line 42: `update.effective_user` provides user info (id, username, first_name)
- Line 52: `reply_text()` sends a plain text response to the user

---

### HTML Formatted Response - /help (Lines 56-69)

```python
56  async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
57      """Handle /help command - Provide usage instructions."""
58      help_text = (
59          "<b>Bot Help</b>\n\n"
60          "This bot demonstrates basic Telegram bot functionality:\n\n"
61          "<code>/start</code> - Initialize bot interaction\n"
62          "<code>/help</code> - Display this help message\n"
63          "<code>/echo text</code> - Echo your text back\n"
64          "<code>/format</code> - Show text formatting options\n\n"
65          "<i>Send any text message to receive an echo response.</i>"
66      )
67      await update.message.reply_html(help_text)
68      logger.info(f"Help requested by user {update.effective_user.id}")
```

**Annotation**:
- Lines 59-65: Uses HTML tags for formatting (`<b>`, `<i>`, `<code>`)
- Line 67: `reply_html()` parses HTML formatting in the message

---

### Command with Arguments - /echo (Lines 72-83)

```python
72  async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
73      """Handle /echo command - Echo back the provided text."""
74      if context.args:
75          text_to_echo = " ".join(context.args)
76          response = f"You said: {text_to_echo}"
77          await update.message.reply_text(response)
78          logger.info(f"Echo command: '{text_to_echo}'")
79      else:
80          await update.message.reply_text(
81              "Please provide text to echo.\nUsage: /echo <your message>"
82          )
```

**Annotation**:
- Line 74: `context.args` contains list of arguments after the command
- Line 75: Join arguments into a single string
- Lines 79-82: Handle case when no arguments provided

---

### Message Handler (Lines 107-120)

```python
107  async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
108      """Handle regular text messages - Echo them back."""
109      user = update.effective_user
110      message_text = update.message.text
111
112      # Log received message
113      logger.info(f"Received from {user.username} ({user.id}): {message_text}")
114
115      # Echo the message back with some formatting
116      response = f"You sent: {message_text}\n\nMessage length: {len(message_text)} characters"
117      await update.message.reply_text(response)
118
119      logger.info(f"Echoed message back to user {user.id}")
```

**Annotation**:
- Line 110: `update.message.text` contains the raw text content
- Line 116: Creates a response with message stats
- This handler processes all non-command text messages

---

### Bot Initialization and Registration (Lines 136-162)

```python
136  def main() -> None:
137      """Initialize and run the Telegram bot."""
138      # Get bot token from environment variable
139      token = os.environ.get("TELEGRAM_BOT_TOKEN")
140
141      if not token:
142          print("Error: TELEGRAM_BOT_TOKEN environment variable not set!")
...
152      print("Starting Telegram bot...")
153      print("Press Ctrl+C to stop the bot\n")
154
155      # Create the Application
156      application = Application.builder().token(token).build()
157
158      # Register command handlers
159      application.add_handler(CommandHandler("start", start_command))
160      application.add_handler(CommandHandler("help", help_command))
161      application.add_handler(CommandHandler("echo", echo_command))
162      application.add_handler(CommandHandler("format", format_command))
163
164      # Register message handler for non-command text messages
165      application.add_handler(
166          MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
167      )
168
169      # Register error handler
170      application.add_error_handler(error_handler)
171
172      # Start the bot
173      logger.info("Bot started successfully!")
174      application.run_polling(allowed_updates=Update.ALL_TYPES)
```

**Annotation**:
- Line 139: Secure token handling via environment variable
- Line 156: Builder pattern creates the Application instance
- Lines 159-162: Each `CommandHandler` maps a command string to a function
- Line 166: `filters.TEXT & ~filters.COMMAND` matches text that isn't a command
- Line 174: `run_polling()` starts the bot and listens for updates

---

## Expected Output

### Console Output (Bot Startup)

```
Starting Telegram bot...
Press Ctrl+C to stop the bot

2024-01-15 10:30:45,123 - __main__ - INFO - Bot started successfully!
```

### Console Output (User Interaction)

```
2024-01-15 10:31:02,456 - __main__ - INFO - User 123456789 (john_doe) started the bot
2024-01-15 10:31:15,789 - __main__ - INFO - Help requested by user 123456789
2024-01-15 10:31:30,012 - __main__ - INFO - Echo command: 'Hello World'
2024-01-15 10:31:45,345 - __main__ - INFO - Received from john_doe (123456789): Testing the bot
2024-01-15 10:31:45,456 - __main__ - INFO - Echoed message back to user 123456789
```

### Telegram Chat Output

**User sends**: `/start`

**Bot responds**:
```
Hello John! I'm a demo bot.

Available commands:
/start - Show this welcome message
/help - Get help information
/echo <text> - Echo back your message
/format - Show formatting examples

Or just send me any message and I'll echo it back!
```

---

**User sends**: `/echo Hello World`

**Bot responds**:
```
You said: Hello World
```

---

**User sends**: `Testing the bot`

**Bot responds**:
```
You sent: Testing the bot

Message length: 15 characters
```

---

**User sends**: `/help`

**Bot responds** (with HTML formatting):
```
Bot Help

This bot demonstrates basic Telegram bot functionality:

/start - Initialize bot interaction
/help - Display this help message
/echo text - Echo your text back
/format - Show text formatting options

Send any text message to receive an echo response.
```

---

## Error Output (No Token Set)

```
Error: TELEGRAM_BOT_TOKEN environment variable not set!
Please set it with: export TELEGRAM_BOT_TOKEN='your-token-here'

To get a token:
1. Open Telegram and search for @BotFather
2. Send /newbot and follow the instructions
3. Copy the token provided by BotFather
```

---

## Key Concepts

| Concept | Description | Code Reference |
|---------|-------------|----------------|
| Application | Main bot class (v21+ replaces Updater) | Line 156 |
| CommandHandler | Handles /commands | Lines 159-162 |
| MessageHandler | Handles regular messages | Lines 165-167 |
| filters | Filter messages by type | Line 166 |
| reply_text() | Send plain text response | Line 52 |
| reply_html() | Send HTML formatted response | Line 67 |
| context.args | Command arguments list | Line 74 |
| effective_user | User who sent the message | Line 42 |
| run_polling() | Start listening for updates | Line 174 |

## Version Requirements

- **Python**: >= 3.9
- **python-telegram-bot**: >= 21.0

The v21+ library uses async/await exclusively. Older synchronous patterns are not supported.

## Additional Resources

- [python-telegram-bot Documentation](https://docs.python-telegram-bot.org/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [BotFather - Create Your Bot](https://t.me/botfather)
