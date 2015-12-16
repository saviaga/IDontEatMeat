import tweepy

robotTweeter={}
robotTweeter["baselineBot"]={}
robotTweeter["socialBot"]={}
robotTweeter["solidarityBot"]={}
robotTweeter["contributionsBot"]={}
robotTweeter["mia"]={}
robotTweeter["mia2"]={}
 
robotTweeter["baselineBot"]["CONSUMER_KEY"]='HIr71lwjU7VqbVKx5oR6wzcKj'
robotTweeter["baselineBot"]["CONSUMER_SECRET"]='Jik9frU5envkzUBqZgiWqp2CDQC2Z8arlEltTzpP80l0gK3fG2'
robotTweeter["baselineBot"]["ACCESS_KEY"]='2915861004-jVKShRpvSYXODoVYcNb7xHzo7UADLIiNFdd6HX4'
robotTweeter["baselineBot"]["ACCESS_SECRET"]='ttGK3zdYwcKpycGWxsoLknU95i4SVkJFCiJlRTLQQVfyl'
 
robotTweeter["socialBot"]["CONSUMER_KEY"]='xoaRLRds3jsPKA8fICaSzVw0T'
robotTweeter["socialBot"]["CONSUMER_SECRET"]='c23zJM1L4ppXa460DRQlSoFO6P3itD5y7etQ91wSdiajGP0nux'
robotTweeter["socialBot"]["ACCESS_KEY"]='2915873316-FoinglKj3I38dRRuqEqpq1N9FBtyJihrZMZ72JS'
robotTweeter["socialBot"]["ACCESS_SECRET"]='wwxbs4LyYiRpP4SMOfXjGO8V8vQ4Lk4gA5jm40hBMzmbH'
 
robotTweeter["solidarityBot"]["CONSUMER_KEY"]='W8jr4fmfqQ4oCjljUMlRpiscX'
robotTweeter["solidarityBot"]["CONSUMER_SECRET"]='9a4aIRXfyquVuqVZQHAQn4tIl19CR2iJg4oMEYEn5950DODTZC'
robotTweeter["solidarityBot"]["ACCESS_KEY"]='2915892522-edXtQEFX0UNJfOpLrjDhnT2BLC1zx80bP14l3If'
robotTweeter["solidarityBot"]["ACCESS_SECRET"]='5qQSucB05klO8Aopi1XqDeDe0oRPmSW30WA8psinYC54E'
 
robotTweeter["contributionsBot"]["CONSUMER_KEY"]='Odl8rsmcH5LQIALruswsRK0gg'
robotTweeter["contributionsBot"]["CONSUMER_SECRET"]='X6SS2yKXjWTWXfwPaPl3VHeLP1XmaPcG73iR5MIK1kstUK8Aju'
robotTweeter["contributionsBot"]["ACCESS_KEY"]='2917970107-1qsZgchKgSxF2Aeb0JhdACfMftF5vKyrmb99MAd'
robotTweeter["contributionsBot"]["ACCESS_SECRET"]='kulTWJO71eusERnJNRc7o7uDxo00xgknKZrLmKNl3wnP0'
 
robotTweeter["mia"]["CONSUMER_KEY"]='OI0fpK83czqr6iVZxzCmVBfmX'
robotTweeter["mia"]["CONSUMER_SECRET"]='PxeIB9sJfusyBh1aaSncAyy6M881WkNuoTIa22MpTXMlxoir5n'
robotTweeter["mia"]["ACCESS_KEY"]='16507835-6CQyfynMhr73uS005HR3UqAaLmCvhwN6a2lCOxG5B'
robotTweeter["mia"]["ACCESS_SECRET"]='LyhsFBWSvkJHEZVtcwpolRO1b1P7ZmTolUnERcYlZBdJZ'

def prepareLoginData(botname="baselineBot"):
    print "ALMOST"
    robot=robotTweeter[botname]
     
    CONSUMER_KEY =robot["CONSUMER_KEY"]
    CONSUMER_SECRET =robot["CONSUMER_SECRET"]#keep the quotes, replace this with your consumer secret key
    ACCESS_KEY =robot["ACCESS_KEY"]#keep the quotes, replace this with your access token
    ACCESS_SECRET =robot["ACCESS_SECRET"]#keep the quotes, replace this with your access token secret
     
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

    prepareLoginData()