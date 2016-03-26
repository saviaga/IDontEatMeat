import tweepy
import time


class GetTwitterInfo:
    def __init__(self, consumer_key, consumer_secret, access_token,access_token_secret,screen_name):

        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)
        self.screen_name = screen_name
        self.user = self.api.get_user(self.screen_name)



    def get_stream(self,StdOutListener):
        l= StdOutListener()
        self.stream = tweepy.Stream(self.auth,l)


    def nfollowers(self):
        """Retrieves the number fo followers
        from the user given in the text file
         """
        nFollows = self.user.followers_count
        return  nFollows

    def get_user_id(self):
        return int(self.user.id_str)

    def get_screen_name(self,user_id):
        screen_name = self.api.get_user(user_id).screen_name
        return screen_name

    def creates_frienship(self,follow_id):
        self.api.create_friendship(follow_id)


    def get_user_ratio(self,screen_name):
        followers = self.api.followers_ids(screen_name)
        friends = self.api.friends_ids(screen_name)
        try:
            ratio = len(followers)/len(friends)
        except ZeroDivisionError:
            ratio = 0

        return ratio

    def get_user_timeline(self,the_screen_name,the_count):
        user_timeline = self.api.user_timeline(screen_name=the_screen_name, count=the_count)[0]
        return user_timeline

    def destroy_the_friendship(self,user_id):
        self.api.destroy_friendship(user_id)

    def create_block(self,user_id):
        self.api.create_block(user_id)


    def followers_info(self,username):
        """Retrieves the id of my followers
        """
        print("getting the followers_info from: ", username)
        ids = []
        for page in tweepy.Cursor(self.api.followers_ids,screen_name= username,count=5000).pages():

            ids.extend(page)
            time.sleep(150)
        print("done getting users")
        #names= self.print_names(ids )
        save_to_int("followers.txt",ids)
        #save_to_int("followers.txt",names)
        #return names
        return ids



    def print_names(self,ids):
        names = []
        for item in ids:
            names.append(self.get_screen_name(item))
            print (item)
            time.sleep(10)
        return names

    def following_info(self):
        """Retrieves the id of the people I follow
        """
        ids = []
        print("antes del for")
        for page in tweepy.Cursor(self.api.friends_ids,screen_name= self.screen_name).pages():
            ids.extend(page)
            #time.sleep(60)
            print("array de following")
        print(len(ids))
        save_to_int("followers.txt",ids)
        return ids



    def user_location(self):
        """Retrieves the location of the follower
        as seen on twitter profile
        """
        location = self.user.location
        return location

    def is_my_friend(self,ids):
        """Retrieves a tuple with the information of me and the information
        of the ids given as a parameter. This to be later used to check if
        both are following each other or not
        """
        list_friend_relations=[]
        #counter = 0
        #friend = self.api.show_friendship(target_id=ids[1])
        for friend_tuple in ids:
            #if counter < 200:
                try:
                    #print("number of item",counter)
                    list_friend_relations.append(self.api.show_friendship(target_id=friend_tuple))
                    #print(self.api.show_friendship(target_id=friend_tuple))
                    #time.sleep(15)
                    #counter +=1

                #else:
                #    break
                except tweepy.TweepError as e:
                    print("got and error", e)
                    break
        save_to_string("info_tuples.txt",list(list_friend_relations))
        return list_friend_relations


    def review_frienship(self,dfriendship):
        """Recieves a tuple with my information and the followers/following info
        then it checks the status of the parameters in the tuple that indicate the existence
        of a relationship (following parameter)
        if both are true means we are following each other, not true one of us is not following the other

        What it needs to be programmed:
        Ok if i am following someone that is not following back, then i need so save that id in a list
        Return and the list of ids

        """
        my_tuples=[]

        for tuples in dfriendship:
            # The first return data is me

            me = tuples[0].following
            idme=tuples[0].id
            # The second return data is a follower
            check_friend = tuples[1].following

            idfriend=tuples[1].id
            #print(tuples[1].id)


            # if both are different it means there is no relationship
            # if first is False & second is True it means he follows me but i do not follow back
            if me == False and check_friend == True:
                print("Follows me but I DO NOT follow back ")
            # if first is True & second is False it means I follow him but he does not follow me back
            if me == True and check_friend == False:
                 print("I Follows him but HE DOES NOT follow back ")
                 print("check_friend: ",check_friend)
                 self.api.destroy_friendship(check_friend)
                 #then save the follower id in a list
                 print(self.get_screen_name(idfriend))
                 my_tuples.append(idfriend)

            # if both values are true it means WE FOLLOW EACH OTHER <3
            if me == True and check_friend == True:
                 print("WE FOLLOW EACH OTHER")
        return my_tuples

    def unfollow(self):
        followers = self.api.followers_ids(self.screen_name)
        friends = self.api.friends_ids(self.screen_name)
        print(friends)
        for f in friends:
            print("next: ",f)
            if f not in followers:
                #print ("Unfollow {0}?".format(self.api.get_user(f).screen_name))
                #if raw_input("Y/N?") == 'y' or 'Y':
                    self.api.destroy_friendship(f)
                    print("unfollowed: ",f)
                    time.sleep(5)

    def search_and_save_tweets(self,query,max_tweets,lang):

        searched_tweets = [status for status in tweepy.Cursor(self.api.search, q=query, lang=lang).items(int(max_tweets))]
        #print(searched_tweets)
        output = open('searchtweets3.txt', 'w')
        dict={}

        for elem in searched_tweets:
            dict[str(elem.text.encode("utf-8"))]= elem.favorite_count

        sorted_x = sorted( ((v,k) for k,v in dict.items()), reverse=True)

        for k, v in sorted_x:
            output.write(str(k) + '***' + str(v) + '\n')
            #print(str(k) + ',' + str(v) + '\n')

        output.close()
        return searched_tweets

    def publish_tweet(self):
        #Read from file only if tweet has more than 2 favorites
        archivo = open('searchtweets3.txt', 'r')
        for line in archivo:
            x = line.split("***")
            try:
                print("Most favorite tweet ")
                print(x[1])
                publish = input("Publish? [Y]es  to publish [N]o to pass or [E]xit to exit ")
                print(publish.lower())
                if publish.lower() == 'y':
                    self.api.update_status(status=str(x[1]))
                    print('yes')
                elif publish.lower() == 'n':
                    print('no')
                    pass
                elif publish.lower() == 'e':
                    break
            except IndexError:
                    pass
        archivo.close()



def save_to_string(filename,info):

   print("I am writing to file")
   file= open(filename, "w" )
   for t in info:

        file.write(' '.join(str(s) for s in t) + '\n')
   file.close()


def save_to_int(filename,info):
   file= open(filename, "w" )
   for item in info:
        file.write(str(item) + '\n')

   file.close()


def add_to_file(filename,info):
   print("los followers antes de guardar: ",info)
   file= open(filename, "a" )
   for item in info:
        file.write("%s\n" % item)

   file.close()
