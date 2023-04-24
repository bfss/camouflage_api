# -*- coding: utf-8 -*-
import os
from datetime import datetime
from fastapi import APIRouter, Form, Depends
from bs4 import BeautifulSoup
from app.database import get_db
from app.config import get_settings
from app.crud import article as crud_article
from app.schema import article as schema_article
from app.api.security import is_login
from app.tools.image import save_image


router = APIRouter()
settings = get_settings()


@router.post("/article")
def post_article(
    article: schema_article.ArticlePost,
    db=Depends(get_db),
    user=Depends(is_login),
):
    """接收文章"""
    soup = BeautifulSoup(article.content, "html.parser")
    images = soup.find_all("img")
    for image in images:
        image_path = save_image(image)
        image["src"] = f"{settings.SERVER_NAME}/{image_path}"
    db_article = crud_article.post_article(
        article.title, str(soup), user.get("id"), datetime.now(), db
    )
    return {"id": db_article.id}


@router.get("/article", response_model=list[schema_article.AtriclesResponse])
def get_articles(db=Depends(get_db)):
    return crud_article.get_articles(db)


@router.get("/article/{article_id}")
def get_article(article_id: int, db=Depends(get_db)):
    return crud_article.get_article(article_id, db)


@router.patch("/article/{article_id}")
def patch_article(article_id:int, article: schema_article.ArticlePost, db=Depends(get_db)):
    """更新文章"""
    soup = BeautifulSoup(article.content, "html.parser")
    images = soup.find_all("img")
    for image in images:
        image_path = save_image(image)
        image["src"] = f"{settings.SERVER_NAME}/{image_path}"
    
    db_article = crud_article.update_article(article_id, article.title, str(soup), db)
    return {"id": db_article.id}
