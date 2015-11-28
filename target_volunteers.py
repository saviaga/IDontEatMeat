import retrive_twitter_info

from peewee import *
from create_recruited_database import Recruited, Tweets, Hashtag, SentDate
import datetime, time


class target:
    def __init__(self, twitter, db, user):
        self.twitter = twitter
        self.db = db
        self.user = user

    def get_hashtags(self):
        # Option 1: Retrieve the tweet to send from a previously filled table in the database
        # Option 2: Create the tweet to send on the fly (easier to do)

        """
         #retrieve all the hashtags from database
        :return: the lis of the hashtags
        """
        hashtag = Hashtag.select(Hashtag.hashtag_text).distinct()
        hashtag_list = []
        for item in hashtag:
            hashtag_list.append(item.hashtag_text)

        return hashtag_list

    def show_menu(self, hashtag_list):
        """
         #shows hashtagas as menu items
        :return: nothing
        """
        count = 1;
        for item in hashtag_list:
            print("{}:{}".format(count, item))
            count += 1

    def retrieve_users(self, target_hashtag_idx, the_hashtags):
        """
         #retrieve all users that have used the selected hashtags and that have not received tweets recently (last 24 hours)
        :return: the list of selected  users
        """
        now = datetime.datetime.now()

        now = datetime.datetime.now()
        pop_user = []
        final_list = []
        print(target_hashtag_idx)
        the_target_hashtag = the_hashtags[target_hashtag_idx - 1]
        # this query gets the user_ids of those users that tweeted the selected hashtag
        users = Hashtag.select(Hashtag.user_of_hashtag).where(Hashtag.hashtag_text == the_target_hashtag)
        users_list = []
        for item in users:
            users_list.append(item.user_of_hashtag_id)
        print(users_list)
        selected_user = []
        # this query selects the datetime of the users that where retrieved with the last query (users who tweeted certain hashtag)
        for item in users_list:
            selected_user = SentDate.select(SentDate.user_sent, SentDate.date_tweet_sent, SentDate.tweet_sent_message).where(SentDate.user_sent == item)
            # if the user has been sent a tweet in the last 24 hours skip it
            print("selected users")
            for item in selected_user:
                print(item.user_sent_id)
            for item in selected_user:
                # print("printing selected user")
                # print (item.date_tweet_sent)
                # print(item.tweet_sent_message)
                # print(item.user_sent_id)

                date_retrieved = datetime.datetime.strptime(item.date_tweet_sent, '%Y-%m-%d %H:%M:%S.%f')
                print('sent', date_retrieved)
                print('48 hours', now - datetime.timedelta(hours=48))
                if (now - datetime.timedelta(hours=48)) < date_retrieved:
                    print('Not have passed 48 hours, cannot send tweet')

                    if item.user_sent_id not in pop_user:
                        pop_user.append(item.user_sent_id)

        print("user to pop: ", pop_user)
        # only keeps the users that who didn't receive a tweet in the last 48 hours
        print('user_list', users_list)
        for elem in pop_user:
            users_list = [value for value in users_list if value != elem]

        print("final list", users_list)
        return users_list

    def construct_tweet(self, list_of_users, message):
        """
        #append message to username
        :return: the constructed tweet

        """

        tweets = {}
        print(list_of_users)
        counter = 1
        print("Constructing tweets")
        for item in list_of_users:
            if counter < 25:
                string_name =twitter.get_screen_name(item)
                print(string_name)
                tweets[item]='@' + string_name + ' ' + message
                print(type(tweets))
                print(tweets[item])
                counter +=1
            else:
                break
        return tweets

    def send_tweet(self, tweets_to_send):
        """
        #just send the tweet to the list, sleep.time(15)
        #save in the data_tweets_sent:
            user_id to whom it was sent
            the tweet_id fo the tweet
            the text of the text
            the date sent (possible hour?)


        :return: nothing

        """
        for k,v in tweets_to_send.items():
            print('Mensaje a enviar: ', v)
            # tweet_only= item.split(' ')[:0]
            print("The following tweets will be sent")

            print (k , 'corresponds to', v)
            # print(tweet_only)


            twitter.api.update_status(status=v)
            time.sleep(600)
            self.save_tweet_data(k,v)
            # print "Tweeting!"

    def save_tweet_data(self, k,v):
        # Get id of the user
        list_tweets = []

        id = int(k)
        tweet_sent = v


        print('id vale', id)

        user_sent = id
        # tweet=last_tweet.split(',')[1:2]
        print("save tweet ", tweet_sent)
        tweet = self.twitter.get_user_timeline(self.user, 1)
        # tweet = twitter.api.get_user(int_id).id_str

        print(tweet_sent)

        print(user_sent)
        print(datetime.datetime.now())

        list_tweets.append({'user_sent': user_sent, 'tweet_sent_message': tweet_sent,
                            'date_tweet_sent': datetime.datetime.now()})
        for item in list_tweets:
            a = SentDate(**item)
            a.save()

    def send_tweet_to_recruited(self):
        # retrieve all the hashtags from database
        the_hashtags = self.get_hashtags()
        print(the_hashtags)
        # show menu and
        self.show_menu(the_hashtags)
        # Ask for the hashtag to target
        target = input("Which hashtag do you want to target: ")
        # get targeted hashtag
        target_hashtag_idx = int(target)
        # get list of users according to hashtag
        recruited = self.retrieve_users(target_hashtag_idx, the_hashtags)
        print('recruited', recruited)
        if  recruited:
            message = input("Write the tweet you want do send: ")
            contructed_tweet = self.construct_tweet(recruited, message)
            print(contructed_tweet)
            send = input('Are you sure you want to send them? Y=yes, N=no: ')
            if send.lower() == 'y':
                self.send_tweet(contructed_tweet)
            else:
                exit()

                # confirm send this tweet?
                # if yes: send_tweet(constructed_message returned from def constructed_message)
                # if not: cancel
        else:
            print("There are no recruiters")
            exit()

def insert_in_database(user, id_tweet, message, date):
    query_user = SentDate.create(user_sent=user, tweet_sent_message=message,
                                 date_tweet_sent=date)
    query_user.save()


user, ck, cs, at, atc = [line.rstrip('\n') for line in open('my_twitter_info.txt', 'r')]
print("the user is", user)
twitter = retrive_twitter_info.GetTwitterInfo(ck, cs, at, atc, user)
print("antes de procesar archivo")
db = SqliteDatabase('recruited.db')
db.connect()
# insert_in_database(44973121,995,"just python5",datetime.datetime.now())
new_target = target(twitter, db, user)
new_target.send_tweet_to_recruited()
