from datetime import datetime, timedelta

def get_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    return future_date.strftime('%Y-%m-%d')

def main():
    days = int(input("Введите количество дней: "))
    future_date = get_future_date(days)
    print(f"Дата через {days} дней: {future_date}")

main()
