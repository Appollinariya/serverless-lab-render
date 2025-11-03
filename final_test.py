import urllib.request
import json

# ЗАМЕНИТЕ НА ВАШ РЕАЛЬНЫЙ URL
url = "https://serverless-lab-a535.onrender.com"

print("🚀 Тестируем полную функциональность...")

print("\n1. 📄 Главная страница:")
try:
    with urllib.request.urlopen(url) as response:
        print("✅", response.read().decode('utf-8').strip())
except Exception as e:
    print("❌", e)

print("\n2. 💾 Сохраняем сообщение в БД:")
try:
    data = {"message": "Тест из PostgreSQL! 🐘"}
    json_data = json.dumps(data).encode('utf-8')
    req_save = urllib.request.Request(
        f"{url}/save",
        data=json_data,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    with urllib.request.urlopen(req_save) as response:
        result = response.read().decode('utf-8')
        print("✅", result)
except Exception as e:
    print("❌", e)

print("\n3. 📋 Получаем сообщения из БД:")
try:
    with urllib.request.urlopen(f"{url}/messages") as response:
        messages = response.read().decode('utf-8')
        print("✅ Сообщения из базы данных:")
        print(messages)
except Exception as e:
    print("❌", e)