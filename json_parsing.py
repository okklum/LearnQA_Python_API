import json

strData = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And ' \
          'this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
dictData = json.loads(strData)
key = "messages"
print(dictData["messages"][1]["message"])