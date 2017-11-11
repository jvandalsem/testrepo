import requests
import json

base_url = 'https://api.groupme.com/v3/groups?'
access_token = 'TpDu7j5zAATwDnG3VKQhtzncLa3tIslt9CLmlv7R'
redirect_url = 'https://oauth.groupme.com/oauth/authorize?client_id=uPYMyaugJ4c9BZWs7e8VExWoUCxWwDQvbonAfG0f73NnBfdF'
params = {'token': access_token, 'id': 25481406}

# text_filename = 'groupme.json'
# f = open(text_filename, 'r')
# f_str = f.read()

j = requests.get(base_url, params).json()
print(j)
for a in j:
    print('\n')
    print('\n')
    print('\n')
    print(a)
