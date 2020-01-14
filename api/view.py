from django.http import HttpResponse

import json
from django.http import JsonResponse
from . import config
import requests

my_api_key = config.API_KEY['api_key']
base_url = 'https://api.themoviedb.org/3/'

def top_movie(requeset):
    url = f'{base_url}movie/popular?api_key={my_api_key}&language=en-US&page=1'
    response = requests.get(url)
    response_json = response.json()
    result = response_json['results']
    return JsonResponse(result[0:10], safe=False)


def detail_movie(requeset, id):
    url = f'{base_url}movie/{id}?api_key={my_api_key}&language=en-US'
    response = requests.get(url)
    result = response.json()
    return JsonResponse(result)