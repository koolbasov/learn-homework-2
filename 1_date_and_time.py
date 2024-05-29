"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import datetime


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = datetime.datetime.now()
    delta_1 = datetime.timedelta(days=1)
    delta_30 = datetime.timedelta(days=30)
    yesterday = today - delta_1
    thirty_days_ago = today - delta_30
    format = '%d.%m.%Y'
    print(f"Вчера: {yesterday.strftime(format)}")
    print(f"Сегодня: {today.strftime(format)}")
    print(f"30 дней назад: {thirty_days_ago.strftime(format)}")


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
