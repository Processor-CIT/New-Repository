import ast
import os
import sys
errors = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if ast.get_docstring(node) is None:
                        errors.append(
                            f"{path}: {node.name} missing docstring"
                        )
if errors:
    print("\n".join(errors))
    sys.exit(1)
print("All functions have docstrings")
