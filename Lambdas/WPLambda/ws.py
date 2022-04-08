from bs4 import BeautifulSoup
import json
import requests
import re

def findws(event=None, context=None):
    month = event['queryStringParameters']['birthMonth']
    day = event['queryStringParameters']['birthDay']
    #extract the birth day and month from the query string, enter it into the url, then get the stuff
    #url = 'https://www.basketball-reference.com/friv/birthdays.fcgi?month=12&day=12'
    url = 'https://www.basketball-reference.com/friv/birthdays.fcgi?month='+str(month)+'&day='+str(day)
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    listPercent = doc.body.table.find_all('td', {'data-stat' : "ws"})
    listPlayers = doc.body.table.find_all('a', href=re.compile('/players/'))

    wsDict = {}

    for idx in range(0, len(listPercent)):
        listPercent[idx] = listPercent[idx].text

    for idx in range(0, len(listPlayers)):
        listPlayers[idx] = listPlayers[idx].text

    for idx in range(0, len(listPercent)):
        wsDict[listPlayers[idx]] = float(listPercent[idx])

    
    wsDict = {k: v for k, v in sorted(wsDict.items(), key=lambda item: item[1])}

    dictLen = len(wsDict)

    for key in list(wsDict):
        if dictLen > 4:
            wsDict.pop(key)
        else:
            break
        dictLen -= 1

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET'
        },
        'body': json.dumps(wsDict)
    }


