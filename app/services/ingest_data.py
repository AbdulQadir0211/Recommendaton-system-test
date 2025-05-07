import requests
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.models.post import Post
from app.models.interaction import Interaction
from datetime import datetime

BASE_URL = "http://localhost:8000/api"  # Change to actual API base

def fetch_data(endpoint: str):
    response = requests.get(f"{BASE_URL}/{endpoint}")
    response.raise_for_status()
    return response.json()

def save_users(data, db: Session):
    for item in data:
        user = User(id=item["id"], name=item["name"])
        db.merge(user)
    db.commit()

def save_posts(data, db: Session):
    for item in data:
        post = Post(
            id=item["id"],
            title=item["title"],
            description=item["description"],
            author=item["author"],
            timestamp=datetime.fromisoformat(item["timestamp"].replace("Z", "+00:00"))
        )
        db.merge(post)
    db.commit()

def save_interactions(data, db: Session):
    for item in data:
        interaction = Interaction(
            id=item["id"],
            user_id=item["user_id"],
            post_id=item["post_id"],
            type=item["type"],
            timestamp=datetime.fromisoformat(item["timestamp"].replace("Z", "+00:00"))
        )
        db.merge(interaction)
    db.commit()

def ingest_all():
    db = SessionLocal()
    try:
        save_users(fetch_data("users"), db)
        save_posts(fetch_data("posts"), db)
        save_interactions(fetch_data("interactions"), db)
    finally:
        db.close()
