import retrive_twitter_info
import tweepy
from peewee import *
from create_recruited_database import Recruited,Tweets,Hashtag


class recruit:
    def __init__(self,twitter,db):
        self.twitter = twitter
        self.db = db

    def search_and_save_users(self):
        language = 'en'
        #use the lines below if you want to target another language besides english
        #language = input("Which language do you want to target 'es'espanish, 'en'english: ")
        #language = language.lower()

        query = input("Which words do you want to search ?")

        max_tweets = int(input("How many tweets do you want to retrieve? "))
        searched_tweets = [status for status in tweepy.Cursor(twitter.api.search, q=query, lang=language).items(max_tweets)]


        list_user=[]
        list_hashtag=[]
        list_tweets =[]
        print('users found saved to the database: ')
        for elem in searched_tweets:
            #print(elem.user.screen_name)
            #print(elem.user.id)
            #print(elem.user.description)
            #print(elem.text)
            #print(elem.created_at)
            #print(query)
            list_user.append({'user_id':elem.user.id,'screen_name':elem.user.screen_name,'description':elem.user.description})
            list_hashtag.append({'user_of_hashtag':elem.user.id,'hashtag_text':query})
            list_tweets.append({'user_tweets':elem.user.id,'tweet_message':elem.text,'created_date':elem.created_at})
            print(elem.user.id)


        for itemr,itemh,itemt in zip(list_user,list_hashtag,list_tweets):
            try:

                #The following is the same as the short version Recruited.create(**itemr)
                #a= Recruited.create(user_id = itemr['user_id'],screen_name = itemr['screen_name'],description=itemr['description'])
                a = Recruited.create(**itemr)
                b = Hashtag.create(**itemh)
                c = Tweets.create(**itemt)
                a.save()
                b.save()
                c.save()
            except IntegrityError:
                pass

        return list_user






user,ck,cs,at,atc = [line.rstrip('\n') for line in open('my_twitter_info.txt','r')]
twitter = retrive_twitter_info.GetTwitterInfo(ck,cs,at,atc,user)
print("antes de procesar archivo")
db=SqliteDatabase('recruited.db')
db.connect()
new_recruit = recruit(twitter,db)
list_recruited=new_recruit.search_and_save_users()
#print(list(list_recruited))


