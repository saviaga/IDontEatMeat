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

user4 = "climategames4"
consumer_key4 = "aT0WkPryzyu5YlxzgfYIkXyzy"
consumer_secret4 = "VdIEYAHCWicmNEIAUAseULcRac7egPXiigaCeTuxnYZk9JVYIx"
access_token4 = "4488323893-Lm4UaBHX1a8Mul3xfjBZVoP8J4dTUMA5VKq1xb5"
access_token_secret4 = "lWVfMvkTxxDNG3VrwTgU6yip8bCdOT99GrjdFbBh0GAfB"
auth4 = tweepy.OAuthHandler(consumer_key4, consumer_secret4)
auth4.set_access_token(access_token4, access_token_secret4)
api4= tweepy.API(auth4)

climategames4 = retrive_twitter_info.GetTwitterInfo(consumer_key4,consumer_secret4,access_token4,access_token_secret4,user4)


user5 = "climategames5"
consumer_key5 = "Ob9BUfSIeccUKYCwmzmswmFCJ"
consumer_secret5 = "M6nNAv4wQAnfYKaqKxx8wt2EwbkahKg4nr20dxeAWBDR2t51Bb"
access_token5 = "4407896721-LZwcwISJF7NmWSpcSy2qmectPe8edQFk5SwZDpt"
access_token_secret5 = "ibGmBFsLna9ucqJmmBXzuhhUqdN4ZOpLv0KxD8pcrUBR4"
auth5 = tweepy.OAuthHandler(consumer_key5, consumer_secret5)
auth5.set_access_token(access_token5, access_token_secret5)
api5= tweepy.API(auth5)

climategames5 = retrive_twitter_info.GetTwitterInfo(consumer_key5,consumer_secret5,access_token5,access_token_secret5,user5)

query = input("What do you want to tweet every bot ?")


try:
                print("Wil tweet: ")
                print(query)
                publish = input("Publish? [Y]es  to publish [N]o to pass or [E]xit to exit ")
                print(publish.lower())
                if publish.lower() == 'y':
                    climategames1.api.update_status(status=str(query))
                    climategames2.api.update_status(status=str(query))
                    climategames3.api.update_status(status=str(query))
                    climategames4.api.update_status(status=str(query))
                    climategames5.api.update_status(status=str(query))

                    print('yes')
                elif publish.lower() == 'n':
                    print('no')
                    pass
                elif publish.lower() == 'e':
                    pass
except IndexError:
                    pass


