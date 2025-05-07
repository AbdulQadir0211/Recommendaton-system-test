# 📽️ Video Recommendation Engine

A minimal video recommendation system using FastAPI and deep learning, based on user mood and interaction data.

## 📌 Features

* Fetches user, post, and interaction data from external/mock APIs.
* Stores data in a local SQLite database using SQLAlchemy.
* Trains a simple neural network recommendation model using PyTorch.
* Recommends videos (posts) to users based on mood and past interaction history.
* Provides FastAPI endpoints for triggering recommendations.

---

## ⚙️ Tech Stack

* **Backend Framework**: FastAPI
* **ORM**: SQLAlchemy
* **Database**: SQLite
* **Deep Learning**: PyTorch
* **Migrations**: Alembic

---

## 📁 Project Structure

```
video-recommendation-assignment/
│
├── app/
│   ├── main.py               # FastAPI entrypoint
│   ├── database.py           # SQLAlchemy DB setup
│   ├── models/
│   │   ├── user.py
│   │   ├── post.py
│   │   └── interaction.py
│   ├── crud.py               # DB insert functions
│   ├── schemas.py            # Pydantic schemas
│   ├── ml/
│   │   ├── train.py          # Model training
│   │   └── recommend.py      # Recommendation inference
│   ├── ingest.py             # API data fetching and saving
│   └── mock_api/             # FastAPI mock endpoints
│
├── migrations/               # Alembic migration files
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/video-recommendation-assignment.git
cd video-recommendation-assignment
```

### 2. Set Up Environment

```bash
python -m venv rec
source rec/bin/activate  # On Windows: rec\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure `.env`

Create a `.env` file in the root directory:

```
DATABASE_URL=sqlite:///./test.db
```

---

### 4. Run Alembic Migrations

```bash
alembic upgrade head
```

---

### 5. Ingest Mock Data

In one terminal, run the mock API:

```bash
uvicorn app.mock_api.main:app --port 8001
```

In another terminal, run:

```bash
python app/ingest.py
```

---

### 6. Train the Recommendation Model

```bash
python app/ml/train.py
```

---

### 7. Start the FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

## 🧠 Recommendation Logic

* A simple feedforward neural network is trained using user-post interaction features:

  * Mood
  * Watch time
  * Like status
* It predicts and ranks post recommendations for users.

---

## 📢 API Endpoints

| Method | Endpoint               | Description                        |
| ------ | ---------------------- | ---------------------------------- |
| GET    | `/recommend/{user_id}` | Get top recommendations for a user |
| GET    | `/train`               | Trigger model training             |
| GET    | `/ingest`              | Trigger data fetching and storage  |

---

## ✅ Assignment Scope Covered

* ✅ API data fetching
* ✅ SQLAlchemy models and DB storage
* ✅ Deep learning-based recommendation logic
* ✅ FastAPI endpoints for recommendations
* ✅ No extra features added beyond assignment

---

## 🧪 Example

```bash
curl http://localhost:8000/recommend/1
```

---

## 💼 Cleanup

To reset the database:

```bash
rm test.db
alembic downgrade base
alembic upgrade head
```

---

## 📄 License
