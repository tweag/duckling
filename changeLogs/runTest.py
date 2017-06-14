### Usage: python runTest.py

import requests
import json
import time

timestr = time.strftime("%Y%m%d-%H%M%S")

def getLine(line):
    url     = 'http://0.0.0.0:8000/parse'
    payload = {'text': line}
    headers = {}
    res = requests.post(url, data=payload, headers=headers)

    with open('./testOutput/'+timestr+'.res', 'a') as out:
        out.write(line+'\n')
        out.write(json.dumps(res.json(), indent=4, sort_keys=True)+'\n')

if __name__ == "__main__" :
    with open('ecoTest.md', 'r') as f:
        for line in f.readlines():
            getLine(line.rstrip())
