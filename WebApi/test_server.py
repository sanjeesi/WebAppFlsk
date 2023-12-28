import requests

url = 'http://localhost:5000/api/run_command'
payload = {'command': 'ls -l'}
response = requests.post(url, json=payload)

print(response.json())
