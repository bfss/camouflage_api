# -*- coding: utf-8 -*-
from fastapi import Header, HTTPException, status
from jose import jwt
from app.config import get_settings
from app.crud import user as crud_user


settings = get_settings()


def is_login(authorization: str = Header()):
    try:
        payload = jwt.decode(authorization, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        id = payload.get("id")
        username = payload.get("username")

    except:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)

    return {"id": id, "username": username}
