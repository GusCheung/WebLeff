import json
import requests
import datetime

import hashlib

import time
import hmac
import base64
import urllib.parse

curr_time = datetime.datetime.now()
H = curr_time.hour  # 14 <class 'int'>

data = {
    "feedCard": {
        "links": [
            {
                "title": "时代的火车向前开",
                "messageURL": "https://www.dingtalk.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI",
                "picURL": "https://gw.alicdn.com/tfs/TB1ayl9mpYqK1RjSZLeXXbXppXa-170-62.png"
            },
            {
                "title": "时代的火车向前开2",
                "messageURL": "https://www.dingtalk.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI",
                "picURL": "https://gw.alicdn.com/tfs/TB1ayl9mpYqK1RjSZLeXXbXppXa-170-62.png"
            }
        ]
    },
    "msgtype": "feedCard"
}

timestamp = str(round(time.time() * 1000))
url = 'https://oapi.dingtalk.com/robot/send?access_token=af874f67ddc1aceb4817ec3f971d39342cdadbcbffb4bc4438a7f6810a71ab42'
secret = 'SECfc4501f7b0dc0a0b203a273f90a29f20e8fdf7d34cd3ed3b1e30e99819304907'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
url = url + '&' + timestamp
url = url.encode('utf-8')
r = requests.post(url, json=data)
print(r)
