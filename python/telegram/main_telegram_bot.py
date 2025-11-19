# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "python-telegram-bot>=21.0",
# ]
# ///
"""
Telegram Bot Basic Workflow Example

This script demonstrates fundamental Telegram bot operations:
- Receiving and processing messages
- Sending text responses
- Handling commands (/start, /help, /echo)
- Using message formatting (HTML, Markdown)
- Error handling

To run this bot:
1. Create a bot via @BotFather on Telegram
2. Get your bot token
3. Set environment variable: export TELEGRAM_BOT_TOKEN="your-token-here"
4. Run: uv run python main_telegram_bot.py
"""

import logging
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Configure logging to see bot activity
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command - Welcome new users."""
    user = update.effective_user
    welcome_message = (
        f"Hello {user.first_name}! I'm a demo bot.\n\n"
        "Available commands:\n"
        "/start - Show this welcome message\n"
        "/help - Get help information\n"
        "/echo <text> - Echo back your message\n"
        "/format - Show formatting examples\n\n"
        "Or just send me any message and I'll echo it back!"
    )
    await update.message.reply_text(welcome_message)
    logger.info(f"User {user.id} ({user.username}) started the bot")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /help command - Provide usage instructions."""
    help_text = (
        "<b>Bot Help</b>\n\n"
        "This bot demonstrates basic Telegram bot functionality:\n\n"
        "<code>/start</code> - Initialize bot interaction\n"
        "<code>/help</code> - Display this help message\n"
        "<code>/echo text</code> - Echo your text back\n"
        "<code>/format</code> - Show text formatting options\n\n"
        "<i>Send any text message to receive an echo response.</i>"
    )
    await update.message.reply_html(help_text)
    logger.info(f"Help requested by user {update.effective_user.id}")


async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /echo command - Echo back the provided text."""
    if context.args:
        text_to_echo = " ".join(context.args)
        response = f"You said: {text_to_echo}"
        await update.message.reply_text(response)
        logger.info(f"Echo command: '{text_to_echo}'")
    else:
        await update.message.reply_text(
            "Please provide text to echo.\nUsage: /echo <your message>"
        )


async def format_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /format command - Demonstrate message formatting."""
    # HTML formatting example
    html_message = (
        "<b>Bold Text</b>\n"
        "<i>Italic Text</i>\n"
        "<u>Underlined Text</u>\n"
        "<s>Strikethrough</s>\n"
        "<code>Inline Code</code>\n"
        "<pre>Code Block</pre>\n"
        '<a href="https://telegram.org">Link Text</a>'
    )
    await update.message.reply_html(html_message)

    # Markdown V2 formatting example
    markdown_message = (
        "*Bold Text*\n"
        "_Italic Text_\n"
        "__Underline__\n"
        "~Strikethrough~\n"
        "`Inline Code`\n"
        "```\nCode Block\n```"
    )
    await update.message.reply_markdown_v2(markdown_message)
    logger.info(f"Format examples sent to user {update.effective_user.id}")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle regular text messages - Echo them back."""
    user = update.effective_user
    message_text = update.message.text

    # Log received message
    logger.info(f"Received from {user.username} ({user.id}): {message_text}")

    # Echo the message back with some formatting
    response = (
        f"You sent: {message_text}\n\nMessage length: {len(message_text)} characters"
    )
    await update.message.reply_text(response)

    logger.info(f"Echoed message back to user {user.id}")


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle errors that occur during bot operation."""
    logger.error(f"Exception while handling update: {context.error}")

    # Notify user if possible
    if isinstance(update, Update) and update.effective_message:
        error_message = "Sorry, an error occurred while processing your request."
        await update.effective_message.reply_text(error_message)


def main() -> None:
    """Initialize and run the Telegram bot."""
    # Get bot token from environment variable
    token = os.environ.get("TELEGRAM_BOT_TOKEN")

    if not token:
        print("Error: TELEGRAM_BOT_TOKEN environment variable not set!")
        print("Please set it with: export TELEGRAM_BOT_TOKEN='your-token-here'")
        print("\nTo get a token:")
        print("1. Open Telegram and search for @BotFather")
        print("2. Send /newbot and follow the instructions")
        print("3. Copy the token provided by BotFather")
        return

    print("Starting Telegram bot...")
    print("Press Ctrl+C to stop the bot\n")

    # Create the Application
    application = Application.builder().token(token).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("echo", echo_command))
    application.add_handler(CommandHandler("format", format_command))

    # Register message handler for non-command text messages
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    # Register error handler
    application.add_error_handler(error_handler)

    # Start the bot
    logger.info("Bot started successfully!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
