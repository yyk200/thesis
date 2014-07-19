import feedparser
import datetime
import urllib
import urllib2
import json
import operator
import tweepy

# class to store article from today
class Article:
    def __init__(self, title, link, likes):
        self.title = title
        self.link = link
        self.likes = likes

# list of the article class
article_list = [500]

# get today's date in similar format to parsed feed entries
today = datetime.date.today()
today_edited = str(today.strftime("("'%-d, %-m, %Y'")"))

# list of feeds
feed_list = []

feed_list.append("http://www.nu.nl/feeds/rss/binnenland.rss")
feed_list.append("http://www.telegraaf.nl/rss/binnenland.xml")
feed_list.append("http://www.ad.nl/nederland/rss.xml")
feed_list.append("http://www.volkskrant.nl/nieuws/binnenland/rss.xml")
feed_list.append("http://www.trouw.nl/nieuws/nederland/rss.xml")
feed_list.append("http://www.parool.nl/binnenland/rss.xml")
feed_list.append("http://feeds.feedburner.com/NRCHandelsbladBinnenland")
feed_list.append("http://www.metronieuws.nl/rss.xml?c=1277377288-3")
feed_list.append("http://www.spitsnieuws.nl/rss/binnenland/rss.xml")
feed_list.append("http://www.elsevier.nl/Service/RSS/Feed/Nederland/")
feed_list.append("http://www.nieuws.nl/rss/binnenland")
feed_list.append("http://feeds.nos.nl/nosnieuwsbinnenland?format=xml")
feed_list.append("http://www.rtlnieuws.nl/service/rss/nieuws/binnenland/index.xml")


# parse feed
for feed in feed_list:
	d = feedparser.parse(feed)

	# get entries from today
	for x in range(0, len(d['entries'])):
		date = d['entries'][x]['published_parsed']
		the_date = date.tm_mday, date.tm_mon, date.tm_year
		the_the_date = str(the_date)
		if the_the_date == today_edited:
			the_url = "http://graph.facebook.com/?id=" + d['entries'][x]['link']
			response = urllib.urlopen(the_url)
			data = json.loads(response.read())
			try:
				the_data = data['shares']
			except KeyError:
				the_data = 0
			article_list.append(Article(d['entries'][x]['title'], d['entries'][x]['link'], the_data))

# make article list sorted
article_list_sorted = [500]
article_list_sorted.append(Article(article_list[1].title, article_list[1].link, article_list[1].likes))

for x in range(2, len(article_list)):
	if article_list[x].likes < article_list_sorted[len(article_list_sorted)-1].likes:
		article_list_sorted.insert(len(article_list_sorted), Article(article_list[x].title, article_list[x].link, article_list[x].likes))
	else:
		for y in range(1, len(article_list_sorted)):
			if article_list[x].likes > article_list_sorted[y].likes:
				article_list_sorted.insert(y, Article(article_list[x].title, article_list[x].link, article_list[x].likes))
				break
			if article_list[x].likes == article_list_sorted[y].likes:
				article_list_sorted.insert(y, Article(article_list[x].title, article_list[x].link, article_list[x].likes))
				break

#print "aantal:", len(article_list)
#print "sorted aantal:", len(article_list_sorted)

#auth = tweepy.OAuthHandler('eQIbWJzoOs3xyyvaw1USNyUtT', 'pJ6OkvSTMmRALhCQiRmroZkKbxcFcEcHvh2rxrkjVHDPb8BAxK')
#auth.set_access_token('2541521450-AssZKT9SW8a0VUAsokDQzjbHCLG7k1LEbpQcyP8', 'dv1QOlHjgasiN8mqdUOvi1HD8CkLJ5rRV52wtVQxTYa56') #this should probably be replaced with user token data after his/her oauth)

#api = tweepy.API(auth)

for x in range(1, 4):
	#tweettext = article_list_sorted[x].title + " " + article_list_sorted[x].link
	#api.update_status(tweettext)
	print x, article_list_sorted[x].title, article_list_sorted[x].likes, "\n", article_list_sorted[x].link


# @tip_binnenland
