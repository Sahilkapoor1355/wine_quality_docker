
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import numpy as np
import joblib
import os
import uvicorn

# Initialize FastAPI
app = FastAPI()

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Templates configuration
templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "templates")
)

# Static files configuration
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)

# Load trained model
model = joblib.load(
    os.path.join(BASE_DIR, "wine_model.joblib")
)

# Input columns
cols = [
    'fixed acidity',
    'volatile acidity',
    'citric acid',
    'residual sugar',
    'chlorides',
    'free sulfur dioxide',
    'total sulfur dioxide',
    'density',
    'pH',
    'sulphates',
    'alcohol'
]


# Home page
@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "cols": cols,
            "prediction": None
        }
    )


# Prediction route
@app.post("/")
async def predict(request: Request):

    form = await request.form()

    In = []

    for col in cols:
        value = float(form[col])
        In.append(value)

    # Predict wine quality
    out = model.predict([In])

    prediction = float(out[0])

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "cols": cols,
            "prediction": prediction
        }
    )


# Run application
if __name__ == "__main__":

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )
