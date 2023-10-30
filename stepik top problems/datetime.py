from datetime import datetime

def str2period(str_dates):
    period = tuple(map(lambda x: datetime.strptime(x, "%d.%m.%Y"), str_dates.split("-")))
    return period if len(period) > 1 else period * 2


def not_overlapping(period1, period2):
    return period1[1] < period2[0] or period1[0] > period2[1]


def is_available_date(booked_dates, date_for_booking):
    check_dates = str2period(date_for_booking)
    for bd in booked_dates:
        if not not_overlapping(str2period(bd), check_dates):
            return False
    return True



"""Во время визита очередного гостя сотрудникам отеля приходится проверять, доступна ли та или иная дата для бронирования номера.

Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:

    booked_dates — список строковых дат, недоступных для бронирования. Элементом списка является либо одиночная дата, либо период (две даты через дефис). Например:

    ['04.11.2021', '05.11.2021-09.11.2021']

    date_for_booking — одиночная строковая дата или период (две даты через дефис), на которую гость желает забронировать номер. Например:

    '01.11.2021' или '01.11.2021-04.11.2021'

Функция is_available_date() должна возвращать True, если дата или период date_for_booking полностью доступна для бронирования. В противном случае функция должна возвращать False."""