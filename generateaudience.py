import tweepy
import sys
import operator
import retrive_twitter_info
import time

#royal
#user1="shoptheroyalwe"
#consumer_key1 = "MOCS4kDoTDVTdT7XPUnIsFECL"
#consumer_secret1 = "quJUZvjoNRxBMOwmbKw1ozdY4LKSPrqvfagZu7JF0I8tk8oona"
#access_token1 = "4520033536-PVVpUnLWZbfVtbFcH267Kx6An7WpWM69N7fjiEZ"
#access_token_secret1 = "hj2UGoJwvFVnl3htb75i0odANcAl6sUQOLyfV9nGKjxnA"
#auth1 = tweepy.OAuthHandler(consumer_key1, consumer_secret1)
#auth1.set_access_token(access_token1, access_token_secret1)
#api1 = tweepy.API(auth1)



#climategames1
#user1="climategames1"
#consumer_key1 = "BbgIVypKy3NJi9hGK03ywiFTD"
#consumer_secret1 = "0bQsTvk5a5u0rMksBdIl6Vh9jMdi27cXTzQfFtzmPnifP6fYXO"
#access_token1 = "4331388381-DYASi2x8Q5KTRuXPxeQThyhkXece5aEMtuTHiKX"
#access_token_secret1 = "sGdCmfc02YxA78odDXJUZ7oejNbFoYMwleollgHc415jt"
#auth1 = tweepy.OAuthHandler(consumer_key1, consumer_secret1)
#auth1.set_access_token(access_token1, access_token_secret1)
#api1 = tweepy.API(auth1)

climategames1 = retrive_twitter_info.GetTwitterInfo(consumer_key1,consumer_secret1,access_token1,access_token_secret1,user1)

#climategames2
user2 = "climategames2"
consumer_key2 = "JVKqhuoG4lZOrzsk8prDGDPzw"
consumer_secret2 = "KBj0TqI74kitjQy5H3t3XgEx11WUJlpx0NFsJEYRdT3tVUW6Sz"
access_token2 = "4331461101-ssMkvdGD04vpkJLyebnqT1mMz4IUYbNTTAyh50C"
access_token_secret2 = "JkRc7uQmXPHk3axKVhkIshJ9kCXTwGORXvIjv64NAP8gz"
auth2 = tweepy.OAuthHandler(consumer_key2, consumer_secret2)
auth2.set_access_token(access_token2, access_token_secret2)
api2 = tweepy.API(auth2)

climategames2 = retrive_twitter_info.GetTwitterInfo(consumer_key2,consumer_secret2,access_token2,access_token_secret2,user2)


#climategames3
user3 = "climategames3"
consumer_key3 = "k7KiN6lGzUMKI6i9LZnLVf0Ff"
consumer_secret3 = "4KE8gQxMGschMlZm0JzVFXp0GRUHRQC2c4uhIgOdZS6tpEORWx"
access_token3 = "4331903416-t6T71ICFpuYIUH8uGlxJzCEmuHfluDueDYNDO3f"
access_token_secret3 = "By1vkuEa6tzxrMrKUEDfZSZlCMC2sIxTBhJG4HLqwYwRX"
auth3 = tweepy.OAuthHandler(consumer_key3, consumer_secret3)
auth3.set_access_token(access_token3, access_token_secret3)
api3= tweepy.API(auth3)

climategames3 = retrive_twitter_info.GetTwitterInfo(consumer_key3,consumer_secret3,access_token3,access_token_secret3,user3)

def follow_non_repeated_users(searched_tweets,bot_used):
    """

        Check that the other bots are not following
        the same user that the main bot wants to follow
        Right now it does not check that yet, it needs to be improved so we are not making that many calls to twitter API

    """
    if bot_used==1:
        used_bot="climategames1"
    elif bot_used==2:
        used_bot="climategames2"
    elif bot_used==3:
        used_bot="climategames3"
    print("Bot " ,(used_bot), "wants to follow")
    wantofollow=(searched_tweets.user.screen_name)
    print(wantofollow)
    follow= find_ratio(wantofollow)
    #iduserbotA = climategames2.following_info()

    #for users in iduserbotA:

        #if wantofollow is (climategames2.get_screen_name(users)):
        #    print("bot 2 is following that user")
        #else:
        #    print("bot 2 is not following that user")
            #if other bots are not following that user, then it creates a relationship between the original bot and the new recruited user
            #if the main bot is going to follow the user, the other bots cannot follow that user or being followed by that user
            # (this to have differente audiences in each bot)

    if bot_used==1 and follow == 1:
        print("following")
        climategames1.creates_frienship(wantofollow)
    elif bot_used==2:
        print("who am i ",climategames2.screen_name)
        climategames2.creates_frienship(wantofollow)
    elif bot_used==3:
        climategames3.creates_frienship(wantofollow)
    time.sleep(60)


def find_ratio(wantofollow):
    ratio =climategames1.get_user_ratio(wantofollow)
    print("ratio: ", ratio)
    if ratio < 1.5:
        follow = 1
    else:
        follow = 0

    return  follow


def follow_users(searched_tweets,bot_used):
    """
    This function only follows the users that where retrieved by the keywords in their tweets
    :param searched_tweets:
    :return:nothing
    """
    lenghtusers = len(searched_tweets)
    print(lenghtusers)
    for items in searched_tweets:
        time.sleep(15)
        follow_non_repeated_users(items,bot_used)
        print(searched_tweets[lenghtusers-1].text)





def generate_audience():
    query = input("Which words do you want to search ?")
    max_tweets = input("How many tweets do you want to retrieve? ")
    bot_used = int(input("Which bot do you want to use? [1]bot1, [2],bot2, [3]bot3: "))
    print("bot used",bot_used)

    if bot_used == 1:
            searched_tweets = climategames1.search_and_save_tweets(query,max_tweets)
    #print(searched_tweets)
    elif bot_used == 2:
            searched_tweets = climategames2.search_and_save_tweets(query,max_tweets)

    elif bot_used == 3:
            searched_tweets = climategames3.search_and_save_tweets(query,max_tweets)


    follow_users(searched_tweets,bot_used)


generate_audience()

