from fastapi import APIRouter
from app.utils.data_fetcher import fetch_data_from_endpoint

router = APIRouter()

@router.get("/collect/viewed-posts")
async def get_viewed_posts():
    data = await fetch_data_from_endpoint("posts/view")
    return data

@router.get("/collect/liked-posts")
async def get_liked_posts():
    data = await fetch_data_from_endpoint("posts/like")
    return data

@router.get("/collect/inspired-posts")
async def get_inspired_posts():
    data = await fetch_data_from_endpoint("posts/inspire")
    return data

@router.get("/collect/rated-posts")
async def get_rated_posts():
    data = await fetch_data_from_endpoint("posts/rating")
    return data

@router.get("/collect/all-posts")
async def get_all_posts():
    data = await fetch_data_from_endpoint("posts/summary/get", include_resonance=False)
    return data

@router.get("/collect/all-users")
async def get_all_users():
    data = await fetch_data_from_endpoint("users/get_all", include_resonance=False)
    return data
