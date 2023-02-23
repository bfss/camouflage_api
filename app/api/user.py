# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from fastapi import APIRouter, Form, Depends, HTTPException, status
from passlib.hash import pbkdf2_sha256
from jose import jwt
from app.database import get_db
from app.config import get_settings
from app.crud import user as crud_user
from app.api.security import is_login


router = APIRouter()
settings = get_settings()


@router.post("/login")
def login(username: str = Form(), password: str = Form(), db=Depends(get_db)):
    db_user = crud_user.get_user(db, username)
    if db_user and pbkdf2_sha256.verify(password, db_user.password):
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        to_encode = {"id": db_user.id, "username": username, "exp": expire}

        encoded_jwt = jwt.encode(
            to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
        )
        return {"access_token": encoded_jwt}
    raise HTTPException(status.HTTP_401_UNAUTHORIZED)

@router.get("/checkout")
def checkout(user=Depends(is_login)):
    pass
