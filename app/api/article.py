# -*- coding: utf-8 -*-
import os
from uuid import uuid4
import base64
from datetime import datetime
from fastapi import APIRouter, Form, Depends
from bs4 import BeautifulSoup
from app.database import get_db
from app.config import get_settings
from app.crud import article as crud_article
from app.schema import article as schema_article
from app.api.security import is_login


router = APIRouter()
settings = get_settings()


@router.post("/article")
def post_article(
    title: str = Form(),
    content: str = Form(),
    db=Depends(get_db),
    user=Depends(is_login),
):
    """接收文章"""
    soup = BeautifulSoup(content, "html.parser")
    images = soup.find_all("img")
    for image in images:
        head, encode = image["src"].split(",", 1)
        ext = head.split(";")[0].split("/")[1]
        data = base64.b64decode(encode)
        folder = os.path.join(settings.IMAGE_FOLDER, datetime.now().strftime("%Y%m%d"))
        os.makedirs(folder, exist_ok=True)
        while True:
            image_name = str(uuid4())[:8]
            image_path = os.path.join(folder, f"{image_name}.{ext}")
            if not os.path.isfile(image_path):
                break
        with open(image_path, "wb") as f:
            f.write(data)
        image["src"] = f"http://127.0.0.1:8000/{image_path}"
    crud_article.post_article(title, str(soup), user.get("id"), datetime.now(), db)


@router.get("/article", response_model=list[schema_article.AtriclesResponse])
def get_articles(db=Depends(get_db)):
    return crud_article.get_articles(db)


@router.get("/article/{article_id}")
def get_article(article_id: int, db=Depends(get_db)):
    return crud_article.get_article(article_id, db)
