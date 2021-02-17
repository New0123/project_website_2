Для развертывания проекта на сервере нам понадобится:
1. Установить Python 3.5.2 (ссылка на скачивание с официального сайта - https://www.python.org/downloads/release/python-352/)
2. Открываем командную строку от имени администратора.
3. Выполняем команду: pip install flask
4. Выполняем команду: pip install psycopg2-binary
5. Выполняем команду: pip install flask-sqlalchemy
6. Выполняем команду: pip install Flask-Migrate
7. Выполняем команду: pip install python -m pip install --upgrade pip
8. Выполняем команду: pip install flask-login
9. Выполняем команду: pip install flask-wtf
10. Выполняем команду: pip install email_validator
11. Установить Postgressql версии 12.4 и выше (ссылка на скачивание с официального сайта - https://postgrespro.ru/windows)
12. Скопировать project.sql в папку С:\Program Files\PostgreSQL\12\bin (пароль: 123)
13. Скопировать папку webmssql в папку Python35 (путь в моем случае: C:\Users\user\AppData\Local\Programs\Python\Python35)
14. Открываем командную строку от имени администратора.
15. Переходим в командной строке в папку webmssql (в моем случае: cd C:\Users\user\AppData\Local\Programs\Python\Python35\webmssql)
16. Выполняем команду: venv\Scripts\activate
17. Выполняем команду: set FLASK_APP=webmssql.py
18. Выполняем команду: flask run
19. Будет выдана ссылка на ip-адрес и порт сайта (в моем случае 127.0.0.1:5000)
20. Вводим в адресной строке браузера 127.0.0.1:5000 и логинимся под пользователем artem (пароль: 1)
21. Ознакамливаемся с содержимым сайта.
22. Для отображения графиков на заглавной странице необходимо наличие подключения к сети интернет, так как используется библиотека google для построения графиков.