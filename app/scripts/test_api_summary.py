import asyncio
from utils.data_fetcher import fetch_data_from_endpoint


async def main():
    print("\n📥 Fetching Viewed Posts...")
    viewed = await fetch_data_from_endpoint("posts/view")
    print(f"Viewed Posts Count: {len(viewed.get('data', []))}")

    print("\n❤️ Fetching Liked Posts...")
    liked = await fetch_data_from_endpoint("posts/like")
    print(f"Liked Posts Count: {len(liked.get('data', []))}")

    print("\n✨ Fetching Inspired Posts...")
    inspired = await fetch_data_from_endpoint("posts/inspire")
    print(f"Inspired Posts Count: {len(inspired.get('data', []))}")

    print("\n⭐ Fetching Rated Posts...")
    rated = await fetch_data_from_endpoint("posts/rating")
    print(f"Rated Posts Count: {len(rated.get('data', []))}")

    print("\n📦 Fetching All Posts Summary...")
    all_posts = await fetch_data_from_endpoint("posts/summary/get", include_resonance=False)
    print(f"All Posts Count: {len(all_posts.get('data', []))}")

    print("\n👤 Fetching All Users...")
    all_users = await fetch_data_from_endpoint("users/get_all", include_resonance=False)
    print(f"All Users Count: {len(all_users.get('data', []))}")


if __name__ == "__main__":
    asyncio.run(main())
