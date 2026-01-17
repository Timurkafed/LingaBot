import google.generativeai as genai

# ВСТАВЬ СВОЙ КЛЮЧ СЮДА
GEMINI_API_KEY = "AIzaSyB3WDZzImuBbOy8ovgi5yLE2NcWdHoNCxM"

print(f"📚 Версия библиотеки: {genai.__version__}")

try:
    genai.configure(api_key=GEMINI_API_KEY)
    print("✅ Ключ принят. Список доступных моделей:")
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"👉 {m.name}")
            
except Exception as e:
    print(f"❌ Ошибка: {e}")

input("Нажми Enter, чтобы выйти...")