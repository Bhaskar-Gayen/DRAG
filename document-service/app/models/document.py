from sqlalchemy import Column, Integer, String, DateTime
from models import Base
from datetime import datetime


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True, nullable=False)
    username = Column(String, index=True, nullable=False)
    s3_url = Column(String, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.now)
