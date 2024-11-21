import requests


# URL для запроса данных
url = 'https://jsonplaceholder.typicode.com/posts'

# Отправка GET-запроса
response = requests.get(url)

# Проверка статуса ответа
if response.status_code == 200:
    # Вывод первых пяти записей
    posts = response.json()[:5]
    for post in posts:
        print(f"ID: {post['id']}, Title: {post['title']}")
else:
    print("Ошибка при запросе данных:", response.status_code)

# Библиотека Requests используется для отправки HTTP-запросов.
# Она упрощает взаимодействие с веб-ресурсами и предоставляет удобный интерфейс для выполнения GET,
# POST и других HTTP-запросов.

# Основные возможности:

# 1. Отправка HTTP-запросов (GET, POST, PUT, DELETE и т.д.).
# 2. Обработка ответа от сервера, включая статус-код и содержимое.
# 3. Работа с параметрами запроса, заголовками и cookies.
# 4. Поддержка аутентификации и сессий для взаимодействия с защищёнными ресурсами.
