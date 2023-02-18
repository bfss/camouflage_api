# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy.orm import Session
from app.model.article import Article


def post_article(title: str, content: str, user: int, timestamp: datetime, db: Session):
    """保存文章"""
    db_article = Article(title=title, content=content, user=user, timestamp=timestamp)
    db.add(db_article)
    db.commit()
    return db_article
