import requests

class TestCreateJoke():

    def test_create_random_joke(self):
        url = "https://official-joke-api.appspot.com/jokes/random"
        print(url)

        result = requests.get(url)
        print(result.json())

        print(f'Статус-код: {result.status_code}')
        assert result.status_code == 200
        print('Статус-код корректен')

        check_joke = result.json()
        joke_type = check_joke.get('type')
        print(joke_type)
        print('Тест прошел успешно')

start = TestCreateJoke()
start.test_create_random_joke()