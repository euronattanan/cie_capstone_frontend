import requests
import uuid
import time
import webbrowser

BASE = 'http://127.0.0.1:5000/'

data = {
    'firstname': 'Euro',
    'lastname': 'Euro',
    'contact': '0957395770',
    'numberOfVaccines': 2,
    'doses': [
        {
            'vaccine': 'Pfizer'
        },
        {
            'vaccine': 'Pfizer'
        }
    ]
}
headers = {'Content-type': 'application/json'}
response_post = requests.post(BASE, json = data, headers = headers)
print('post response: ', response_post.json())
post_resp = response_post.json()['data']
print("post_resp: ", "'" + post_resp + "'")
print("post_resp type: ", type(post_resp))

time.sleep(3)


# response_get = requests.get(str(post_resp))
response_get = requests.get(str(post_resp))
# print('get response: ', response_get.json())

new = 2 #open in new tab if possible
url = (post_resp)

webbrowser.open(url,new=new)



