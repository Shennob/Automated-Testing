import requests

class test_new_location():

    def test_create_new_location(self):

        base_url = 'https://rahulshettyacademy.com'
        key = '?key=qaclick123'
        post_resourse = '/maps/api/place/add/json'
        get_resourse = '/maps/api/place/get/json'

        post_url = base_url + post_resourse + key
        print(post_url)

        json_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        result_post = requests.post(post_url, json=json_location)
        print(result_post.json())

        print(f'Статус-код: {result_post.status_code}')
        assert result_post.status_code == 200
        print('Стату-код POST корректен')

        check_response_post = result_post.json()

        status = check_response_post.get('status')
        print(status)
        assert status == 'OK'
        print('Поле Status корректно')

        place_id = check_response_post.get('place_id')
        print(f'Поле place_id: {place_id}')

        get_url = base_url + get_resourse + key + '&place_id=' + place_id
        print(get_url)

        result_get = requests.get(get_url)
        print(result_get.json())

        print(f'Статус-код: {result_get.status_code}')
        assert result_get.status_code == 200
        print('Статус код GET корректен')


start = test_new_location()
start.test_create_new_location()
print('Тест прошел успешно')