from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "760982681198944256-S4jSOYuyItZSxZCifeNKI7KrH7I18S4"
access_token_secret = "ReEehn5n6bH9QXJNCx9OBs9HIiTOKaALhxLEHW0IjcK3g"
consumer_key = "i2tMSKimnyjFWnbN6l3fmfCF3"
consumer_secret = "Bp4uf1aB3YzRyDnUsJ3gquHYLYbLyEd8sEso2f1gYlAxFJYk7Y"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    '''This handles Twitter authetification and the connection to
    Twitter Streaming API'''

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords:
    # 'python', 'javascript', 'ruby'
    stream.filter(track=['olympics', 'phelps', 'neymar'])
