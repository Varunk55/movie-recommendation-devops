# 🎬 Movie Recommendation System

This is a simple movie recommender web app using Streamlit and a Bayesian network.

## 🔧 Technologies Used
- Python
- Streamlit
- scikit-learn, pandas, networkx
- Docker
- Jenkins for CI/CD

## ⚙️ CI/CD Pipeline
- Jenkins pulls code from GitHub
- Installs dependencies
- Runs tests (pytest)
- Builds Docker image
- Pushes to DockerHub

## 🐳 Docker Commands
```bash
docker build -t movie-recommender .
docker run -p 8501:8501 movie-recommender
