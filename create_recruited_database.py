from peewee import *
import datetime

db=SqliteDatabase('recruited.db')

class BModel(Model):
    class Meta:
        database = db


class Recruited(BModel):
        user_id = IntegerField(primary_key=True,unique=True)
        screen_name = CharField(max_length=255, unique=True,index=True)
        description = TextField()

        class Meta:
             db_table = 'users_recruited'

class Tweets(BModel):
        #Saves the tweets that contain the hashtag that was used to recruit the user
        user_tweets = ForeignKeyField(Recruited, to_field='user_id', related_name='tweets')
        tweet_message = TextField()
        created_date = DateTimeField(default=datetime.datetime.now)

        class Meta:
             db_table = 'user_tweets'

class Hashtag(BModel):
        user_of_hashtag = ForeignKeyField(Recruited, related_name='hashtag')
        hashtag_text =TextField()

        class Meta:
             db_table = 'user_hashtag'

class SentDate(BModel):
        """
        This Class stores the sent date, and the tweet that was used to target the user
        """
        user_sent = ForeignKeyField(Tweets,  related_name='sentdate')
        #tweet_id_sent = IntegerField()
        tweet_sent_message = TextField()
        #datetime.date(1943,3, 13)  #year, month, day
        date_tweet_sent = DateTimeField(formats=['%Y-%m-%d'])

        class Meta:
             db_table = 'dates_tweets_sent'


if __name__ == '__main__':
     try:
        db.connect()
        db.create_tables([Recruited,Tweets,Hashtag,SentDate])
     except OperationalError as e:
          print('Error: ', e)