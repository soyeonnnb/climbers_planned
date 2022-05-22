import json
import requests
import js2py
from tests import *

def getLatLng(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
    headers = {"Authorization": "KakaoAK 073a393656181c6073880062d3507191"}
    result = json.loads(str(requests.get(url, headers=headers).text))
    match_first = result['documents'][0]['address']
    return float(match_first['y']), float(match_first['x'])
    
# eval_res, tempfile = js2py.run_file("travels\\tests.js")
# print(tempfile.returnAddress)

eval_res, tempfile = js2py.run_file("travels\\tests.js")
tempfile.wish()