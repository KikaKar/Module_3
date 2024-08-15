from datetime import datetime, timedelta 
from random import sample 
# Завдання № 1
date = '2024-10-09' # Вхідні дані

def get_days_from_today(date):
  try:
    date_object = datetime.strptime(date, "%Y-%m-%d").date() # Перевод даних іх формату строки в дату
    now_time = datetime.now().date() # Теперишній час
    difference = (date_object - now_time).days # Обрахунок різниці в часі
    return difference
  except ValueError:
        return "Неправильний формат дати, використовуйте формат дати 'РРРР-ММ-ДД'." # Обробка вийнятків у вхідних даних
print(f"Завдання № 1, кількість днів між датами {get_days_from_today(date)}")

# Завдання № 2

min_num = 1 # Мінімальне можливе число
max_num = 1000 # Максимальне можливе число
quantity = 6 # Кількість чисел для вибірки

def get_numbers_ticket(min_num, max_num, quantity):
  numbers = sample(range(min_num, max_num), quantity) # Додавання у список випадкових чисел
  return numbers

print(f"Завдання № 2, лотерейний білет {get_numbers_ticket(min_num, max_num, quantity)}")