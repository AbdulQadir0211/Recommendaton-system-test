from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import user, post, interaction
from schemas import UserCreate, PostCreate, InteractionCreate
from crud import save_users, save_posts, save_interactions
from recommendation.infer import recommend_posts

# Create all tables
user.Base.metadata.create_all(bind=engine)
post.Base.metadata.create_all(bind=engine)
interaction.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ----------------------------
# Ingestion Endpoints
# ----------------------------

@app.post("/ingest/users")
def ingest_users(users: list[UserCreate], db: Session = Depends(get_db)):
    save_users(db, users)
    return {"message": f"{len(users)} users saved."}


@app.post("/ingest/posts")
def ingest_posts(posts: list[PostCreate], db: Session = Depends(get_db)):
    save_posts(db, posts)
    return {"message": f"{len(posts)} posts saved."}


@app.post("/ingest/interactions")
def ingest_interactions(interactions: list[InteractionCreate], db: Session = Depends(get_db)):
    save_interactions(db, interactions)
    return {"message": f"{len(interactions)} interactions saved."}


# ----------------------------
# Recommendation Endpoint
# ----------------------------

@app.get("/recommend/{user_id}")
def get_recommendations(user_id: int, top_k: int = 5):
    try:
        posts = recommend_posts(user_id=user_id, top_k=top_k)
        return [{"id": p.id, "content": p.content} for p in posts]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
