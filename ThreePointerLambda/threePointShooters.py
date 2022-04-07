from bs4 import BeautifulSoup
import json
import requests
import re

def findThreePointShooters(event=None,context=None):
    #month = event['birthMonth']
    #day = event['birthDay']
    #extract the birth day and month from the query string, enter it into the url, then get the stuff
    
   # url = 'https://www.basketball-reference.com/friv/birthdays.fcgi?month='+month+'&day='+day
    url = 'https://www.basketball-reference.com/friv/birthdays.fcgi?month=12&day=12'
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    listPercent = doc.body.table.find_all('td', {'data-stat' : "fg3_pct"})
    listPlayers = doc.body.table.find_all('a', href=re.compile('/players/'))

    #make it into dict, sort the dict by the stat, then truncate the dict

    percentDict = {}

    for idx in range(0, len(listPercent)):
        listPercent[idx] = listPercent[idx].text

    for idx in range(0, len(listPlayers)):
        listPlayers[idx] = listPlayers[idx].text

    for idx in range(0, len(listPercent)):
        percentDict[listPlayers[idx]] = listPercent[idx]

    percentDict = {k: v for k, v in sorted(percentDict.items(), key=lambda item: item[1])}

    dictLen = len(percentDict)

    for key in list(percentDict):
        if dictLen > 4:
            percentDict.pop(key)
        else:
            break
        dictLen -= 1

    return {
        'statusCode': 200,
        'body': json.dumps(percentDict)
    }


