def caching_fibonacci():
    # Ініціюємо порожній словник для збереження результатів обчислень
    cache = {}

    # Внутрішня функція fibonacci для обчислення чисел Фібоначчі
    def fibonacci(n):
        # Перевірка умов і наявності значення у змінній cache
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            # Обчислення числа Фібоначчі та збереження результату у кеші
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    # Повернення внутрішньої функції для зовнішнього використання
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()
# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))
print(fib(15))
