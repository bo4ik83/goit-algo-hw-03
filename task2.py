import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    # Перевірка вхідних параметрів
    if not (1 <= min <= max <= 1000):
        return []
    if quantity > (max - min + 1) or quantity <= 0:
        return []
    
    # Генеруємо унікальні випадкові числа
    numbers = random.sample(range(min, max + 1), quantity)

    # Повертаємо відсортований список
    return sorted(numbers)

# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)