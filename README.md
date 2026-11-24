# 🍷 Wine Quality Predictor (FastAPI + Docker)

A containerized machine learning web application built with **FastAPI**, **Jinja2**, **NumPy**, **Joblib**, and **Docker** that predicts wine quality from 11 physicochemical features using a pre-trained model (`wine_model.joblib`).

---

## ✨ Features

- **Real-Time Wine Quality Inference:** Loads `wine_model.joblib` at startup and serves predictions through a `POST /` endpoint.
- **Interactive Web Interface:** Renders `templates/index.html` with `GET /` and `POST /` routes and serves static assets from `/static`.
- **Dockerized Deployment:** Ready to build and run inside a container with `requirements.txt` and `wine_model.joblib`.

---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, Uvicorn
- **Frontend:** Jinja2 Templates (`templates/index.html`), Static Files (`static/`)
- **Machine Learning & Data:** NumPy, Joblib (`wine_model.joblib`), scikit-learn
- **Containerization:** Docker

---

## 📂 Project Structure

```text
├── app.py                 # FastAPI app, GET/POST routes, and model inference
├── wine_model.joblib      # Serialized pre-trained wine quality model
├── Dockerfile             # Docker image build instructions
├── requirements.txt       # Python dependencies
├── static/                # Static assets (CSS, JS, images)
└── templates/
    └── index.html         # Input form and prediction display template
