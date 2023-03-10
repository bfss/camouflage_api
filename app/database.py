# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import get_settings


settings = get_settings()

engine = create_engine(
    settings.DATABASE_URL
)

SessionLocal = sessionmaker(engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db():
    with SessionLocal() as db:
        yield db
