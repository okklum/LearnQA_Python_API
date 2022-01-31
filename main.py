import requests

mainUrl = 'https://playground.learnqa.ru'

response = requests.get(f'{mainUrl}/api/get_text')
print(response.text)