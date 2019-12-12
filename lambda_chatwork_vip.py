import requests

import base64
import hashlib
import hmac
import json
import os

def lambda_handler(event, context):
    #  署名検証
    secret_key = base64.b64decode(os.environ['CW_HOOK_TOKEN'])
    digest = hmac.new(secret_key, event['body'].encode('utf-8'), hashlib.sha256).digest()
    signature = base64.b64encode(digest)
    if signature != event['headers']['X-ChatWorkWebhookSignature'].encode():
        print(f'signature error')
        return {
            'statusCode': 403,
            'body': 'forbidden'
        }

    #  匿名チャンネルへ投稿
    url = f"https://api.chatwork.com/v2/rooms/{os.environ['ROOM_ID']}/messages"
    headers = {'X-ChatWorkToken': os.environ['CW_API_KEY']}
    content = json.loads(event['body'])  # bodyは文字列で来ていた
    content = content['webhook_event']['body']
    params = {'body': f'{content}'}
    res = requests.post(url, data=params, headers=headers)
    return {
        'statusCode': res.status_code,
        'body': 'posted'
    }
