import json

strData = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And ' \
          'this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
dictData = json.loads(strData)
key = "messages"

if key in dictData:
    key1 = "message"
    if key1 in dictData:
        print(dictData["messages"][1]["message"])
    else:
        print(f"Key {key1} not found in modified JSON")
else:
    print(f"Key {key} not found in JSON")