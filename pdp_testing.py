import requests

url = "http://127.0.0.1:8000/pdp/"   

headers = {
    "Content-Type": "application/json",
    "X-API-KEY": "1b3e2a4939ef4c789821fba000123abc"
}

payload = {
    "urls": ["https://example.com/iphone"],
    "pincodes": [560001,5600312]
}

response = requests.post(url, json=payload, headers=headers)

print("Status:", response.status_code)
print("Raw Text:", response.text)

try:
    print("JSON:", response.json())
except Exception:
    print("Response is not JSON")