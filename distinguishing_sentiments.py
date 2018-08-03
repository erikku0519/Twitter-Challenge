### 00: Module and API Set-Up ####

# Dependencies
import tweepy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from config import consumer_key, consumer_secret, access_token, access_token_secret


# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

### 02-1: Twitter API Pull for BBC News ####

# Target User Account
target_account="@BBCNews"

for target_user in target_account:

    # Counter
    counter = 0

# Variables for holding sentiments
timestamp_list = []
compound_list = []
positive_list = []
negative_list = []
neutral_list = []
text_list = []
tweets_ago_list = []
handle_list = []

# Loop through 5 pages of tweets (total 100 tweets)
for x in range(1, 6):

    # Get all tweets from home feed
    public_tweets = api.user_timeline(target_account, page=x)

    # Loop through all tweets
    for tweet in public_tweets:

        # VADER: Run Vader Analysis on each tweet
        results = analyzer.polarity_scores(tweet["text"])
        compound = results["compound"]
        pos = results["pos"]
        neu = results["neu"]
        neg = results["neg"]
        
        # Counter and Timestamp
        counter+= 1
        tweet_time = tweet["created_at"]        
        
        # VADER: Add each value to the appropriate list
        compound_list.append(compound)
        positive_list.append(pos)
        negative_list.append(neg)
        neutral_list.append(neu)

        # Twitter Handle
        handle_list.append(tweet["user"]["screen_name"])

        # Add Text to list
        text_list.append(tweet["text"])

        # Add counter to list
        tweets_ago_list.append(counter)

        # Add Timestamp to list
        timestamp_list.append(tweet_time)
        
# Turn into DataFrame
df_bbc=pd.DataFrame(list(zip(handle_list,tweets_ago_list,timestamp_list,
                         compound_list,positive_list,negative_list,neutral_list,text_list)))


### 02-2: Twitter API Pull for CBS News ####

# Target User Account
target_account="@CBSNews"

for target_user in target_account:
    counter = 0

timestamp_list = []
compound_list = []
positive_list = []
negative_list = []
neutral_list = []
text_list = []
tweets_ago_list = []
handle_list = []

for x in range(1, 6):
    public_tweets = api.user_timeline(target_account, page=x)
    for tweet in public_tweets:
        results = analyzer.polarity_scores(tweet["text"])
        compound = results["compound"]
        pos = results["pos"]
        neu = results["neu"]
        neg = results["neg"]
        counter+= 1
        tweet_time = tweet["created_at"]        
        compound_list.append(compound)
        positive_list.append(pos)
        negative_list.append(neg)
        neutral_list.append(neu)
        handle_list.append(tweet["user"]["screen_name"])
        text_list.append(tweet["text"])
        tweets_ago_list.append(counter)
        timestamp_list.append(tweet_time)
        
# Turn into DataFrame
df_cbs=pd.DataFrame(list(zip(handle_list,tweets_ago_list,timestamp_list,
                         compound_list,positive_list,negative_list,neutral_list,text_list)))

### 02-3: Twitter API Pull for CNN ####

# Target User Account
target_account="@CNN"

for target_user in target_account:
    counter = 0

timestamp_list = []
compound_list = []
positive_list = []
negative_list = []
neutral_list = []
text_list = []
tweets_ago_list = []
handle_list = []

for x in range(1, 6):
    public_tweets = api.user_timeline(target_account, page=x)
    for tweet in public_tweets:
        results = analyzer.polarity_scores(tweet["text"])
        compound = results["compound"]
        pos = results["pos"]
        neu = results["neu"]
        neg = results["neg"]
        counter+= 1
        tweet_time = tweet["created_at"]        
        compound_list.append(compound)
        positive_list.append(pos)
        negative_list.append(neg)
        neutral_list.append(neu)
        handle_list.append(tweet["user"]["screen_name"])
        text_list.append(tweet["text"])
        tweets_ago_list.append(counter)
        timestamp_list.append(tweet_time)
        
# Turn into DataFrame
df_cnn=pd.DataFrame(list(zip(handle_list,tweets_ago_list,timestamp_list,
                         compound_list,positive_list,negative_list,neutral_list,text_list)))

### 02-4: Twitter API Pull for Fox News ####

# Target User Account
target_account="@FoxNews"

for target_user in target_account:
    counter = 0

timestamp_list = []
compound_list = []
positive_list = []
negative_list = []
neutral_list = []
text_list = []
tweets_ago_list = []
handle_list = []

for x in range(1, 6):
    public_tweets = api.user_timeline(target_account, page=x)
    for tweet in public_tweets:
        results = analyzer.polarity_scores(tweet["text"])
        compound = results["compound"]
        pos = results["pos"]
        neu = results["neu"]
        neg = results["neg"]
        counter+= 1
        tweet_time = tweet["created_at"]        
        compound_list.append(compound)
        positive_list.append(pos)
        negative_list.append(neg)
        neutral_list.append(neu)
        handle_list.append(tweet["user"]["screen_name"])
        text_list.append(tweet["text"])
        tweets_ago_list.append(counter)
        timestamp_list.append(tweet_time)
        
# Turn into DataFrame
df_fox=pd.DataFrame(list(zip(handle_list,tweets_ago_list,timestamp_list,
                         compound_list,positive_list,negative_list,neutral_list,text_list)))

### 02-5: Twitter API Pull for New York Times ####

# Target User Account
target_account="@nytimes"

for target_user in target_account:
    counter = 0

timestamp_list = []
compound_list = []
positive_list = []
negative_list = []
neutral_list = []
text_list = []
tweets_ago_list = []
handle_list = []

for x in range(1, 6):
    public_tweets = api.user_timeline(target_account, page=x)
    for tweet in public_tweets:
        results = analyzer.polarity_scores(tweet["text"])
        compound = results["compound"]
        pos = results["pos"]
        neu = results["neu"]
        neg = results["neg"]
        counter+= 1
        tweet_time = tweet["created_at"]        
        compound_list.append(compound)
        positive_list.append(pos)
        negative_list.append(neg)
        neutral_list.append(neu)
        handle_list.append(tweet["user"]["screen_name"])
        text_list.append(tweet["text"])
        tweets_ago_list.append(counter)
        timestamp_list.append(tweet_time)
        
# Turn into DataFrame
df_nyt=pd.DataFrame(list(zip(handle_list,tweets_ago_list,timestamp_list,
                         compound_list,positive_list,negative_list,neutral_list,text_list)))

### 03: Cleansing DataFrame ####

# Combine the DataFrame of 5 different media sources
df_all_news=df_bbc.append([df_cbs,df_cnn,df_fox,df_nyt])

df_all_news=df_all_news.rename(columns={0:"Handle",1:"Tweets_Ago",
                                        2:"Timestamp",3:"Compound",4:"Positive",5:"Negative",6:"Neutral",7:"Text"})

# Export as CSV File
df_all_news.to_csv("Media_Sentiment.csv", index=False, header=True)


#### 04: Data Visualization ####

# First Plot: Bar Plot of Media Sentiments
news=df_all_news["Handle"].unique()

colors=['skyblue','green','red','blue','yellow']


for n in range(5):
    plt.scatter(x=df_all_news[df_all_news["Handle"]==news[n]]["Tweets_Ago"].values,
                y=df_all_news[df_all_news["Handle"]==news[n]]["Compound"].values,
                marker="o", facecolors="red", s=40,
                c = colors[n],
                label = news[n],
                edgecolors="grey", alpha=0.75)


plt.ylim(-1, 1)
plt.grid()
plt.xlabel("Tweets Ago")
plt.ylabel("Tweet Polarity")
plt.title("Sentiment Analysis of Media Tweets (Summer 2018)")
plt.legend(title="Media Sources", loc="upper right")
plt.tight_layout()
plt.savefig("Figure01.png")
plt.show()

# Second Plot: Bar Plot of Media Sentiments

bbc_compound=df_bbc[3].mean()
cbs_compound=df_cbs[3].mean()
cnn_compound=df_cnn[3].mean()
fox_compound=df_fox[3].mean()
nyt_compound=df_nyt[3].mean()
    

news=df_all_news["Handle"].unique()
cp=[bbc_compound,cbs_compound,cnn_compound,fox_compound,nyt_compound]
overall_sentiment=[{'bbc':bbc_compound,'cbs':cbs_compound,'cnn':cnn_compound,'fox':fox_compound,'nyt':nyt_compound}]
overall_sentiment=pd.DataFrame(overall_sentiment)
overall_sentiment=overall_sentiment.transpose()
overall_sentiment=overall_sentiment.reset_index()

overall_sentiment=overall_sentiment.rename(columns={"index":"Media",0:"Avg_Comp_Sentiment"})
    

x_axis=np.arange(len(overall_sentiment))
colors={'skyblue','green','red','blue','yellow'}

plt.bar(news,cp,alpha=0.5,align="center",width=1,edgecolor="black",color=colors)
plt.ylabel("Tweet Polarity")
plt.title("Overall Media Sentiment based on Twitter (Summer 2018)")
plt.savefig("Figure02.png")
plt.show()