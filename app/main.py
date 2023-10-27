from fastapi import FastAPI, File, Form, UploadFile
from fastapi.staticfiles import StaticFiles
from typing import Annotated

from transformers import pipeline
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from pathlib import Path

import shutil
import sys
import uuid
import logging

from logging.config import dictConfig
from log_conf import log_conf

dictConfig(log_conf)

version = f"{sys.version_info.major}.{sys.version_info.minor}"
logger = logging.getLogger(__name__)
app = FastAPI(redoc_url=None, title="app-name", version="1.0.0")
app.mount("/static", StaticFiles(directory="static"), name="static")

pipe = pipeline("image-classification", model="./model")

@app.get("/")
def read_root():
    """
    Get python version
    """
    msg = f"Hello isobar!!! From FastAPI Using Python {version}"
    return {"message": msg}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Predict an image
    """
    request_object_content = await file.read()
    try:
        img = Image.open(BytesIO(request_object_content))
    except UnidentifiedImageError:
        return {"message": "unsupported file type(1)"}
    if img.format not in ["JPEG", "PNG", "MPO"]:
        return {"message": "unsupported file type(2)"}

    # save upload file
    fileid = str(uuid.uuid1())
    fullfn = Path("upload/{}.jpg".format(fileid))
    logger.info("upload/{}".format(fullfn.name))
    try:
        with fullfn.open("wb") as buffer:
            file.file.seek(0)
            shutil.copyfileobj(file.file, buffer)
    finally:
        file.file.close()

    img.thumbnail((512,512))
    res = pipe(img)
    logger.info(res)
    return [obj for obj in res if obj['label'] == 'ghost']

@app.get("/predictdemo")
def predictdemo(fn: str = 'https://th.bing.com/th/id/OIP.7r5wE0d4exdlTXpUsp7RWwHaF1'):
    """
    Demo
    """
    res = pipe(fn)
    return res[0]

