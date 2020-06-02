import random

#количество попыток

tries = 0

#Генерируем случайное число
number = random.randint(1, 50)


print("""Привет! Я загадал число в диапазоне от 1 до 50.
         Попробуй его угадать. У тебя всего 6 попыток.""")

while tries < 6:
    guess = int(input('Введи число: '))

    tries+=1

    if guess < number:
        print('Число слишком маленькое')

    if guess > number:
        print('Число слишком большое.')

    if guess == number:
        print(f'Ты угадал! Это была {tries} попытка!')
        break

    if guess != number and tries == 6:
        print(f'Ты проиграл. Количество попыток исчерпано. А я загадал число: {number}')

print('Игра закончена..')
