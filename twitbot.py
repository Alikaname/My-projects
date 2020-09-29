import tweepy
import time

auth = tweepy.OAuthHandler('bNJA2IaqEYidSoKIPIsN3lSnb', '71poMRm3uSqAImAMe3y4oQEopRMFoUeyB6lHdAogVuGZqCxATG')
auth.set_access_token('298552998-2only899kf4QmOgCEMHqvj78PA1faMWfxAXRrDfx', 'zcuy4AauGY19otHXQTKFqMTlVMZ9HnKWOSslUSklEMmrd')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()

    except tweepy.RateLimitError:
        time.sleep(300)


# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == "":
#         follower.follow()
#         break

search_string = "pisi"
number_of_tweets = 5

for tweet in tweepy.Cursor(api.search, search_string).items(number_of_tweets):
    try:
        tweet.favorite()
        print("liked")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
