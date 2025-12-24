import json
import sys
from datetime import datetime

try:
    # Read JSON input from stdin
    input_data = json.loads(sys.stdin.read())

    # Extract session_id and prompt
    session_id = input_data.get('session_id', 'unknown')
    prompt = input_data.get('prompt', '')

    # Log with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("claude.log", "a") as f:
        f.write(f"[{timestamp}] Session: {session_id}\n")
        f.write(f"Input Data: {input_data}\n")
        f.write("-" * 80 + "\n")

    sys.exit(0)
except Exception:
    # If anything fails, just log timestamp as before
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("claude.log", "a") as f:
        f.write(f"{timestamp}\n")
    sys.exit(0)
