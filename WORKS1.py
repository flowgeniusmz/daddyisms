import requests
import json

content = "You bought the top because it 'looked strong'? So does a volcano before it erupts."
url = "https://discord.com/api/webhooks/1360719040682660162/5AdyoOsvOJgwIGAs4JNC_9LFaEFN2-l9Zg8LF8-0IcmFTpi7d7xmaPIBLELjcwuR-QF1"

payload_json = {
    "content": content
}

files = {
    'payload_json': (None, json.dumps(payload_json), 'application/json'),
    'file1': ('4152025.png', open('images/4152025.png', 'rb'), 'image/png')
}

response = requests.post(url, files=files)
print(response.status_code, response.text)
