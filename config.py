import os
import tweepy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_client():
    # Fetch credentials from environment variables
    bearer_token = os.getenv("BEARER_TOKEN")
    api_key = os.getenv("API_KEY")
    api_secret_key = os.getenv("API_SECRET_KEY")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    # Set up client using Tweepy
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=api_key,
        consumer_secret=api_secret_key,
        access_token=access_token,
        access_token_secret=access_token_secret
    )
    return client
