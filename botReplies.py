import tweepy
import pickle

global repliesBot



def menu():
    bot_used = int(input("Which bot do you want to use? [1]cg1, [2],cg2, [3]cg3,[4]cg4,[5]cg5 : "))
    print("bot used",bot_used)
    if bot_used == 1:
            botName="climate1Bot"
    elif bot_used == 2:
            botName="climate2Bot"
    elif bot_used == 3:
            botName="climate3Bot"
    elif bot_used == 4:
            botName="climate4Bot"
    elif bot_used == 5:
            botName="climate5Bot"
    return botName


def authenticate(botName):
    consumer_key=robotTweeter[botName]["CONSUMER_KEY"]
    consumer_secret=robotTweeter[botName]["CONSUMER_SECRET"]
    access_token=robotTweeter[botName]["ACCESS_KEY"]
    access_token_secret=robotTweeter[botName]["ACCESS_SECRET"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    l = StdOutListener()
    stream = tweepy.Stream(auth,l)
    return stream

class StdOutListener(tweepy.StreamListener):

    def on_status(self, status):
        try :


            global repliesBot
            print ("all good")
            #Extract info of the incomming message
            date,status,screen_name,message,idTweet,names,hashNames=prepareDataIncomingMessage(status)
            api.create_favorite(idTweet)
            #api.retweet(idTweet)

            print (message)
            print ("SCREEN NAME:"+str(screen_name))
            print ("WORDFILTER:"+str(wordToFilter))

            if not screen_name in wordToFilter.lower():
                if not screen_name in nombresTodosBots:
                    print ("entered if of screenname")
                    print ("think of all the things")

                    print ("IT'S A Statement")
                    print (hashNames)
                    r2=getRandomMessage(hashNames)

                    print ("got to reply")
                    print ("Names:"+str(len(names)))
                    print("r2: ",r2)
                    print("screen_name: ",screen_name)
                    print("idTweet: ",idTweet)
                    print("names: ",names)
                    print("hashnames: ",hashNames)
                    twitterMessage=outputTweet(r2,screen_name,idTweet,names,hashNames)
                    currentMesageBot=twitterMessage
                    print("antes del set default")
                    messagesBotWithReplies.setdefault(currentMesageBot,{})
                    print(messagesBotWithReplies[currentMesageBot].setdefault(hashNames,None))
                    print("after setdefault")
                    key = str(idTweet)
                    messagesBotWithReplies[currentMesageBot][hashNames]=(key + ':' + currentMesageBot)
                    #messagesBotWithReplies.update({key:message})

                    print ("Mi Mensaje:"+r2)

                    pickle.dump(messagesBotWithReplies, open(storingDirectory+"messagesBotWithReplies_"+botName+"_"+currentCause+"_"+str(currentTestNumber)+".p", "wb" ) )

        except Exception as e:
            print ("EXCEPTION :(", e)
            #pass
          
    def on_error(self, status):
        
        print ("EERROR"+str(status))
    


def prepareRepliesBot():
	global repliesBot
	repliesBot=[]
	repliesBot.append("Great! Let's keep going! Show world how you fight climate change with friends use #ParisClimateFight")
	repliesBot.append("Awesome! Let's post now photos of how we fight climate change at work! use #ParisClimateFight")
	repliesBot.append("Could you share now a photo showing how you fight climate change at home? use #ParisClimateFight")
	repliesBot.append("Great! Let's keep going! Show world how you fight climate change with friends use #ParisClimateFight")
	repliesBot.append("Cool! Let's post now photos of how  fun fighting climate change can be! Use #ParisClimateFight")
	repliesBot.append("Neat! Let's all post photos of how we fight climate change in our cities! Use #ParisClimateFight")
	repliesBot.append("Neat! Let's all post photos of how we fight climate change in our daily lives! Use #ParisClimateFight")
	repliesBot.append("Neat! Let's bring awareness to #ParisClimateFight share massively your photos using the hashtag!")
	repliesBot.append("Cool! Let's bring awareness to #ParisClimateFight share massively how you fight climate change, use the hashtag!")

prepareRepliesBot()
botName=menu()
print(botName)
stream=authenticate(botName)
#storingDirectory="frasesclimate1Bot/"
	

	