# -*- coding: utf-8 -*-
from functools import lru_cache
from pydantic import BaseSettings


class DevSettings(BaseSettings):
    DATABASE_URL = "postgresql+psycopg://postgres:postgres@127.0.0.1:5432/camouflage"
    IMAGE_FOLDER = "static/images"
    # openssl rand -hex 32
    SECRET_KEY = "a749de9651e5088025df4b22e93be2a2693c585971a8fed3a216d2f2523e300a"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 2
    SUPER_USER = "admin"
    SUPER_USER_PASSWORD = "123456"
    SERVER_NAME = "http://127.0.0.1:8000"


class ProdSettings(BaseSettings):
    DATABASE_URL: str
    IMAGE_FOLDER: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    SUPER_USER: str
    SUPER_USER_PASSWORD: str
    SERVER_NAME: str


@lru_cache()
def get_settings():
    return ProdSettings()
