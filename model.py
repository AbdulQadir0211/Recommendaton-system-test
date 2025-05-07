# model.py

import torch
import torch.nn as nn

class VideoRecommender(nn.Module):
    def __init__(self, num_users, num_posts, embedding_dim=32):
        super(VideoRecommender, self).__init__()
        self.user_embed = nn.Embedding(num_users, embedding_dim)
        self.post_embed = nn.Embedding(num_posts, embedding_dim)
        self.fc1 = nn.Linear(embedding_dim * 2, 64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64, 1)  # Predicts interaction score

    def forward(self, user_ids, post_ids):
        user_vec = self.user_embed(user_ids)
        post_vec = self.post_embed(post_ids)
        combined = torch.cat([user_vec, post_vec], dim=1)
        x = self.fc1(combined)
        x = self.relu(x)
        return self.fc2(x)
