import tweepy
from datetime import datetime, timedelta
import time
from tokens import API_KEY, API_SECRET, ACCESS_KEY, ACCESS_SECRET

# Twitter API credentials
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_KEY,
    access_token_secret=ACCESS_SECRET
)

# Countdown configuration
EVENT_DATE = datetime(2025, 5, 22, 23, 59, 59)

def post_tweet(message):
    try:
        response = client.create_tweet(text=message)
        print(f"Tweet posted successfully: {message}")
    except tweepy.TweepError as e:
        print(f"Error posting tweet: {e}")

def post_daily_countdown():
    now = datetime.now()
    time_left = EVENT_DATE - now

    if time_left.total_seconds() <= 0:
        post_tweet("🎉 The Final Reckoning is out now! Let's do this one last time🔥")
    elif time_left.days == 0:
        post_hourly_countdown()
    else:
        days = time_left.days
        countdown_message = f"⏳ {days} days left until The Final Reckoning!"
        post_tweet(countdown_message)

def post_hourly_countdown():
    last_hour = None
    while True:
        now = datetime.now()
        time_left = EVENT_DATE - now

        if time_left.total_seconds() <= 0:
            post_tweet("🎉 The Final Reckoning is out now! Enjoy 🎉")
            break
        else:
            hours_left = time_left.seconds // 3600
            if last_hour != hours_left:
                countdown_message = f"⏳ Final Countdown: {hours_left} hours left until Dead Reckoning!"
                post_tweet(countdown_message)
                last_hour = hours_left
            time.sleep(3600)

if __name__ == "__main__":
    now = datetime.now()
    if (EVENT_DATE - now).days == 0:
        post_hourly_countdown()
    else:
        post_daily_countdown()
