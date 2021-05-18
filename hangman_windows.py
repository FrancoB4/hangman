from time import sleep as sl
import random
import os



text = [
    """
       :::    :::         :::         ::::    :::       ::::::::         :::   :::            :::         ::::    :::
      :+:    :+:       :+: :+:       :+:+:   :+:      :+:    :+:       :+:+: :+:+:         :+: :+:       :+:+:   :+:  
     +:+    +:+      +:+   +:+      :+:+:+  +:+      +:+             +:+ +:+:+ +:+       +:+   +:+      :+:+:+  +:+  
    +#++:++#++     +#++:++#++:     +#+ +:+ +#+      :#:             +#+  +:+  +#+      +#++:++#++:     +#+ +:+ +#+   
   +#+    +#+     +#+     +#+     +#+  +#+#+#      +#+   +#+#      +#+       +#+      +#+     +#+     +#+  +#+#+#     
  #+#    #+#     #+#     #+#     #+#   #+#+#      #+#    #+#      #+#       #+#      #+#     #+#     #+#   #+#+#     
 ###    ###     ###     ###     ###    ####       ########       ###       ###      ###     ###     ###    #### \n""",
    '                          ',
]


def get_data(file):
    words = []
    with open('./archives/data.txt', 'r', encoding='utf-8') as f:
        for i in f:
            words.append(i.replace('\n', ''))
    return words


def lbl(text):
    for i in text:
        print(i, end='')
        sl(0.005)
    sl(1)
        


def win():
    os.system('clear')
    print(text[0])
    print('\nHAS GANADO!! ERES EL MEJOR. \nGRACIAS POR JUGAR\n')


def loose(hide):
    print('Has perdido! La proxima sera mejor\n')
    show = ''
    for i in hide:
        show = show + i['letter'].upper()
    print('La palabra era: ' + show)
    retry = input('¿Quieres jugar de nuevo? (y/n)\n').lower()
    if retry == 'y':
        run()
    else:
        os.system('clear')
        quit()


def attempt(hide, word, life):
    os.system('clear')
    print(text[0])
    cont = False
    show = ''
    for i in hide:
        if i['enabled'] == False:
            show = show + '- '
        else:
            show = show + i['letter'].upper() + ' '
    print('Tienes ' + str(life) + ' vidas\n')
    print(text[1] + show + '\n')
    try:
        char = input('Ingresa una letra: ').lower()
        if char.isnumeric():
            raise ValueError('Solo se permiten letras')
        for i in hide:
            if i['letter'] == char:
                i['enabled'] = True
                word = word.replace(char, '')
                cont = True
        if cont == False:
            life -= 1
        if word == '':
            win()
        else:
            if life >= 0:
                attempt(hide, word, life)
            else:
                loose(hide)
    except ValueError as ve:
        print(ve)


def run():
    os.system('clear')
    lbl(text[0])
    life = 5
    word = random.choice(get_data('./archives/data.txt'))
    hide = [{'enabled': False, 'letter': i} for i in word]
    attempt(hide, word, life)


if __name__ == '__main__':
    run()
