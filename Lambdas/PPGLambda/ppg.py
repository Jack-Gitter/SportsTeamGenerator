from bs4 import BeautifulSoup
import json
import requests
import re

def findppg(event=None, context=None):
    month = event['queryStringParameters']['birthMonth']
    day = event['queryStringParameters']['birthDay']
    #extract the birth day and month from the query string, enter it into the url, then get the stuff
    
    url = 'https://www.basketball-reference.com/friv/birthdays.fcgi?month='+str(month)+'&day='+str(day)
    #url = 'https://www.basketball-reference.com/friv/birthdays.fcgi?month=12&day=12'
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    listPercent = doc.body.table.find_all('td', {'data-stat' : "pts_per_g"})
    listPlayers = doc.body.table.find_all('a', href=re.compile('/players/'))

    ppgDict = {}

    for idx in range(0, len(listPercent)):
        listPercent[idx] = listPercent[idx].text

    for idx in range(0, len(listPlayers)):
        listPlayers[idx] = listPlayers[idx].text

    for idx in range(0, len(listPercent)):
        ppgDict[listPlayers[idx]] = float(listPercent[idx])

    
    ppgDict = {k: v for k, v in sorted(ppgDict.items(), key=lambda item: item[1])}

    dictLen = len(ppgDict)


    for key in list(ppgDict):
        if dictLen > 4:
            ppgDict.pop(key)
        else:
            break
        dictLen -= 1

    print(ppgDict)


    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET'
        },
        'body': json.dumps(ppgDict)
    }


