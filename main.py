import os
import tweepy
from datetime import datetime, timedelta

# Twitter API credentials from environment variables
client = tweepy.Client(
    consumer_key=os.environ['API_KEY'],
    consumer_secret=os.environ['API_SECRET'],
    access_token=os.environ['ACCESS_KEY'],
    access_token_secret=os.environ['ACCESS_SECRET']
)

# Countdown configuration
EVENT_DATE = datetime(2025, 5, 22, 23, 59, 59)

def post_tweet(message):
    try:
        response = client.create_tweet(text=message)
        print(f"Tweet posted successfully: {message}")
    except Exception as e:
        print(f"Error posting tweet: {e}")

def post_daily_countdown():
    now = datetime.now()
    time_left = EVENT_DATE - now

    if time_left.total_seconds() <= 0:
        post_tweet("🎉 The Final Reckoning is out now! Let's do this one last time🔥")
    else:
        days = time_left.days
        countdown_message = f"⏳ {days} days left until The Final Reckoning!"
        post_tweet(countdown_message)

if __name__ == "__main__":
    post_daily_countdown()
