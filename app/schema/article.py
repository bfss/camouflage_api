# -*- coding: utf-8 -*-
from datetime import datetime
from pydantic import BaseModel


class AtriclesResponse(BaseModel):
    id: int
    title: str
    timestamp: datetime

    class Config:
        orm_mode = True
