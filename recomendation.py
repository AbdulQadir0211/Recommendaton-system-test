# recommendation.py

from sqlalchemy.orm import Session
from models.user import User
from models.post import Post
from models.interaction import Interaction

# Recommend based on mood
def recommend_by_mood(db: Session, user_id: int) -> list[Post]:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return []
    
    return db.query(Post).filter(Post.mood == user.mood).limit(10).all()

# Recommend based on past interactions
def recommend_by_interaction(db: Session, user_id: int) -> list[Post]:
    interactions = (
        db.query(Interaction)
        .filter(Interaction.user_id == user_id)
        .order_by(Interaction.timestamp.desc())
        .limit(10)
        .all()
    )
    
    if not interactions:
        return []

    post_ids = [interaction.post_id for interaction in interactions]
    
    return db.query(Post).filter(Post.id.in_(post_ids)).all()
