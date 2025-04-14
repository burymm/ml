import requests
import sys



params = {
    'json': True,
}


for line in sys.stdin:
    line = line.rstrip()
    res = requests.get('http://numbersapi.com/{num}/math'.format(num=line), params=params)
    data = res.json()
    print('Interesting' if data['found'] else 'Boring')