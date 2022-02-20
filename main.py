import requests

url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

response1 = requests.post(url)
print(response1, "Ответ на запрос без параметра method")

response2 = requests.patch(url)
print(response2, "Ответ на запрос не из списка")

response3 = requests.get(url, params={"method": "GET"})
print(response3, "Ответ на запрос с правильным значением method")

# Поиск всех реальных типов запроса и значений параметра method
methodList = ["GET", "POST", "PUT", "DELETE"]
typeList = ["post", "put", "delete"]

for methodType in methodList:
    responseGet = requests.get(url, params={"method": {methodType}})
    if responseGet.status_code != 200:
        print(f"Для метода GET запрос с параметрами", {methodType}, "ответил кодом", {responseGet.status_code})
    else:
        break

for methodType1 in methodList:
    for typeMethod in typeList:
        responseType = requests.request(typeMethod, url, data={"method": {methodType1}})
        # print(typeMethod, methodType1, responseType.status_code)
        if responseType.status_code != 200:
            print(f"Для метода GET запрос с параметрами", {typeMethod}, "ответил кодом", {responseType.status_code})
        else:
            break
