import urllib.request
import json

url = "https://ВАШ-URL.onrender.com/echo"
data = {"user": "student", "action": "test"}

# Преобразуем данные в JSON
json_data = json.dumps(data).encode('utf-8')

# Создаем запрос
req = urllib.request.Request(
    url,
    data=json_data,
    headers={'Content-Type': 'application/json'},
    method='POST'
)

try:
    # Отправляем запрос
    with urllib.request.urlopen(req) as response:
        result = response.read().decode('utf-8')
        print("Успех! Ответ:")
        print(result)
except Exception as e:
    print("Ошибка:", e)
