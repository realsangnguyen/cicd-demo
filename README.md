# CI/CD Pipeline Demo

A complete CI/CD pipeline using GitHub Actions to automatically test, build, and deploy a Python Flask application to Kubernetes.

## Architecture
## Application

Simple Python Flask application with:
- `GET /` — returns welcome message
- `GET /health` — health check endpoint

## Pipeline Stages

| Stage | Description |
|---|---|
| Test | Runs pytest unit and integration tests |
| Build & Push | Builds Docker image tagged with commit SHA, pushes to Docker Hub |
| Deploy | Rolling deployment to Kubernetes via kubectl |

## Infrastructure

- **Kubernetes** — Talos K8s cluster (self-hosted)
- **Container Registry** — Docker Hub
- **Runner** — Self-hosted GitHub Actions runner with kubectl

## Prerequisites

GitHub Secrets required:
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
- `KUBE_CONFIG` — base64 encoded kubeconfig

## Usage

```bash
# Run tests locally
pip install -r requirements.txt
pytest tests/

# Build Docker image
docker build -t flask-app .

# Deploy to Kubernetes
kubectl apply -f k8s/
```

## Key Concepts Demonstrated

- CI/CD pipeline with GitHub Actions
- Automated testing with pytest
- Docker image build and push with commit SHA tagging
- Zero-downtime rolling deployment to Kubernetes
- Self-hosted runner with kubectl
- Liveness and readiness probes
- Kubernetes PodSecurity hardening

## Troubleshooting Notes

Real issues encountered and resolved during build:
- kubectl missing from runner — solved with custom runner image
- PodSecurity violations on Talos — solved with securityContext
- GitHub token scope — workflow scope required for pipeline triggers

## Author

Sang Nguyen — [github.com/realsangnguyen](https://github.com/realsangnguyen)
EOF
