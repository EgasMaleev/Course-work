import os
import requests
from pprint import pprint
Yandex_token = 'AQAAAABM9tR2AADLW4FNSpmMiEJ8qiX2_dNy4RY'
id = 259092763
TOKEN = '4b7cac1e4ac6d9beaf0802fae2ff0c43563ff8d22b24792738be57290a5df4b64e8559fa50ec41d361586'
URL = 'https://api.vk.com/method/photos.getAll'
offset = 0
class VK_USER:
    def __init__(self, Yandex_token, id):
        self.Yandex_token = Yandex_token
        self.id = id
    def info_photo(self, URL, offset):
        params = {
            'access_token' : TOKEN,
            'owner_id' : id,
            'album_id' : 'profile',
            'count' : '1',
            'v' : '5.131',
            'extended' : '1',
            'offset' : offset
        }
        resp = requests.get(URL, params).json()['response']
        response = resp['items']
        return response
    def save_photo_album(self, offset):
        req = Egor.info_photo(URL, offset=offset)
        num = 0
        for el in req:
            # num += 1
            date = el['date']
            count = 0
            for i in el['sizes']:
                if i['type'] != 'z':
                    count += 1
                else:
                    break
            url = el['sizes'][count]['url']
            like = el['likes']['count']
            path = r'''C:\Users\Егор\Desktop\Курсовая\photo'''
            file_name = str(like) + '_' + str(date) + '.jpg'
            full_path = os.path.join(path, file_name)
            print(full_path)
            print(file_name)
            list = []
            dict = {}
            dict["filename"] = file_name
            dict["size"] = "z"
            list.append(dict)
            URL_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            params = {'url': url, 'path': file_name, 'overwrite': 'true'}
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(Yandex_token)
            }
            resp = requests.post(url=URL_upload, params=params, headers=headers)
            print(resp.json)
Egor = VK_USER(Yandex_token, id)
count_photo = 41
params = {
    'access_token': TOKEN,
    'owner_id': id,
    'album_id': 'profile',
    'count': '1',
    'v': '5.131',
    'extended': '1',
    'offset': offset
}
count_photo = requests.get(URL, params).json()['response']['count']
while offset < count_photo:
    offset += 1
    pprint(Egor.info_photo(URL, offset=offset))
    Egor.save_photo_album(offset=offset)
