from datetime import datetime

def get_current_time_info():
    now = datetime.now()
    date_time = now.strftime('%Y-%m-%d %H:%M:%S')
    day_of_week = now.strftime('%A')
    week_number = now.isocalendar()[1]
    return date_time, day_of_week, week_number

def main():
    date_time, day_of_week, week_number = get_current_time_info()
    print(f"Текущая дата и время: {date_time}")
    print(f"День недели: {day_of_week}")
    print(f"Номер недели в году: {week_number}")

main()
