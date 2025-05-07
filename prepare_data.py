# prepare_data.py

from sqlalchemy.orm import Session
from models.interaction import Interaction
from models.user import User
from models.post import Post
import pandas as pd

def prepare_dataset(db: Session):
    interactions = db.query(Interaction).all()
    data = []

    for interaction in interactions:
        user = db.query(User).filter(User.id == interaction.user_id).first()
        post = db.query(Post).filter(Post.id == interaction.post_id).first()
        if user and post:
            data.append({
                "user_id": user.id,
                "post_id": post.id,
                "mood": user.mood,
                "post_mood": post.mood,
                "interaction_type": interaction.interaction_type,
            })
    
    return pd.DataFrame(data)
