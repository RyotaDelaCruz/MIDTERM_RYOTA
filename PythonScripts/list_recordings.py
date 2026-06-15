import requests
from config import HEADERS

url = "https://webexapis.com/v1/recordings"

try:
    response = requests.get(url, headers=HEADERS)

    print("Status:", response.status_code)
    print(response.text)

except Exception as e:
    print(e)