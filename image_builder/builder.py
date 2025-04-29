import subprocess

def build_image(dockerfile_path, image_tag, context_path="."):
    # Ensure paths with spaces are correctly handled by enclosing them in quotes
    cmd = [
        "docker", "build",
        "-t", image_tag,
        "-f", dockerfile_path,
        context_path
    ]
    # Execute the command
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    # Example: Adjust the paths according to your folder structure
    build_image(
        dockerfile_path='"Oppari (oamk)/AI_testing/dockerfiles/Dockerfile.frontend"',  # Use quotes for paths with spaces
        image_tag="studyplatform-frontend:latest",
        context_path="."  # You can also set this to another folder if required
    )
    
    build_image(
        dockerfile_path='"Oppari (oamk)/AI_testing/dockerfiles/Dockerfile.backend"',
        image_tag="studyplatform-backend:latest",
        context_path="."
    )
