import requests

url = "http://127.0.0.1:8000/pl/"

headers = {
    "Content-Type": "application/json",
    "X-API-KEY": "1b3e2a4939ef4c789821fba000123abc"
}

payload = {
    "keywords": ["iphone", "mobile","shoes"],
    "pincodes": [560001,560003,5660003]      
}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response Text:", response.text)