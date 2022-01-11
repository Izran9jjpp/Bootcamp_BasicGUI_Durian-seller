import json

with open('data.json',encoding='utf-8')as file:
	data = json.load(file)
	print(data)
	print(type(data))
	print(data[0]['name'])
