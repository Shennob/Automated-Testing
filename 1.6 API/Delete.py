import requests

class test_new_location():

    def test_create_new_location(self):

        base_url = 'https://rahulshettyacademy.com'
        key = '?key=qaclick123'
        post_resourse = '/maps/api/place/add/json'
        get_resourse = '/maps/api/place/get/json'
        put_resourse = '/maps/api/place/update/json'
        delete_resourse = '/maps/api/place/delete/json'
        new_address = '50 Sovetskay street, RU'

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

        put_url = base_url + put_resourse + key
        print(put_url)

        json_put_location = {
            "place_id" : place_id,
            "address" : new_address,
            "key" : "qaclick123"
        }

        result_put = requests.put(put_url, json=json_put_location)
        print(result_put.json())

        print(f'Статус-код: {result_put.status_code}')
        assert result_put.status_code == 200
        print('Статус-код PUT корректен')

        check_response_put = result_put.json()

        msg = check_response_put.get('msg')
        print(msg)
        assert msg == 'Address successfully updated'
        print('Поле MSG корректно')

        result_get = requests.get(get_url)
        print(result_get.json())
        check_response_get = result_get.json()

        print(f'Статус-код: {result_get.status_code}')
        assert result_get.status_code == 200
        print('Статус код GET корректен')

        actual_address = check_response_get.get('address')
        print(actual_address)
        assert actual_address == new_address
        print('Адресс изменился')

        delete_url = base_url + delete_resourse + key
        print(delete_url)

        json_delete_location = {
            "place_id" : place_id
        }

        result_delete = requests.delete(delete_url, json=json_delete_location)
        print(result_delete.json())

        print(f'Статус-код: {result_delete.status_code}')
        assert result_delete.status_code == 200
        print('Статус-код DELETE корректен')

        check_response_delete = result_delete.json()

        status = check_response_delete.get('status')
        print(status)
        assert status == 'OK'
        print('Поле Status корректно')

        result_get = requests.get(get_url)
        print(result_get.json())

        print(f'Статус-код: {result_get.status_code}')
        assert result_get.status_code == 404
        print('Стутс-код корректен, локация удалена')

        check_response_get = result_get.json()
        msg = check_response_get.get('msg')
        print(msg)
        assert msg == "Get operation failed, looks like place_id  doesn't exists"
        print('Поле MSG корректно')


start = test_new_location()
start.test_create_new_location()
print('Тест прошел успешно')