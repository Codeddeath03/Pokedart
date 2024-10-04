import requests
import os
from dotenv import load_dotenv
load_dotenv()

token = os.environ['token']
APP_ID = "671706523541569546"
SERVER_ID = "1142473459843215441"
BOT_TOKEN = token

# global commands are cached and only update every hour
# url = f'https://discord.com/api/v10/applications/{APP_ID}/commands'

# while server commands update instantly
# they're much better for testing
url = f'https://discord.com/api/v10/applications/{APP_ID}/guilds/{SERVER_ID}/commands'

json = [
  {
    'name': 'help',
    'description': 'List most of the commands',
  },
  {
    'name': 'balance',
    'description': 'To check your owned credits',
  },
  {
    'name': 'redeem',
    'description': 'To check your redeems',
  },

]

response = requests.put(url, headers={
  'Authorization': f'Bot {BOT_TOKEN}'
}, json=json)

print(response.json())