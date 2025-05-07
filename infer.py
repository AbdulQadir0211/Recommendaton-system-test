import torch
from torch.nn.functional import cosine_similarity
from database import SessionLocal
from models.user import User
from models.post import Post
from models.interaction import Interaction
from recommendation.model import RecommendationModel

# Load trained model
MODEL_PATH = "recommendation/model.pth"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = RecommendationModel(num_users=1000, num_posts=1000, embed_dim=32).to(device)
model.load_state_dict(torch.load(MODEL_PATH))
model.eval()

def recommend_posts(user_id: int, top_k: int = 5):
    session = SessionLocal()

    all_posts = session.query(Post).all()
    post_ids = [post.id for post in all_posts]

    user_tensor = torch.tensor([user_id] * len(post_ids), dtype=torch.long).to(device)
    post_tensor = torch.tensor(post_ids, dtype=torch.long).to(device)

    with torch.no_grad():
        user_embeds = model.user_embedding(user_tensor)
        post_embeds = model.post_embedding(post_tensor)
        scores = cosine_similarity(user_embeds, post_embeds)

    # Get top K post IDs
    top_indices = torch.topk(scores, top_k).indices
    recommended_post_ids = [post_ids[i] for i in top_indices.cpu().numpy()]
    recommended_posts = session.query(Post).filter(Post.id.in_(recommended_post_ids)).all()

    session.close()
    return recommended_posts
