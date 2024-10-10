import tweepy
from config import create_client

def post_tweet(text):
    client = create_client()  # Initialize the client
    try:
        response = client.create_tweet(text=text)
        print("Tweet posted successfully.")
        print(f"Tweet ID: {response.data['id']}")
    except tweepy.Forbidden as e:
        print("Error: You do not have permission to perform this action.")
        print(f"Details: {e}")
    except tweepy.TweepyException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    tweet_text = input("Post your tweet: ")
    post_tweet(tweet_text)