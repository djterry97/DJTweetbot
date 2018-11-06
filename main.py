import tweepy, markovify

consumer_key = 'APDpS7Z3PXHZrc3Tf25m2xWLu '
consumer_secret = 'uiiOdjdsl27vGsvi1hycC5FiFqyjRNwcQCHtbJ5pOFtHELObN9 '
access_token = '1059596360171876352-TUe8IJFXpGCTxVQczXZgg4LqroTDpn'
access_secret = 'hMti3N1ZlVxQAlqw6dFucipANxJcl0bfCZvdO0StxuET2'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

with open('sources/bible.txt') as f:
    toMarkov = f.read()

model = markovify.Text(toMarkov)

tweet = model.make_short_sentence(140)
print(tweet)

api.update_status(tweet)
