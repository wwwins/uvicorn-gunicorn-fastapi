import requests
import os
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from pathlib import Path
import torch
from transformers import pipeline


# Using pipeline
#pipe(url)
#pipe(image)
pipe = pipeline("image-classification", model="./model")

# Kiwi
#url = 'https://th.bing.com/th/id/OIP.7r5wE0d4exdlTXpUsp7RWwHaF1?w=227&h=180'
# Mango
#url = 'https://th.bing.com/th/id/OIP.J1I5WGloDBIOCnHZqo668AHaFj?w=242&h=182'
# Strawberry
#url = 'https://th.bing.com/th/id/OIP.k44Y0_OQboq_jifg7fIDAAHaF7?w=216&h=180'
# Coconut
#url = 'https://th.bing.com/th/id/OIP.TRl10fQ04locjkckMnHY9gHaFj?w=216&h=180'
#myimage = Image.open(requests.get(url, stream=True).raw)
#predict(myimage)

if __name__ == '__main__':
    import timeit
    images = []
    urls = ('https://th.bing.com/th/id/OIP.7r5wE0d4exdlTXpUsp7RWwHaF1?w=227&h=180','https://th.bing.com/th/id/OIP.J1I5WGloDBIOCnHZqo668AHaFj?w=242&h=182','https://th.bing.com/th/id/OIP.k44Y0_OQboq_jifg7fIDAAHaF7?w=216&h=180')
    for url in urls:
        images.append(Image.open(requests.get(url, stream=True).raw))
    print(timeit.timeit("pipe(images[0]),pipe(images[1]),pipe(images[2])", globals=globals(), number=10))
