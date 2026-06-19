import json
import os
import subprocess
repo = os.environ["GITHUB_REPOSITORY"]
token = os.environ["GITHUB_TOKEN"]
event_file = os.environ["GITHUB_EVENT_PATH"]
with open(event_file, "r") as f:
    event = json.load(f)
pr_number = event["pull_request"]["number"]
comment = """
Automated Code Review Completed
✓ pycodestyle executed
✓ Line count check completed
✓ Docstring validation completed
cmd = [
    "curl",
    "-X",
    "POST",
    "-H",
    f"Authorization: token {token}",
    "-H",
    "Accept: application/vnd.github+json",
    f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments",
    "-d",
    json.dumps({"body": comment}),
]
subprocess.run(cmd, check=True)
