# import os
# path = os.getcwd()
# file_name = 'photo.jpg'
# full_path = os.path.join(path, file_name)
# print(full_path)
import requests
from pprint import pprint
# a = 'https://sun9-53.userapi.com/impg/Y3SLP4UKmN9QdJW4nCWplAacBu868awd__tSnQ/zp-eGOXMhVI.jpg?size=87x130&quality=96&sign=c4838c2aeb4eba3cecfe68b3cecffc48&c_uniq_tag=NGboP37NP18-njqL3-Y2pv1HQMBO3fbgUa-St1HfY7Y&type=album'
# img_data = requests.get(a).content
# with open(full_path, 'wb') as handler:
#     handler.write(img_data)
URL = 'https://api.vk.com/method/photos.getById'
TOKEN = 'd82c00e5a40f505a9c1c30d04487eb7b42fbdf7e94aaa0a014ed4dcdd23acac2cf809f65bd9edfc1e1463'
dict = {
    'id': 457245930,
    'owner_id': 403142107
}
photo = str(dict['owner_id']) + '_' + str(dict['id'])
params = {
    'access_token' : 'd82c00e5a40f505a9c1c30d04487eb7b42fbdf7e94aaa0a014ed4dcdd23acac2cf809f65bd9edfc1e1463',
    'photos' : photo,
    'extended' : 1,
    'v' : '5.131'
}
response = requests.get(URL, params).json()['response'][0]['likes']['count']
pprint(response)