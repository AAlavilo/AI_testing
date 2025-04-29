from image_builder.builder import build_image

# Build Frontend
build_image(
    dockerfile_path="mainFolder/AI_testing/dockerfiles/Dockerfile.frontend",
    image_tag="studyplatform-frontend:latest",
    context_path="."
)

# Build Backend
build_image(
    dockerfile_path="mainFolder/AI_testing/dockerfiles/Dockerfile.backend",
    image_tag="studyplatform-backend:latest",
    context_path="."
)