This Repo demonstrates how to **serve a Machine Learning model** using **FastAPI** and **Docker**.  
It allows you to train, save, and deploy an ML model as a REST API that can receive input data and return predictions.

## 📦 Quick Start (Docker)

You can directly pull and run the prebuilt image without cloning the repo.

```bash
docker pull beekrm/ml-image
docker run -d -p 8000:8000 --name ml-api beekrm/ml-image
