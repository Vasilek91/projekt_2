"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petr Novotný
email: hornstr@seznam.cz
discord: vasilek91_82724
"""

import random
from datetime import datetime, timedelta

oddelovac = '-----------------------------------------------'
pozdrav = 'Hi there!'
uvod = '''I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.'''

def vypis_uvod():
    print(f'{oddelovac}\n{pozdrav}\n{oddelovac}\n{uvod}\n{oddelovac}')

def generuj_kod():
    return ''.join(map(str, random.sample(range(1, 10), k=4)))

def validuj_vstup(hrac_cislo):
    if len(hrac_cislo) != 4:
        print('Enter four digit number')
        return False
    if not hrac_cislo.isnumeric():
        print('Enter four digit number')
        return False
    if hrac_cislo[0] == '0':
        print('Enter four digit number, no zero at the start')
        return False
    if len(set(hrac_cislo)) < 4:
        print('Enter four digit number with unique numbers')
        return False
    return True

def ziskej_hracske_cislo():
    while True:
        hrac_cislo = input('Enter a number: ')
        if validuj_vstup(hrac_cislo):
            return hrac_cislo

def vyhodnot_hru(hrac_cislo, kod_1):
    zip_kodu = tuple(zip(hrac_cislo, kod_1))
    bulls = sum(x == y for x, y in zip_kodu)
    cows = sum(hrac_cislo.count(z) for z in kod_1) - bulls
    return bulls, cows

def tiskni_vysledek(bulls, cows):
    if bulls == 1 and cows == 1:
        print(bulls, 'bull', cows, 'cow')
    elif bulls == 1:
        print(bulls, 'bull', cows, 'cows')
    elif cows == 1:
        print(bulls, 'bulls', cows, 'cow')
    else:
        print(bulls, 'bulls', cows, 'cows')

def hra():
    kod_1 = generuj_kod()
    pokusy = 0
    start_time = datetime.now()
    print(kod_1)  # tento řádek můžeš odstranit nebo zakomentovat, pokud nechceš zobrazovat kód při vývoji

    while True:
        pokusy += 1
        hrac_cislo = ziskej_hracske_cislo()
        bulls, cows = vyhodnot_hru(hrac_cislo, kod_1)
        if bulls == 4:
            print(f'''{oddelovac}\nCorrect, you've guessed the right number in {pokusy} {'guess' if pokusy == 1 else 'guesses'}.''')
            end_time = datetime.now()
            doba_trvani = end_time - start_time
            doba_trvani_zaokr = doba_trvani - timedelta(microseconds=doba_trvani.microseconds)
            doba_string = str(doba_trvani_zaokr)
            print(f'Duration of a try: {doba_string}')
            historie_pokusu.append((datetime.now().strftime('%Y-%m-%d %H:%M:%S'), pokusy, doba_string))
            break
        else:
            tiskni_vysledek(bulls, cows)

def zobrazit_historii():
    print(f'{oddelovac}\nGame History\n{oddelovac}')
    if historie_pokusu:
        for zaznam in historie_pokusu:
            print(f'Date: {zaznam[0]}, Attempts: {zaznam[1]}, Duration: {zaznam[2]}')
    else:
        print('No history available.')
    print(oddelovac)


historie_pokusu = []
vypis_uvod()

while True:
    hra()
    zobrazit_historii()
    while True:
        nova_hra = input('Do you want to play again? (yes/no): ').lower()
        if nova_hra in ['yes', 'no']:
            break
        print('Please enter "yes" or "no".')

    if nova_hra == 'no':
        print('Thanks for playing!')
        break
    else:
        print('''\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game.\n''')