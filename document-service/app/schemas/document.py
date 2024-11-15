from pydantic import BaseModel
from datetime import datetime


class DocumentBase(BaseModel):
    filename: str


class DocumentCreate(DocumentBase):
    s3_url: str


class DocumentResponse(DocumentBase):
    id: int
    s3_url: str
    uploaded_at: datetime

    class Config:
        orm_mode = True


class DocumentMetadata(BaseModel):
    id: int
    filename: str
    username: str
    s3_url: str
    uploaded_at: datetime

    class Config:
        orm_mode = True
