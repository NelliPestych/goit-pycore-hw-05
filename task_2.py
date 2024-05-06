import re
from typing import Callable

def generator_numbers(text: str):
    # Знаходимо всі дійсні числа у тексті за допомогою регулярного виразу
    pattern = r'\b\d+\.\d+\b'  # Пошук окремих чисел з плаваючою точкою (початок та кінець є цифрою, всередині можуть міститись цифри і крапка)
    for match in re.finditer(pattern, text):
        #  Повертаємо знайдений паттерн у тексті у вигляді дійсного числа
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    # Використовуємо генератор для отримання всіх чисел і підсумовуємо їх
    total = sum(func(text))
    return total

# Використання функції:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
