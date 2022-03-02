import requests
Yandex_token = 'AQAAAABM9tR2AADLW4FNSpmMiEJ8qiX2_dNy4RY'
id = 259092763
TOKEN = 'e2e665ca9b8d33cc060110dbec31e4291339110bb564f67076332d40f2cd9ea184ddac2d8369c40fb07f0'
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
        for el in req:
            date = el['date']
            count = 0
            for i in el['sizes']:
                if i['type'] != 'z':
                    count += 1
                else:
                    break
            url = el['sizes'][count]['url']
            like = el['likes']['count']
            file_name = str(like) + '_' + str(date) + '.jpg'
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
Egor = VK_USER(Yandex_token, id)
count_photo = 5
params = {
    'access_token': TOKEN,
    'owner_id': id,
    'album_id': 'profile',
    'count': '1',
    'v': '5.131',
    'extended': '1',
    'offset': offset
}
# count_photo = requests.get(URL, params).json()['response']['count']
count_photo=input('Введите число фотографий, которое вы хотите сохранить. '
                  'Если хотите сохранить все фото - напишите "Все"'
                  ' По умолчанию программа сохраняет 5 фото.')
if count_photo == 'Все':
    count_photo = requests.get(URL, params).json()['response']['count']
else:
    count_photo = int(count_photo)
from tqdm import tqdm
for i in tqdm(range(count_photo + 1)):
    offset += 1
    Egor.save_photo_album(offset=offset)
