import tweepy
from config import create_client

def delete_tweet(tweet_id):
    client = create_client()  # Initialize the client
    try:
        response = client.delete_tweet(tweet_id)
        if response:
            print(f"Tweet with ID {tweet_id} deleted successfully.")
    except tweepy.Forbidden as e:
        print("Error: You do not have permission to perform this action.")
        print(f"Details: {e}")
    except tweepy.TweepyException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    tweet_id = input("Enter the tweet ID you want to delete: ")
    delete_tweet(tweet_id)
