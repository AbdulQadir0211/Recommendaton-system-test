from sqlalchemy import Column, String, Integer, ForeignKey
from app.database import Base

class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"))
    post_id = Column(String, ForeignKey("posts.id"))
    interaction_type = Column(String)  # e.g., "viewed", "liked", "inspired", "rated"
