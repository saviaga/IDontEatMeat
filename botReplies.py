import tweepy
import pickle
import datetime
import time
from time import gmtime, strftime
import random

global repliesBot
#FirstRun
#messagesBotWithReplies={}
#humanReplies={}

#SecondRuns!
messagesBotWithReplies=pickle.load(open(storingDirectory+"messagesBotWithReplies_"+botName+".p","rb"))
humanReplies=pickle.load(open(storingDirectory+"humanReplies_"+botName+".p","rb"))


botNamesWordsFilter={}
botNamesWordsFilter["climate1Bot"]="climategames1"
botNamesWordsFilter["climate2Bot"]="climategames2"
botNamesWordsFilter["climate3Bot"]="climategames3"
botNamesWordsFilter["climate4Bot"]="climategames4"
botNamesWordsFilter["climate5Bot"]="climategames5"

#nombresTodosBots={}
#nombresTodosBots["climate1Bot"]=0
#nombresTodosBots["climate2Bot"]=0
#nombresTodosBots["climate3Bot"]=0
#nombresTodosBots["climate4Bot"]=0
#nombresTodosBots["climate5Bot"]=0


robotTweeter={}
robotTweeter["climate1Bot"]={}
robotTweeter["climate2Bot"]={}
robotTweeter["climate3Bot"]={}
robotTweeter["climate4Bot"]={}
robotTweeter["climate5Bot"]={}

nameBots={}
nameBots["climategames1"]=0
nameBots["climategames2"]=0
nameBots["climategames3"]=0
nameBots["climategames4"]=0
nameBots["climategames5"]=0
#nameBots.append("climategames1")








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

def getPeopleMentionedTweet(message):
    '''

    :param message: get the received tweet in which the bot was mentioned
    :return: the username of the people mentioned on the tweet including the bots username
    '''
    words=message.split()
    names={}
    for w in words:
        w=w.lower()
        if "@" in w:
            
            if not wordToFilter.lower() in w:
                if not "climategames1" in w:
                    print ("Name detected:"+w)
                    w=w.lower()
                    names[w]=0
    for n in names:
        print ("Nombre:"+n+">>>>")
    return names


def prepareDataIncomingMessage(status):
    '''
    reads the tweet in which the bot was mentioned
    :param status:  is the tweet received
    :return: all the information retrieved from the message separated as variables
    '''
    print ("entre prepareData")
    year=strftime("%Y", gmtime())
    month=strftime("%m", gmtime())
    day=strftime("%d", gmtime())
    hour=strftime("%H", gmtime())
    minute=strftime("%M", gmtime())
    sec=strftime("%S", gmtime())
            
    date= datetime.datetime(int(year),int(month),int(day),int(hour),int(minute),int(sec) )
    status.created_at = date
    screen_name=status.user.screen_name
    screen_name=screen_name.lower()
    message=status.text
    idTweet=status.id_str
    #get the people mentioned in the tweet and adds the @ symbol
    names=getPeopleMentionedTweet(message)
    names["@"+screen_name]=0
    print ("ScreenNameEE:"+screen_name)
    print ("Message:"+message)

    #hashNames=getHashNames(names)
    return date,status,screen_name,message,idTweet,names



def getRandomMessage():
    global repliesBot
    print("'im in get random message3")
    listreplybots = list(repliesBot)
    print(type(listreplybots))
    r=random.choice(listreplybots)

    print("random choice: ",r)
    return r


def setNumberOfNames(tweet,names):
    newTweet=tweet
    nombresNoAgregados={}
    for n in names:
        print ("Name:")
        print (n)
        newPossibleTweet=n+" "+newTweet
        if len(newPossibleTweet)<140:

            newTweet=n+" "+newTweet
            print ("parece bien el tweet!"+newTweet)
        
        else:
            print ("Muy grande tweet:"+str(len(newPossibleTweet)))
            nombresNoAgregados[n]=0
    print ("este es el tweet final numNombres:"+newTweet)
    return newTweet, nombresNoAgregados



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

def outputTweet(canResponse,screen_name,idTweet,names):
    tweet=canResponse
    if len(tweet)<140:
        print ("creating tweet!")
        print("output screen_name:",screen_name)
        print("output idtweet: ", idTweet)
        print("output names: ",names)
        print ("after store info")
        newTweet, nombresNoAgregados=setNumberOfNames(tweet, names)
        print ("Tweet Carved:"+newTweet)
        print ("IDTweet:"+str(idTweet))
        api.update_status(status=newTweet)
        #api.update_status(newTweet, int(idTweet))
        #api.update_status(newTweet)
        sleepTime=random.randrange(80,200)
        print(sleepTime)
        time.sleep(sleepTime)
        print ("finished tweeting!")
        print ("This is the tweet:"+newTweet)
        return newTweet

class StdOutListener(tweepy.StreamListener):
    global nameBots
    global botName
    global humanReplies
    def on_status(self, status):
        try :


            global repliesBot
            global messagesBotWithReplies
            print ("all good")
            storingDirectory="pickle/"
            #Extract info of the incomming message
            date,status,screen_name,message,idTweet,names=prepareDataIncomingMessage(status)
            api.create_favorite(idTweet)
            
            humanReplies.setdefault(screen_name,{})
            humanReplies[screen_name][idTweet]=message
            print (message)
            print ("SCREEN NAME:"+str(screen_name))
            print ("WORDFILTER:"+str(wordToFilter))

            if not screen_name in wordToFilter.lower():
                if not screen_name in nameBots:
                    r2=getRandomMessage()
                    print r2
                    twitterMessage=outputTweet(r2,screen_name,idTweet,names)
                    currentMesageBot=twitterMessage
                    messagesBotWithReplies.setdefault(currentMesageBot,[])
                    key = str(idTweet)
                    messagesBotWithReplies[currentMesageBot].append(key)
                    pickle.dump(messagesBotWithReplies, open("messagesBotWithReplies_"+botName+".p", "wb" ) )
                    pickle.dump(humanReplies, open("humanReplies_"+botName+".p", "wb" ) )
                    


             #       print ("entered if of screenname")
              #      print ("think of all the things")

               #     print ("IT'S A Statement")
                #    print (hashNames)
                 #   r2=getRandomMessage(hashNames)

                  #  print ("got to reply")
                   # print ("Names:"+str(len(names)))
                   # print("r2: ",r2)
                   # print("screen_name: ",screen_name)
                   # print("idTweet: ",idTweet)
                   # print("names: ",names)
                   # print("hashnames: ",hashNames)
                   #twitterMessage=outputTweet(r2,screen_name,idTweet,names,hashNames)
                   # currentMesageBot=twitterMessage
                   # print("antes del set default")
                   # messagesBotWithReplies.setdefault(currentMesageBot,{})
                   # print(messagesBotWithReplies[currentMesageBot].setdefault(hashNames,None))
                   # print("after setdefault")
                   # key = str(idTweet)
                   # messagesBotWithReplies[currentMesageBot][hashNames]=(key + ':' + currentMesageBot)
                    

                   # print ("Mi Mensaje:"+r2)

                    #pickle.dump(messagesBotWithReplies, open(storingDirectory+"messagesBotWithReplies_"+botName+"_"+currentCause+"_"+str(currentTestNumber)+".p", "wb" ) )

        except Exception as e:
            print ("EXCEPTION :(", e)
            
          
    def on_error(self, status):
        
        print ("EERROR"+str(status))
    
def prepareLoginData(botname):
    '''
    Autentica al Bot con las credenciales que obtiene de infobotsclimates.py
    :param botname: nombre del bot
    :return: api autenticada
    '''
    print ("Prepared Login Data")
    robot=robotTweeter[botname]
    CONSUMER_KEY =robot["CONSUMER_KEY"]
    CONSUMER_SECRET =robot["CONSUMER_SECRET"]#keep the quotes, replace this with your consumer secret key
    ACCESS_KEY =robot["ACCESS_KEY"]#keep the quotes, replace this with your access token
    ACCESS_SECRET =robot["ACCESS_SECRET"]#keep the quotes, replace this with your access token secret
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api


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
    #return repliesBot
    #return repliesBot


prepareRepliesBot()
global repliesBot
botName=menu()
print(botName)
stream=authenticate(botName)
wordToFilter=botNamesWordsFilter[botName]
print "Words to Filter:"+str(wordToFilter)
api=prepareLoginData(botName)
stream.filter(track=[wordToFilter])
#for i in nameBots:
#    print i
#storingDirectory="frasesclimate1Bot/"

#Present menu to choose bot
 #   botName=menu()
  #  print(botName)
   # storingDirectory="frasesclimate1Bot/"
    #Authenticate the chosen bot
    #stream=authenticate(botName)
    #take out the reply messages from the file
    #repliesBot=pickle.load(open("replies_climate1Bot.p","rb"))
    #load the pickle where the reply info is being stored
    #file= pickle.load(open(storingDirectory+"messagesBotWithReplies_"+botName+"_"+currentCause+"_"+str(currentTestNumber)+".p","rb"))
    #miDict = pickle.load(open("dictTest.p", "rb"))
    #print("Original")
    #for i in miDict:
     #   print (i)
    #define the word to filter (the bot chosen)
   # wordToFilter=botNamesWordsFilter[botName]
    #load the replies from file
    #setRepliesBot(storingDirectory,botName)
    #print (botName)
    #print (wordToFilter)
    #api=prepareLoginData(botName)


    #stream.filter(track=[wordToFilter])
    #file.close()

	

	