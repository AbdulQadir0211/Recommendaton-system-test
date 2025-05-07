from sqlalchemy import Column, String, Integer
from app.database import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    category = Column(String)
