"""
Лабораторная 4 Вариант 9
Написать функцию, которая принимает объект datetime и возвращает временную метку (timestamp) из данного объекта.
"""

import datetime

def datetime_to_timestamp(dt):
    return dt.timestamp()

dt = datetime.datetime (2023, 9, 22, 12, 0, 0)
timestamp = datetime_to_timestamp(dt)
print(timestamp) #1695373200.0
