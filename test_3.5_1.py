import requests
import sys

client_id = '4a52526982b8f42d9ab9'
client_secret = '8e2d8b78c247c57869e9dc8e3b342a88'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
token_data = r.json()

# достаем токен
token = token_data["token"]
# print(token)
headers = {"X-Xapp-Token" : token}

# artists = [{'sortable_name': 'Worhol Andy', 'birthday': '1928'}, {'sortable_name': 'Warhol Andy', 'birthday': '1928'}, {'sortable_name': 'Abbas Hamra', 'birthday': '1976'}, {'sortable_name': 'Abbott Mary', 'birthday': '1921'}]
artists = []

for line in sys.stdin:
    line = line.rstrip()
    # print('====', line)
    if line == '':
        break
    # инициируем запрос с заголовком
    r = requests.get("https://api.artsy.net/api/artists/{artist_id}".format(artist_id=line), headers=headers)
    data = r.json()
    # print('data ====', data)
    artists.append({'sortable_name': data['sortable_name'], 'birthday': data['birthday']})

artists = sorted(artists, key=lambda d: (d['birthday'], d['sortable_name']))

for artist in artists:
    print(artist['sortable_name'])

