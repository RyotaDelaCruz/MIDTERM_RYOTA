import requests
from config import HEADERS

message_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL01FU1NBR0UvODU5ZGU4NjAtNjg2NS0xMWYxLWEyYjItNWY3MDRmMjJjMTk4"

url = f"https://webexapis.com/v1/messages/{message_id}"

payload = {
    "roomId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vM2E1Y2M5OTAtNjg1ZS0xMWYxLTliYTEtYmRjMmYxOTdjZTMz",
    "text" : "Updated by Python"
}

try:
    response = requests.put(url, headers=HEADERS, json=payload)

    print("Status:", response.status_code)
    print(response.text)

except Exception as e:
    print(e)