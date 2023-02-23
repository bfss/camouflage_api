# -*- coding: utf-8 -*-
from passlib.hash import pbkdf2_sha256
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.api.article import router as article_router
from app.api.user import router as user_router
from app.database import SessionLocal
from app.crud import user as crud_user
from app.config import get_settings


app = FastAPI(title="API", version="0.1.0", openapi_url=None)
settings = get_settings()

app.mount(settings.IMAGE_FOLDER, StaticFiles(directory=settings.IMAGE_FOLDER), name="images")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(article_router)
app.include_router(user_router)

@app.on_event("startup")
def startup():
    db = SessionLocal()
    if not crud_user.get_user(db, settings.SUPER_USER):
        crud_user.create_user(
            db,
            username=settings.SUPER_USER,
            password=pbkdf2_sha256.hash(settings.SUPER_USER_PASSWORD)
        )
    db.close()
