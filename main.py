import requests

mainUrl = 'https://playground.learnqa.ru'

response = requests.get(f'{mainUrl}/api/long_redirect')
print(len(response.history))