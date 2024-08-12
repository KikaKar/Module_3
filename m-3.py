from datetime import datetime, timedelta 
date = '2024-10-09'

def get_days_from_today(date):
  try:
    date_object = datetime.strptime(date, "%Y-%m-%d").date()
    now_time = datetime.now().date()
    difference = (date_object - now_time).days
    return difference
  except ValueError:
        return "Неправильний формат дати, використовуйте формат дати 'РРРР-ММ-ДД'."
print(get_days_from_today(date))