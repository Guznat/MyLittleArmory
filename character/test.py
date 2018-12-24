#
# import urllib.request
# import json
#
# import pprint
#
#
# api_key = 'USOAQyx1baVrOJYI0Ym1Lv2fiyiDehmWyV'
# url = 'https://eu.api.blizzard.com/wow/character/'
#
# def mount_search(character, server):
#     char = character
#     serv = server.replace(' ', '-')
#     final_url = url + serv + '/' + char + '?fields=mounts&access_token=' + api_key
#     response = urllib.request.urlopen(final_url)
#     data = json.load(response)
#     mounts = data['mounts']
#
#     for mount in mounts['collected']:
#         pprint.pprint('Name:'+ mount['name']+ " Flying:"+ str(mount['isFlying']))
#
# pprint.pprint(mount_search('Guznat', 'defias-brotherhood'))