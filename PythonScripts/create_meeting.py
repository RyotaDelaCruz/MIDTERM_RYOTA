import requests
from config import HEADERS

url = "https://webexapis.com/v1/meetings"

payload = {
    "title": "Python Meeting",
    "start": "2026-06-20T08:00:00Z",
    "end": "2026-06-20T09:00:00Z"
}

try:
    response = requests.post(url, headers=HEADERS, json=payload)

    print("Status:", response.status_code)
    print(response.text)

except Exception as e:
    print(e)