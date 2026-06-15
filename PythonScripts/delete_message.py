import requests
from config import HEADERS

message_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL01FU1NBR0UvODU5ZGU4NjAtNjg2NS0xMWYxLWEyYjItNWY3MDRmMjJjMTk4"

url = "https://webexapis.com/v1/messages/{message_id}"

try:
    response = requests.delete(url, headers=HEADERS)

    print("Status:", response.status_code)

    if response.status_code ==204:
        print("Message Deleted")
    else:
        print(response.text)

except Exception as e:
    print(e)