count = 0
import os
import requests
from pprint import pprint
Yandex_token = 'AQAAAABM9tR2AADLW4FNSpmMiEJ8qiX2_dNy4RY'
id = 403142107
TOKEN = 'd82c00e5a40f505a9c1c30d04487eb7b42fbdf7e94aaa0a014ed4dcdd23acac2cf809f65bd9edfc1e1463'
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
            'count' : '3',
            'v' : '5.131',
            'extended' : '1'
        }
        response = requests.get(URL, params).json()['response']['items']
        return response
    def chislo_laikov(self, id):
        URL = 'https://api.vk.com/method/photos.getById'
        dict = {
            'id': id,
            'owner_id': 403142107
        }
        photo = str(dict['owner_id']) + '_' + str(dict['id'])
        params = {
            'access_token': TOKEN,
            'photos': photo,
            'extended': 1,
            'v': '5.131'
        }
        response = requests.get(URL, params).json()['response'][0]['likes']['count']

        return response
    def save_photo_album(self):
        req = Egor.info_photo(URL)
        for el in req:
            # id = el['id']
            url = el['sizes'][0]['url']
            like = el['likes']['count']
            path = r'''C:\Users\Егор\Desktop\Курсовая\photo'''
            file_name = str(like) + '.jpg'
            full_path = os.path.join(path, file_name)
            print(full_path)
            img_data = requests.get(url).content
            with open(full_path, 'wb') as file:
                file.write(img_data)
Egor = VK_USER(Yandex_token, id)
pprint(Egor.info_photo(URL))
Egor.save_photo_album()