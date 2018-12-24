from django.shortcuts import render
import urllib.request
import json
from django.views import View
from.forms import MountSearchForm
import pprint


api_key = 'USOAQyx1baVrOJYI0Ym1Lv2fiyiDehmWyV'
url = 'https://eu.api.blizzard.com/wow/character/'

# def mount_search(character, server):
#     char = character
#     serv = server.replace(' ', '-')
#     final_url = url + serv + '/' + char + '?fields=mounts&access_token=' + api_key
#     response = urllib.request.urlopen(final_url)
#     data = json.load(response)
#     mounts = data['mounts']
#
#     for mount in mounts['collected']:
#         pprint.pprint(mount['name'])
#
# mount_search('Bob', 'defias-brotherhood')


class MountSearch(View):
    def get(self, request):
        form = MountSearchForm()
        ctx = {
            'form': form
        }
        return render(request, 'character/mounts.html', ctx)

    def post(self, request):
        form = MountSearchForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            final_mounts = []
            char = str(form['character'])
            serv = form['server']
            final_url = url + str(serv) + '/' + str(char) + '?fields=mounts&access_token=' + api_key
            response = urllib.request.urlopen(final_url)
            data = json.load(response)
            mounts = data['mounts']
            collected = mounts['collected']
            collected_number = mounts['numCollected']
            not_collected_number = mounts['numNotCollected']
            for mount in collected:
                final_mounts.append(mount['name'])
            ctx = {
                'final_mounts': final_mounts,
                'collected_number':collected_number,
                'not_collected_number':not_collected_number,
            }
            return render(request, 'character/mounts.html', ctx)
        return render(request, 'character/mounts.html', ctx)








