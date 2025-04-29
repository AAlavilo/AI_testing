import os

def generate_dockerfiles(output_dir="."):
    """
    Generate optimized Dockerfiles for frontend and backend.
    """

    # Frontend Dockerfile (Vite + React → build → Nginx)
    frontend_dockerfile = '''# Frontend Dockerfile (Vite + React)
FROM node:20.9.0 AS builder
WORKDIR /app
ENV HOME=/app
ENV NPM_CONFIG_CACHE=/app/.npm

COPY Oppimisalusta/studyPlatform/package*.json ./
RUN npm install --unsafe-perm
RUN npm install react-player --unsafe-perm
COPY Oppimisalusta/studyPlatform/ ./
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html

RUN chgrp -R 0 /usr/share/nginx/html && chmod -R g+rwX /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
'''

    # Backend Dockerfile (Express.js backend)
    backend_dockerfile = '''# Backend Dockerfile (Node.js API)
FROM node:20.9.0
WORKDIR /app
ENV HOME=/app
ENV NPM_CONFIG_CACHE=/app/.npm

COPY Oppimisalusta/studyPlatform/package*.json ./
RUN npm install --unsafe-perm
COPY Oppimisalusta/studyPlatform/ ./

RUN chgrp -R 0 /app && chmod -R g+rwX /app

EXPOSE 3000
CMD ["node", "app.js"]
'''

    # Create output folder if needed
    dockerfiles_dir = os.path.join(output_dir, "dockerfiles")
    os.makedirs(dockerfiles_dir, exist_ok=True)

    # Write frontend Dockerfile
    with open(os.path.join(dockerfiles_dir, "Dockerfile.frontend"), "w") as f:
        f.write(frontend_dockerfile)

    # Write backend Dockerfile
    with open(os.path.join(dockerfiles_dir, "Dockerfile.backend"), "w") as f:
        f.write(backend_dockerfile)

    print("Optimized Dockerfiles generated at:", dockerfiles_dir)
