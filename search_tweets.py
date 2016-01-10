import tweepy
import sys
import operator
import retrive_twitter_info
import time


#climategames1
user1="climategames1"
consumer_key1 = "BbgIVypKy3NJi9hGK03ywiFTD"
consumer_secret1 = "0bQsTvk5a5u0rMksBdIl6Vh9jMdi27cXTzQfFtzmPnifP6fYXO"
access_token1 = "4331388381-DYASi2x8Q5KTRuXPxeQThyhkXece5aEMtuTHiKX"
access_token_secret1 = "sGdCmfc02YxA78odDXJUZ7oejNbFoYMwleollgHc415jt"
auth1 = tweepy.OAuthHandler(consumer_key1, consumer_secret1)
auth1.set_access_token(access_token1, access_token_secret1)
api1 = tweepy.API(auth1)

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


query = input("Which words do you want to search ?")
max_tweets = input("How many tweets do you want to retrieve? ")
search_tweets = climategames1.search_and_save_tweets(query,max_tweets)
time.sleep(15)

archivo = open('searchtweets3.txt', 'r')
for line in archivo:
    x = line.split("***")
    try:
                print("Most favorite tweet ")
                print(x[1])
                publish = input("Publish? [Y]es  to publish [N]o to pass or [E]xit to exit ")
                print(publish.lower())
                if publish.lower() == 'y':
                    climategames1.api.update_status(status=str(x[1]))
                    climategames2.api.update_status(status=str(x[1]))
                    climategames3.api.update_status(status=str(x[1]))

                    print('yes')
                elif publish.lower() == 'n':
                    print('no')
                    pass
                elif publish.lower() == 'e':
                    break
    except IndexError:
                    pass
archivo.close()

#climategames1.publish_tweet()
#time.sleep(15)



#climategames2.publish_tweet()
#time.sleep(15)
#climategames3.publish_tweet()

#time.sleep(15)
#api.update_status(status="Buenos y Feministas Dias")
#femapi.update_status(status="Buenos y Feministas Dias")

#to print the recovered tweet from file:
    #api.update_status(status=x[1])
    #femapi.update_status(status=x[1])