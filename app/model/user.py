# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from app.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False, index=True)
    username = Column(String(20), nullable=False, index=True)
    password = Column(String(100), nullable=False)
    