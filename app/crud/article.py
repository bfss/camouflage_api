# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy.orm import Session
from app.model.article import Article


def post_article(title: str, content: str, user_id: int, timestamp: datetime, db: Session):
    """保存文章"""
    db_article = Article(title=title, content=content, user_id=user_id, timestamp=timestamp)
    db.add(db_article)
    db.commit()
    return db_article


def get_articles(db: Session):
    """获取所有文章"""
    return db.query(Article).order_by(Article.timestamp.desc()).all()


def get_article(article_id: int, db: Session):
    """获取一篇文章"""
    return db.query(Article).filter(Article.id == article_id).first()
