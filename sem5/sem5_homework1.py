# ======================================================================================
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после
# друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем
# 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# ======================================================================================
from random import randint as ri
import time

total_sweet = 150
take_sweet = 0
player_sweet = 0
bot_sweet = 0


def players_count():
    players_number = int(input('Введите 1, если хотите играть с ботом или 2, если хотите играть с человеком: '))
    while players_number != 1 and players_number != 2:
        players_number = int(input('One more time: '))
    return players_number

players = players_count()

def start_game():
    print('На столе лежит 150 конфет.\nИграют два игрока делая ход друг после друга.')
    time.sleep(3)
    print('Первый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет.')
    time.sleep(3)
    print('Все конфеты оппонента достаются сделавшему последний ход.')
    time.sleep(3)
    who_is_first()


def who_is_first():
    print('Идет жеребьевка')
    time.sleep(2)
    turn_number = ri(1, 2)
    if turn_number == 1:
        print('Первый ход у первого игрока')
        time.sleep(2)
        player_turn()
    else:
        if players == 1:
            print('Первый ход у бота')
            time.sleep(2)
            bot_turn()
        else:
            print('Первый ход у второго игрока')
            time.sleep(2)
            player2_turn()


def player_turn():
    global total_sweet
    global take_sweet
    global player_sweet
    print(f'Ход первого игрока, сейчас на столе {total_sweet} конфет')
    take_sweet = int(input('Сколько вы берерте конфет? - '))
    while take_sweet > 28 or take_sweet < 0 or take_sweet > total_sweet:
        if take_sweet > 28:
            take_sweet = int(
                input('Вы берете слишком много конфет! Попробуйте снова - '))
        elif take_sweet < 0:
            take_sweet = int(
                input('Вы ввели отрицательное число! Попробуйте снова - '))
        elif take_sweet > total_sweet:
            take_sweet = int(
                input('Вы хотите взять больше конфет, чем есть на столе! Попробуйте снова - '))
        else:
            take_sweet = int(input('Ошибка ввода! Попробуйте снова - '))
    total_sweet -= take_sweet
    player_sweet += take_sweet
    time.sleep(2)
    print(
        f'Вы взяли {take_sweet} конфет. На столе осталось {total_sweet} конфет')
    if total_sweet > 0:
        if players == 1:
            print('Сейчас ходит бот')
            time.sleep(2)
            bot_turn()
        else:
            print('Сейчас ходит второй игрок')
            time.sleep(2)
            player2_turn()
    else:
        print('Первый игрок победил!')


def bot_turn():
    global total_sweet
    global take_sweet
    global bot_sweet
    if total_sweet % 29 != 0:
        take_sweet = total_sweet % 29
    else:
        take_sweet = ri(1, 28)
    total_sweet -= take_sweet
    bot_sweet += take_sweet
    time.sleep(2)
    print(
        f'Бот взял {take_sweet} конфет. На столе осталось {total_sweet} конфет')
    if total_sweet > 0:
        player_turn()
    else:
        print('Бот победил!')


def player2_turn():
    global total_sweet
    global take_sweet
    global player_sweet
    print(f'Ход второго игрока, сейчас на столе {total_sweet} конфет')
    take_sweet = int(input('Сколько вы берерте конфет? - '))
    while take_sweet > 28 or take_sweet < 0 or take_sweet > total_sweet:
        if take_sweet > 28:
            take_sweet = int(
                input('Вы берете слишком много конфет! Попробуйте снова - '))
        elif take_sweet < 0:
            take_sweet = int(
                input('Вы ввели отрицательное число! Попробуйте снова - '))
        elif take_sweet > total_sweet:
            take_sweet = int(
                input('Вы хотите взять больше конфет, чем есть на столе! Попробуйте снова - '))
        else:
            take_sweet = int(input('Ошибка ввода! Попробуйте снова - '))
    total_sweet -= take_sweet
    player_sweet += take_sweet
    time.sleep(2)
    print(
        f'Вы взяли {take_sweet} конфет. На столе осталось {total_sweet} конфет')
    if total_sweet > 0:
        print('Сейчас ходит первый игрок')
        time.sleep(2)
        player_turn()
    else:
        print('Второй игрок победил!')


start_game()
