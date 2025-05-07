from sqlalchemy.orm import Session
from models.user import User
from models.post import Post
from models.interaction import Interaction
from schemas import UserCreate, PostCreate, InteractionCreate


def save_users(db: Session, users: list[UserCreate]):
    for u in users:
        if not db.query(User).filter(User.id == u.id).first():
            user = User(id=u.id, name=u.name, age=u.age, gender=u.gender)
            db.add(user)
    db.commit()


def save_posts(db: Session, posts: list[PostCreate]):
    for p in posts:
        if not db.query(Post).filter(Post.id == p.id).first():
            post = Post(id=p.id, title=p.title, content=p.content, mood=p.mood)
            db.add(post)
    db.commit()


def save_interactions(db: Session, interactions: list[InteractionCreate]):
    for i in interactions:
        if not db.query(Interaction).filter(
            Interaction.user_id == i.user_id and Interaction.post_id == i.post_id
        ).first():
            interaction = Interaction(
                user_id=i.user_id, post_id=i.post_id,
                liked=i.liked, watch_time=i.watch_time
            )
            db.add(interaction)
    db.commit()
