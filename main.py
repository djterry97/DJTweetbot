import tweepy, markovify, random

# Keys and Tokens to access @DJTwitterbot
consumer_key = 's9TGxOnUOxDag7P0T93MSxKkv'
consumer_secret = 'U2PwUyOd7qYOnDSbD8evy8Ebff1dlpjK0onYzpxKpEob3BoOng'
access_token = '1059596360171876352-TUe8IJFXpGCTxVQczXZgg4LqroTDpn'
access_secret = 'hMti3N1ZlVxQAlqw6dFucipANxJcl0bfCZvdO0StxuET2'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Get random book number, with better naming convention this will change
num = random.randint(1, 900)

# Set the filename, hopefully I can find a clearer naming convention soon
openFile = "sources\\" + str(num) + '.txt'
with open(openFile) as f:
    file = f.read()

text = markovify.Text(file)

# Make the tweet, if it is too long or not long enough, do it again
# Num helps me know what book is being used
tweet = str(num) + ': ' + text.make_sentence()
while len(tweet) > 280 or len(tweet) < 95:
    tweet = str(num) + ': ' + text.make_sentence()

# Update @DJTwitterbot status, print what was sent
api.update_status(tweet)
print(tweet)
