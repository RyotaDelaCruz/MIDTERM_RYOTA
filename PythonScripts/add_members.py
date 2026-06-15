import requests
from config import HEADERS

url = "https://webexapis.com/v1/memberships"

payload = {
    "roomId" : "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vM2E1Y2M5OTAtNjg1ZS0xMWYxLTliYTEtYmRjMmYxOTdjZTMz",
    "personEmail": "sarabiafrancis752@gmail.com"
}

try:
    response = requests.post(url, headers=HEADERS, json=payload)

    print("Status:", response.status_code)
    print(response.text)

except Exception as e:
    print(e)