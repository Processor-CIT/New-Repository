import os
import sys
MAX_LINES = 100
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                lines = len(f.readlines())
            if lines > MAX_LINES:
                print(f"{path} exceeds 100 lines")
                sys.exit(1)
print("Line count check passed")
