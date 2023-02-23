# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session
from app.model.user import User


def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, username: str, password: str):
    db_user = User(username=username, password=password)
    db.add(db_user)
    db.commit()
    return db_user
