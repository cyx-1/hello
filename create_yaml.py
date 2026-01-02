content = """plan_usage_limit_session_pct: 1
plan_usage_limit_reset_time: 2026-01-01T22:59:23.131952
"""
with open('./tmp/claude_usage.yaml', 'w') as f:
    f.write(content)
print("File created successfully")
with open('./tmp/claude_usage.yaml', 'r') as f:
    print(f.read())
