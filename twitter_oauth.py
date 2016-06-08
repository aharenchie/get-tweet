#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import twitkey
import tweepy

CONSUMER_KEY = twitkey.twkey['cons_key']
CONSUMER_SECRET = twitkey.twkey['cons_sec']
ACCESS_TOKEN = twitkey.twkey['accto_key']
ACCESS_SECRET = twitkey.twkey['accto_sec']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成
api = tweepy.API(auth)

# これだけで、Twitter APIをPythonから操作するための準備は完了。
print('Done!')

print(api.home_timeline()[0].text)
