import tweepy

access_token = "760982681198944256-S4jSOYuyItZSxZCifeNKI7KrH7I18S4"
access_token_secret = "ReEehn5n6bH9QXJNCx9OBs9HIiTOKaALhxLEHW0IjcK3g"
consumer_key = "i2tMSKimnyjFWnbN6l3fmfCF3"
consumer_secret = "Bp4uf1aB3YzRyDnUsJ3gquHYLYbLyEd8sEso2f1gYlAxFJYk7Y"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.get_user('MichaelPhelps')

public_tweets = api.home_timeline(user)
for tweet in public_tweets:
    print(tweet.text)
