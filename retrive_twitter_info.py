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

    def nfollowers(self):
        """Retrieves the number fo followers
        from the user given in the text file
         """
        nFollows = self.user.followers_count
        return  nFollows

    def get_screen_name(self,user_id):
        screen_name = self.api.get_user(user_id).screen_name
        return screen_name



    def get_user_timeline(self,the_screen_name,the_count):
        user_timeline = self.api.user_timeline(screen_name=the_screen_name, count=the_count)[0]
        return user_timeline

    def destroy_the_friendship(self,user_id):
        self.api.destroy_friendship(user_id)

    def followers_info(self):
        """Retrieves the id of my followers
        """
        ids = []
        for page in tweepy.Cursor(self.api.followers_ids,screen_name= self.screen_name).pages():
            ids.extend(page)
            time.sleep(60)
        save_to_int("array_ids.txt",ids)
        return ids

    def following_info(self):
        """Retrieves the id of the people I follow
        """
        ids = []
        for page in tweepy.Cursor(self.api.friends_ids,screen_name= self.screen_name).pages():
            ids.extend(page)
            time.sleep(60)
        print("array de following")
        print(len(ids))
        save_to_int("array_friends.txt",ids)
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
                    print(self.api.show_friendship(target_id=friend_tuple))
                    time.sleep(15)
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
                 self.api.destroy_friendship(check_friend)
                 #then save the follower id in a list
                 print(idfriend)
                 my_tuples.append(idfriend)

            # if both values are true it means WE FOLLOW EACH OTHER <3
            if me == True and check_friend == True:
                 print("WE FOLLOW EACH OTHER")
        return my_tuples



def save_to_string(filename,info):
   file= open(filename, "w" )
   for t in info:
        file.write(' '.join(str(s) for s in t) + '\n')
   file.close()


def save_to_int(filename,info):
   file= open(filename, "w" )
   for item in info:
        file.write("%s\n" % item)

   file.close()


def add_to_file(filename,info):
   file= open(filename, "a" )
   for item in info:
        file.write("%s\n" % item)

   file.close()







