import requests

response = requests.get('https://randomuser.me')
print(response.status_code )