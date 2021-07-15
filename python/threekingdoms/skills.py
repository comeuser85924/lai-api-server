import requests
import json
import os

def skills(key):
    url = "https://sheets.googleapis.com/v4/spreadsheets/1LGTmxJPbJ3p1lhpXJaow7OtbLbF1T0kO1SoZlR_IMW8/values/'Skills'!A1:D999?key=" + key
    resp = requests.request("GET", url)
    newList = []
    for item in resp.json()['values']:
        if(item[0] != 'quality' and item[0] != 'break'):
            newList.append({
                'quality':item[0],
                'name':item[1],
            })
        
    return {'data':newList}