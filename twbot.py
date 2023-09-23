import tweepy
import schedule
import time
from datetime import datetime

# Twitter API credentials
consumer_key = 'NKS9VIrhB4xEm3y4hys5prGU3'
consumer_secret = 'eeGA5U6V8YFiMO6ZTnEceowi7QyWzwumTEeTmONShzhFwPVfPG'
access_token = '1620428308985831424-ONux53aIokbCIPyP4XZo3VMUt0KVRX'
access_token_secret = 'vzIuwGsWyBlnHPysRETf9eaZcTyQyLZlqCgTCwIPz9uPP'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Paths to the video files you want to tweet
video_paths = ['C:\\slikice\\twbot\\popodne.mp4', 'C:\\slikice\\twbot\\ujutro.mp4']
# Add more paths as needed

# Function to tweet a video
def tweet_video(video_path):
    try:
        # Get the current date and time
        current_datetime = datetime.now()
        
        # Format the date and time
        formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M:%S")

        # Check if it's 6:15 AM or 6:15 PM
        if current_time.hour == 6 and current_time.minute == 15:
            # Upload the video
            media = api.media_upload(filename=video_path)

            # Tweet the video
            tweet_text = "{formatted_datetime}"
            api.update_status(status=tweet_text, media_ids=[media.media_id])
            print(tweet_text)

    except Exception as e:
        print("Error:", str(e))

# Schedule the tweet with different videos at 5:15 AM and 5:15 PM every day
schedule.every().day.at("06:15").do(tweet_video, video_paths[1])
schedule.every().day.at("18:15").do(tweet_video, video_paths[0])

# Run the bot
while True:
    schedule.run_pending()
    time.sleep(1)
heroku create myapp --buildpack heroku/python
