# train.py

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from model import VideoRecommender
from prepare_data import prepare_dataset
from database import SessionLocal

# 1. Load Data
db = SessionLocal()
df = prepare_dataset(db)
db.close()

# Encode user_id and post_id as categorical ids
user2idx = {user_id: idx for idx, user_id in enumerate(df["user_id"].unique())}
post2idx = {post_id: idx for idx, post_id in enumerate(df["post_id"].unique())}

# Apply encoding
df["user_idx"] = df["user_id"].map(user2idx)
df["post_idx"] = df["post_id"].map(post2idx)

df["label"] = 1  # assuming any interaction = positive

# 2. Train-test split
X = df[["user_idx", "post_idx"]].values
y = df["label"].values
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert to tensors
X_train_tensor = torch.LongTensor(X_train)
y_train_tensor = torch.FloatTensor(y_train).unsqueeze(1)
X_val_tensor = torch.LongTensor(X_val)
y_val_tensor = torch.FloatTensor(y_val).unsqueeze(1)

# 3. Initialize model
num_users = len(user2idx)
num_posts = len(post2idx)
model = VideoRecommender(num_users=num_users, num_posts=num_posts)

# 4. Training loop
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
epochs = 10

for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    outputs = model(X_train_tensor[:, 0], X_train_tensor[:, 1])
    loss = criterion(outputs, y_train_tensor)
    loss.backward()
    optimizer.step()

    # Validation
    model.eval()
    with torch.no_grad():
        val_outputs = model(X_val_tensor[:, 0], X_val_tensor[:, 1])
        val_loss = criterion(val_outputs, y_val_tensor)

    print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}, Val Loss: {val_loss.item():.4f}")

# 5. Save model and mappings
torch.save(model.state_dict(), "recommender_model.pth")
import pickle
with open("user2idx.pkl", "wb") as f:
    pickle.dump(user2idx, f)
with open("post2idx.pkl", "wb") as f:
    pickle.dump(post2idx, f)

print("Training complete.")
