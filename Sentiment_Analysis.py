
import tweepy
from textblob import TextBlob


consumer_key = "92KaXCSJo0uzDTVK328ITiEEc"
consumer_secret = "qhhcdQrhjYc7cHzZIWUXAc3bH8hSv9w3FodDnFKYBwRghcwOit"
access_token = "627462272-ImssuYeOXh7pZTSsJ6yeZYVBuc18sCnS0PaQRspG"
access_token_secret = "1mdAtzi2y2Ii0bykdXc70XbsS5iSYaAgzEv59ofw2kinB"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

politicians_list = ['Narendra Modi', 'Kejriwal', 'Rahul Gandhi', 'Arun Jaitley', 'Yogi Adityanath', 'Kumaraswamy', 'Shashi Tharoor', "Sushma Swaraj", "Amit Shah", "Mamata Bannerjee"]


def sentiment_label(polarity):
    if (polarity < 0):
        return "Neagtive"
    elif (polarity > 0):
        return "Positive"
    else:
        return "Neutral"


dictionary = {}
for name in politicians_list:
    public_tweets = api.search(name, count=100)
    sentiment = 0
    with open('%s_tweets.csv' % (name), 'w') as file:
        file.write("tweet,sentiment_label\n")
        for tweet in public_tweets:
            textblob_tweet = TextBlob(tweet.text)
            file.write('%s,%s\n' % (tweet.text, sentiment_label(textblob_tweet.sentiment.polarity)))
            sentiment = sentiment + (textblob_tweet.sentiment.polarity)
    dictionary[name] = (sentiment) / 100


print(dictionary)


print("Politician with most positive sentiment tweets")
print(max(dictionary, key=dictionary.get))

print("\nPolitician with most negative sentiment tweets")
print(min(dictionary, key=dictionary.get))
