import webbrowser
import tweepy
import urllib2
import json
import random

# INSTRUCTION: Post the tweets to the bot accounts
# INSTRUCTION: Start MAMP
# INSTRUCTION: Set chosen topics to true (minimum: 3, because need set of 9 recommendations and each bot has 3)
# INSTRUCTION: Start app via terminal
#True

binnenland = False
bizar = False
blogs = False
buitenland = True
cultuur = False
economie = False
filmtv = False
lifestyle = False
muziek = False
politiek = False
showbizz = False
sport = False
tech = True
voetbal = True
wetenschap = True


# after that show order code (0123, 0132, 0213, 0231, 0312 or 0321) so that it can be written down on their form)

showorder = ['0123', '0132', '0213', '0231', '0312', '0321']
chosenrandomshoworder = random.choice(showorder) #this is the showorder, print it on the first page, write it down during experiment and use it here
print "Jouw code:" + chosenrandomshoworder

# Get 1 random spot between 0 and 9 for the first supplemented page
spotsetone = set()
while len(spotsetone) < 1:
    spotsetone.add(random.randint(0,9))

# Get 3 random spots between 0 and 9 for the second supplemented page
spotsettwo = set()
while len(spotsettwo) < 3:
    spotsettwo.add(random.randint(0,9))
#print list(spotsettwo)[0]

# Get 5 random spots between 0 and 9 for the third supplemented page
spotsetthree = set()
while len(spotsetthree) < 5:
    spotsetthree.add(random.randint(0,9))



# Start the app:

auth = tweepy.OAuthHandler('K3wXNO0ac2Lqve2tCmJlsDvU0', 'Ut39evOnzpXCYwgvIz0NiZJIxYwuuWLrOvwFzsBIoL0Z5MPLMo')
 
# Open authorization URL in browser
webbrowser.open(auth.get_authorization_url())
 
# Ask user for verifier pin
pin = raw_input('Verification pin number from twitter.com: ').strip()
 
# Get access token
token = auth.get_access_token(verifier=pin)

auth.set_access_token(token.key, token.secret) #this should probably be replaced with user token data after his/her oauth)

api = tweepy.API(auth)

# get total list of tweets from which random tweets can be chosen for recommendation

Allembeddedtweetspossiblyused = []

# Get all the tweets from the bots

binnenland_tweets = api.user_timeline('tip_binnenland', count=3)
bizar_tweets = api.user_timeline('tip_bizar', count=3)
blogs_tweets = api.user_timeline('tip_blogs', count=3)
buitenland_tweets = api.user_timeline('tip_buitenland', count=3)
cultuur_tweets = api.user_timeline('tip_cultuur', count=3)
economie_tweets = api.user_timeline('tip_economie', count=3)
filmtv_tweets = api.user_timeline('tip_filmtv', count=3)
lifestyle_tweets = api.user_timeline('tip_lifestyle', count=3)
muziek_tweets = api.user_timeline('tip_muziek', count=3)
politiek_tweets = api.user_timeline('tip_politiek', count=3)
showbizz_tweets = api.user_timeline('tip_showbizz', count=3)
sport_tweets = api.user_timeline('tip_sport', count=3)
tech_tweets = api.user_timeline('tip_technologie', count=3)
voetbal_tweets = api.user_timeline('tip_voetbal', count=3)
wetenschap_tweets = api.user_timeline('tip_wetenschap', count=3)

# insert in list online those tweets that are of topics of interest

if binnenland == True:
    for tweet in binnenland_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        Allembeddedtweetspossiblyused.append(embedjsonstring['html'].encode('utf8'))

if bizar == True:
    for tweet in bizar_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        Allembeddedtweetspossiblyused.append(embedjsonstring['html'].encode('utf8'))

if blogs == True:
    for tweet in blogs_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        Allembeddedtweetspossiblyused.append(embedjsonstring['html'].encode('utf8'))

if buitenland == True:
    for tweet in buitenland_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        Allembeddedtweetspossiblyused.append(embedjsonstring['html'].encode('utf8'))

if cultuur == True:
    for tweet in cultuur_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        Allembeddedtweetspossiblyused.append(embedjsonstring['html'].encode('utf8'))

if economie == True:
    for tweet in economie_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        Allembeddedtweetspossiblyused.append(embedjsonstring['html'].encode('utf8'))

if filmtv == True:
    for tweet in filmtv_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        Allembeddedtweetspossiblyused.append(embedjsonstring['html'].encode('utf8'))

if lifestyle == True:
    for tweet in lifestyle_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        Allembeddedtweetspossiblyused.append(embedjsonstring['html'].encode('utf8'))

if muziek == True:
    for tweet in muziek_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        Allembeddedtweetspossiblyused.append(embedjsonstring['html'].encode('utf8'))

if politiek == True:
    for tweet in politiek_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        Allembeddedtweetspossiblyused.append(embedjsonstring['html'].encode('utf8'))

if showbizz == True:
    for tweet in showbizz_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        Allembeddedtweetspossiblyused.append(embedjsonstring['html'].encode('utf8'))

if sport == True:
    for tweet in sport_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        Allembeddedtweetspossiblyused.append(embedjsonstring['html'].encode('utf8'))

if tech == True:
    for tweet in tech_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        Allembeddedtweetspossiblyused.append(embedjsonstring['html'].encode('utf8'))

if voetbal == True:
    for tweet in voetbal_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        Allembeddedtweetspossiblyused.append(embedjsonstring['html'].encode('utf8'))

if wetenschap == True:
    for tweet in wetenschap_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        Allembeddedtweetspossiblyused.append(embedjsonstring['html'].encode('utf8'))


# get random sample of 8 from Allembeddedtweetspossiblyused
recommendationsample = random.sample(Allembeddedtweetspossiblyused, 9)


# generate FIRST page of tweets (original 10 from timeline)

f = open('embedded1.html','w')

public_tweets = api.home_timeline(count=11)
S1 = []
for tweet in public_tweets:
    embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
    embedjsonstring = json.loads(embedjson)
    S1.append(embedjsonstring['html'].encode('utf8'))

codestart = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" itemscope itemtype="http://schema.org/Blog" lang="en-US">
<head profile="http://gmpg.org/xfn/11"></head><body><center>"""
codeend = """<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script></center></body></html>"""
f.write(codestart + S1[0] + S1[1] + S1[2] + S1[3] + S1[4] + S1[5] + S1[6] + S1[7] + S1[8] + S1[9] + codeend)

f.close()

webbrowser.open('http://localhost:8888/embedded1.html')


# generate SECOND page of tweets (1 tweet switched for a recommendation)
def onereplaced():
    g = open('embedded2.html','w')

    public_tweets = api.home_timeline(count=11)
    S2 = []
    for tweet in public_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        S2.append(embedjsonstring['html'].encode('utf8'))

    S2[list(spotsettwo)[0]] = recommendationsample[0]

    codestart = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" itemscope itemtype="http://schema.org/Blog" lang="en-US">
    <head profile="http://gmpg.org/xfn/11"></head><body><center>"""
    codeend = """<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script></center></body></html>"""
    g.write(codestart + S2[0] + S2[1] + S2[2] + S2[3] + S2[4] + S2[5] + S2[6] + S2[7] + S2[8] + S2[9] + codeend)

    g.close()

    webbrowser.open('http://localhost:8888/embedded2.html')


# generate SECOND page of tweets (1 tweet switched for a recommendation)
def threereplaced():
    h = open('embedded3.html','w')

    public_tweets = api.home_timeline(count=11)
    S3 = []
    for tweet in public_tweets:
        embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
        embedjsonstring = json.loads(embedjson)
        S3.append(embedjsonstring['html'].encode('utf8'))

    S3[list(spotsettwo)[0]] = recommendationsample[1]
    S3[list(spotsettwo)[1]] = recommendationsample[2]
    S3[list(spotsettwo)[2]] = recommendationsample[3]


    codestart = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" itemscope itemtype="http://schema.org/Blog" lang="en-US">
    <head profile="http://gmpg.org/xfn/11"></head><body><center>"""
    codeend = """<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script></center></body></html>"""
    h.write(codestart + S3[0] + S3[1] + S3[2] + S3[3] + S3[4] + S3[5] + S3[6] + S3[7] + S3[8] + S3[9] + codeend)

    h.close()

    webbrowser.open('http://localhost:8888/embedded3.html')


# generate THIRD page of tweets (1 tweet switched for a recommendation)
def fivereplaced():
    k = open('embedded4.html','w')

    public_tweets = api.home_timeline(count=11)
    S4 = []
    for tweet in public_tweets:
      embedjson = urllib2.urlopen("https://api.twitter.com/1/statuses/oembed.json?id=" + str(tweet.id) + "&omit_script=true").read()
      embedjsonstring = json.loads(embedjson)
      S4.append(embedjsonstring['html'].encode('utf8'))

    S4[list(spotsetthree)[0]] = recommendationsample[4]
    S4[list(spotsetthree)[1]] = recommendationsample[5]
    S4[list(spotsetthree)[2]] = recommendationsample[6]
    S4[list(spotsetthree)[3]] = recommendationsample[7]
    S4[list(spotsetthree)[4]] = recommendationsample[8]

    codestart = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" itemscope itemtype="http://schema.org/Blog" lang="en-US">
    <head profile="http://gmpg.org/xfn/11"></head><body><center>"""
    codeend = """<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script></center></body></html>"""
    k.write(codestart + S4[0] + S4[1] + S4[2] + S4[3] + S4[4] + S4[5] + S4[6] + S4[7] + S4[8] + S4[9] + codeend)

    k.close()

    webbrowser.open('http://localhost:8888/embedded4.html')


# call pages with replaces tweets in the random order determined earlier in this document
if chosenrandomshoworder == '0123':
    onereplaced()
    threereplaced()
    fivereplaced()

if chosenrandomshoworder == '0132':
    onereplaced()
    fivereplaced()
    threereplaced()

if chosenrandomshoworder == '0213':
    threereplaced()
    onereplaced()
    fivereplaced()

if chosenrandomshoworder == '0231':
    threereplaced()
    fivereplaced()
    onereplaced()

if chosenrandomshoworder == '0312':
    fivereplaced()
    onereplaced()
    threereplaced()

if chosenrandomshoworder == '0321':
    fivereplaced()
    threereplaced()
    onereplaced()






# Documentation:

#https://dev.twitter.com/docs/embedded-tweets
#sudo pip install tweepy
#http://tweepy.readthedocs.org/en/v2.3.0/api.html

#auth = tweepy.OAuthHandler('K3wXNO0ac2Lqve2tCmJlsDvU0', 'Ut39evOnzpXCYwgvIz0NiZJIxYwuuWLrOvwFzsBIoL0Z5MPLMo')
#auth.set_access_token('2491175726-2MCRG8ivi8TvPU0nGFXWURs2x36ayYqfBzMTpMA', 'ngyjHetKNFIZRTSG8MmPUNo3KGIbDUoJoqRG625sXnr3E') #this should probably be replaced with user token data after his/her oauth)

#api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
    #print tweet.id
    #print tweet.text

#print api.user_timeline('brekendnl', count=1)

