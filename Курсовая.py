import os
import requests
from pprint import pprint
Yandex_token = 'AQAAAABM9tR2AADLW4FNSpmMiEJ8qiX2_dNy4RY'
id = 259092763
TOKEN = '07c27c4e128c04e197448f1a8c2a043813f9e8b58f2d67bd525a0ea8eee16149874cc01772df62097d39b'
URL = 'https://api.vk.com/method/photos.getAll'
class VK_USER:
    def __init__(self, Yandex_token, id):
        self.Yandex_token = Yandex_token
        self.id = id
    def info_photo(self, URL):
        params = {
            'access_token' : TOKEN,
            'owner_id' : id,
            'album_id' : 'profile',
            'count' : '10',
            'v' : '5.131',
            'extended' : '1',
            # 'offset' : offset
        }
        resp = requests.get(URL, params).json()['response']
        count_photo = resp['count']
        response = resp['items']
        return response
    def save_photo_album(self):
        req = Egor.info_photo(URL)
        # num = 0
        for el in req:
            # num += 1
            # if num == 200:
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
pprint(Egor.info_photo(URL))
Egor.save_photo_album()