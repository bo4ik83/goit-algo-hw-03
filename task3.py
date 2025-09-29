import re

def normalize_phone(phone_number: str) -> str:
    # Прибираємо всі символи, окрім цифр та '+'
    cleaned = re.sub(r"[^\d+]","", phone_number.strip())

    # Якщо номер вже починається з '+', перевіряємо чи є потрібний код
    if cleaned.startswith("+"):
        if not cleaned.startswith("+38"):
           # Якщо код інший — повертаємо як є (можна адаптувати під інші країни)
           return cleaned
        return cleaned

    # Якщо номер починається з '380', додаємо '+'
    if cleaned.startswith("380"):
        return "+" + cleaned
    
    # Якщо номер починається з '0' або без коду, додаємо '+38'
    return "+38" + cleaned

# Приклад використання
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)