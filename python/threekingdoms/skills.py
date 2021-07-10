import requests
import json
import os

def skills():
    googleSheepKey = os.environ['google_sheet_key']
    url = "https://sheets.googleapis.com/v4/spreadsheets/1LGTmxJPbJ3p1lhpXJaow7OtbLbF1T0kO1SoZlR_IMW8/values/'Skills'!A1:D999?key=" + googleSheepKey
    resp = requests.request("GET", url)
    return resp.json()