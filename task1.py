from datetime import datetime 

def get_days_from_today(date_str: str) -> int:
   try:
      target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
      # Перетворюємо рядок у об'єкт datetime (лише дата)
      today = datetime.today().date()
      # Поточна дата
      today = datetime.today().date()
      # Різниця у днях (заданa - сьогодні)
      delta = today - target_date

      return delta.days
   except ValueError:
      raise ValueError("Невірний формат дати. Використовуйте формат 'YYYY-MM-DD'.")
   
print(get_days_from_today("2020-09-29"))