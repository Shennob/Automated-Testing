import requests

url = "https://official-joke-api.appspot.com/jokes/random"
print(url)
result = requests.get(url)
print("Статус код: " + str(result.status_code))
assert 200 == result.status_code
if result.status_code == 200:
    print('Успешно, статус код верен!')
else:
    print('Провал, статус код не верен!')
result.encoding = 'utf-8'
print(result.text)