import twint

c = twint.Config()
c.Debug = True
c.Proxy_host = "tor"
# c.Proxy_port = 7890
# c.Proxy_type = "http"
c.Username = "Coinlist"
# c.Index_tweets = "demo_tweets"
# c.Index_follow = "demo_follow"
# c.Index_users = 'demo_users'
# c.Elasticsearch = "http://localhost:9200"
# c.Search = ""
c.Limit = 20
# c.Popular_tweets = True
c.Return = True
# c.TranslateDest = 'zh-CN'
# c.TranslateDest = 'zh-CN'
c.Tweets = []
print(c.TwitterSearch)
tweets1 = twint.run.Search(c)
print(c.TwitterSearch)


# c.Username = "GeromanAT"
# tweets2 = twint.run.Search(c)
# c.Username = "DiMartinoBooth"
# tweets3 = twint.run.Search(c)
# c.Username = "ttmygh"
# tweets4 = twint.run.Search(c)
# print(len(tweets))
# for tweet in tweets:
#     print(tweet.__dict__)