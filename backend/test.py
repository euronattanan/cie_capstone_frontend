import requests

BASE = 'http://127.0.0.1:5000/'

testJsonData = {
    'information': {
        'firstname': 'Nattanan',
        'lastname': 'Poolpaodumrongk',
        'contact': '0957395770',
        'numberOfVaccines': 2,
        'doses': [
            'Astra',
            'AstraZeneca'
        ]
    }
}
headers = {'Content-type': 'application/json'}
response = requests.post(BASE + 'getqrcode/1', json=testJsonData, headers=headers)

#status 200 = ok, nothing crash
print(response)