# Создание логов
from datetime import datetime as dt
from time import time

def name_csv(data):
    with open('log_book.csv', 'a') as file:
        file.write('name;{}\n'
                    .format(data))

def family_csv(data):
    with open('log_book.csv', 'a') as file:
        file.write('family;{}\n'
                    .format(data))


def number_csv(data):
    with open('log_book.csv', 'a') as file:
        file.write('number;{}\n'
                    .format(data))

def time_csv():
  time = dt.now().strftime('%H:%M')
  with open('log_book.csv', 'a') as file:
    file.write('time;{}\n'
                    .format(time))