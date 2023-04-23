# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, DateTime, Text
from app.database import Base


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False, index=True)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, index=True)
    user_id = Column(Integer, nullable=False, index=True)
