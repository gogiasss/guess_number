import random

#количество попыток

tries = 0

number = random.randint(1, 50)


print('Угадай число от 1 до 50')

while tries < 6:
    guess = int(input(' Введи число: '))

    tries+=1

    if guess < number:
        print('Слишком мало')

    if guess > number:
        print('Слишком много.')

    if guess == number:
        print(f'Ты угадал! Это была {tries} попытка!')
        break

    if guess != number and tries == 6:
        print(f'Ты проиграл. Количество попыток исчерпано. Я загадал число: {number}')

print('Игра закончена..')
