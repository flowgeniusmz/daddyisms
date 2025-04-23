import requests
import base64

url = "https://discord.com/api/webhooks/1360719040682660162/5AdyoOsvOJgwIGAs4JNC_9LFaEFN2-l9Zg8LF8-0IcmFTpi7d7xmaPIBLELjcwuR-QF1"
files = {
    'payload_json': (None, '{"content": "Do you even trade, bro?"}'),
    'file1': ('images/image2.png', open('images/image2.png', 'rb'), 'image/png')
}

response = requests.post(url, files=files)
print(response.status_code, response.text)