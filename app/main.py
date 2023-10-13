from fastapi import FastAPI, File, Form, UploadFile
from fastapi.staticfiles import StaticFiles
from typing import Annotated

from transformers import pipeline
from PIL import Image, UnidentifiedImageError
from io import BytesIO

import sys
import uuid
import logging


version = f"{sys.version_info.major}.{sys.version_info.minor}"
logger = logging.getLogger(__name__)
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

pipe = pipeline("image-classification", model="./model")

@app.get("/")
def read_root():
    msg = f"Hello isobar!!! From FastAPI Using Python {version}"
    return {"message": msg}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    request_object_content = await file.read()
    try:
        img = Image.open(BytesIO(request_object_content))
    except UnidentifiedImageError:
        return {"message": "unsupported file type"}
    if img.format not in ["JPEG", "PNG"]:
        return {"message": "unsupported file type"}
    res = pipe(img)
    #res = {"message": "success"}
    return res

@app.get("/predictdemo")
def predictdemo(fn: str = None):
    res = pipe('https://th.bing.com/th/id/OIP.7r5wE0d4exdlTXpUsp7RWwHaF1')
    return res[0]

