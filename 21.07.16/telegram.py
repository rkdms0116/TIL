import requests
from pprint import pprint
from decouple import config

TOKEN = '1600774904:AAEA3Jm3VcrgNEZwZv2BAy9I8ZGOTCcBhSQ'
url = f'https://api.telegram.org/bot{TOKEN}'

update_url = f'{url}/getUpdates'
res = requests.get(update_url).json()
# pprint(res)

# CHAT_ID = '1773362486'
CHAT_ID = res['result'][0]['message']['chat']['id']
text = '대전 2반 화이팅! :)'

message_url = f'{url}/sendMessage?chat_id={CHAT_ID}&text={text}'
print(requests.get(message_url))