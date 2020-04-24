import json

file = open('Berakhot_sefaria.json')

file_text = file.read()

data = json.loads(file_text)

print(data)
print(type(data))
print(data.keys())
print(file_text)