import os
import sys
MAX_LINES = 100
for root, dirs, files in os.walk("."):
for file in files:
if file.endswith(".py"):
path = os.path.join(root, file)
        with open(path, "r", encoding="utf-8") as f:
            count = len(f.readlines())
        if count > MAX_LINES:
            print(f"ERROR: {path} has {count} lines (limit = 100)")
            sys.exit(1)
print("Line count check passed.")
