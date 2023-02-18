# -*- coding: utf-8 -*-
from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_HOST = "127.0.0.1"
    DATABASE_PORT = "5432"
    DATABASE_USER = "postgres"
    DATABASE_PASSWORD = "postgres"
    DATABASE_NAME = "camouflage"
    IMAGE_FOLDER = "static/images"


@lru_cache()
def get_settings():
    return Settings()
