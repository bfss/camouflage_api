# -*- coding: utf-8 -*-
import os
from datetime import datetime
from uuid import uuid4
import base64
import requests
from app.config import get_settings


settings = get_settings()


def save_image(image_obj):
    folder = os.path.join(settings.IMAGE_FOLDER, datetime.now().strftime("%Y%m%d"))
    os.makedirs(folder, exist_ok=True)
    if image_obj["src"].startswith("data:image"):
        # base64格式
        head, encode = image_obj["src"].split(",", 1)
        # ext = head.split(";")[0].split("/")[1]
        data = base64.b64decode(encode)
    else:
        # 网页上的图片
        response = requests.get(image_obj["src"])
        # ext = "jpg"
        data = response.content
    while True:
        image_name = str(uuid4())[:8]
        image_path = os.path.join(folder, f"{image_name}.jpg")
        if not os.path.isfile(image_path):
            break
    with open(image_path, "wb") as f:
        f.write(data)
    return image_path
