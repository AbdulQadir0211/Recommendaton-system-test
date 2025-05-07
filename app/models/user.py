from sqlalchemy import Column, String, Integer
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    username = Column(String, index=True)
