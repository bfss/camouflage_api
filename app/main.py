# -*- coding: utf-8 -*-
from passlib.hash import pbkdf2_sha256
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.api.article import router as article_router
from app.api.user import router as user_router
from app.database import SessionLocal
from app.crud import user as crud_user


app = FastAPI()

app.mount("/static/images", StaticFiles(directory="static/images"), name="images")

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
    if not crud_user.get_user(db, "admin"):
        crud_user.create_user(
            db,
            username="admin",
            password=pbkdf2_sha256.hash("123456")
        )
    db.close()
