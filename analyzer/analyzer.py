import json
import os

def analyze_project(path="."):
    """
    Analyze the given project directory to detect tech stack.
    """
    package_json_path = os.path.join(path, "package.json")

    if not os.path.exists(package_json_path):
        print("package.json not found. Not a Node.js project.")
        return "Unknown"

    with open(package_json_path, "r") as f:
        package_json = json.load(f)

    dependencies = package_json.get("dependencies", {})
    dev_dependencies = package_json.get("devDependencies", {})

    is_react = "react" in dependencies or "react" in dev_dependencies
    is_vite = "vite" in dev_dependencies
    is_express = "express" in dependencies

    if is_react and is_vite and is_express:
        return "MERN-VITE"
    elif is_react and is_vite:
        return "React-VITE-Frontend"
    elif is_express:
        return "Express-Backend"
    else:
        return "Unknown"