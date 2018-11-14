import tweepy, markovify

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

with open('sources/bible.txt') as f:
    toMarkov = f.read()

model = markovify.Text(toMarkov)

tweet = model.make_short_sentence(140)
print(tweet)

api.update_status(tweet)
