#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///

from datetime import datetime, timedelta
from pathlib import Path

# Get current time
current_time = datetime.now()

# Add 4 hours and 32 minutes for reset time
reset_time = current_time + timedelta(hours=4, minutes=32)

# Create ISO timestamp
iso_timestamp = reset_time.isoformat()

data = {
    'plan_usage_limit_session_pct': 26,
    'plan_usage_limit_reset_time': iso_timestamp
}

output_file = Path('tmp/claude_usage.yaml')
output_file.parent.mkdir(parents=True, exist_ok=True)

with open(output_file, 'w') as f:
    f.write(f"plan_usage_limit_session_pct: {data['plan_usage_limit_session_pct']}\n")
    f.write(f"plan_usage_limit_reset_time: {data['plan_usage_limit_reset_time']}\n")

print(f"Created {output_file}")
print(f"  Current time: {current_time}")
print(f"  Reset time: {reset_time}")
with open(output_file, 'r') as f:
    print(f"\nFile contents:\n{f.read()}")
