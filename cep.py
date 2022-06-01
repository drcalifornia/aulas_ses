import requests

url = "https://www.cepaberto.com/api/v3/cep?cep=71741705"
# O seu token está visível apenas pra você
headers = {}#{'Authorization': 'Token token=85fb1a5f708eed7190285174fdafa2f2'}
response = requests.get(url, headers=headers)
print(response.text)
#end = response.json()
#print(end['latitude'])