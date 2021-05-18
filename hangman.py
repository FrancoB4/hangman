import random
import os


def get_data(file):
    words = []
    with open('./archives/data.txt', 'r', encoding='utf-8') as f:
        for i in f:
            words.append(i.replace('\n', ''))
    return words


def win():
    os.system('clear')
    print('\nHAS GANADO!! ERES EL MEJOR. \nGRACIAS POR JUGAR')

def attempt(hide, word):
    os.system('clear')
    print('Bienvenido a Hangman!! \n')
    show = ''
    for i in hide:
        if i['enabled'] == False:
            show = show + '- '
        else:
            show = show + i['letter'].upper() + ' '
    print(show + '\n')
    try:
        char = input('Ingresa una letra: ').lower()
        if char.isnumeric():
            raise ValueError('Solo se permiten letras')
        for i in hide:
            if i['letter'] == char:
                i['enabled'] = True
                word = word.replace(char, '')
        if word == '':
            win()
        else:
            attempt(hide, word)
    except ValueError as ve:
        print(ve)


def run():
    word = random.choice(get_data('./archives/data.txt'))
    hide = [{'enabled': False, 'letter': i} for i in word]
    attempt(hide, word)


if __name__ == '__main__':
    run()