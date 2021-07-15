import requests
import json

def generals(key):
    url = "https://sheets.googleapis.com/v4/spreadsheets/1LGTmxJPbJ3p1lhpXJaow7OtbLbF1T0kO1SoZlR_IMW8/values/'Generals'!A1:D999?key=" + key
    resp = requests.request("GET", url)
    newList = []
    for item in resp.json()['values']:
        if(item[0] != 'country' and item[0] != 'break'):
            newList.append({
                'country':item[0],
                'name':item[1],
                'quality':item[2],
                'cost':item[3],
            })
        
    return {'data':newList}
