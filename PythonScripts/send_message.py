import requests
from config import HEADERS

url = "https://webexapis.com/v1/messages"

payload = {
    "roomId" : "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vM2E1Y2M5OTAtNjg1ZS0xMWYxLTliYTEtYmRjMmYxOTdjZTMz",
    "text" : "Hello from Python"
}
try:
    response = requests.post(url, headers=HEADERS, json=payload)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        print("Message Sent Successfully")
    else:
        print("response.text")

except Exception as e:
    print("Error:", e)