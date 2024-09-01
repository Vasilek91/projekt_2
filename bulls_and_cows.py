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

#vypíše úvodní pozdrav
def vypis_uvod():
    print(f'{oddelovac}\n{pozdrav}\n{oddelovac}\n{uvod}\n{oddelovac}')

#generuje unikátní kód, s ošetřením 0 na začátku a neopakování číslic
def generuj_kod():

    kod1 = random.sample(range(1, 10), 1)
    kod2 = list(range(0,10))
    kod2.remove(kod1[0])
    kod2 = random.sample(kod2,3)
    
    return ''.join(map(str,(kod1+kod2)))

#sbírá číslo hráče, spajo s funkcí validuj vstup
def ziskej_hracske_cislo():
    while True:
        hrac_cislo = input('Enter a number: ')
        if validuj_vstup(hrac_cislo):
            return hrac_cislo


#oveří jestli hráč zadává validní vstup, spajo s funkcí ziskej_hracske_cislo
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

#vyhodnocuje počet bulls a cows
def vyhodnot_hru(hrac_cislo, kod):
#    zip_kodu = tuple(zip(hrac_cislo, kod)
    bulls = sum(x == y for x, y in zip(hrac_cislo, kod))
    cows = sum(x in kod for x in hrac_cislo) - bulls
    return bulls, cows

#tiskne výsledek s ohledem na množné číslo slov bulls a cows
def tiskni_vysledek(bulls, cows):
    print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")


#samotná hra
def hra():
    kod = generuj_kod()
    pokusy = 0 #pro počítání pokusů na uhádnutí čísla
    start_time = datetime.now() #ukládá okamžik stratu hry
    print(kod)  # tento řádek můžeš odstranit nebo zakomentovat, pokud nechceš zobrazovat kód při vývoji

    while True:
        pokusy += 1 #když se začně hrát zvýší počet pokusů při neuhádnutém pokusu
        hrac_cislo = ziskej_hracske_cislo()
        bulls, cows = vyhodnot_hru(hrac_cislo, kod)
        if bulls == 4:
            print(f'''{oddelovac}\nCorrect, you've guessed the right number in {pokusy} {'guess' if pokusy == 1 else 'guesses'}.''')
            end_time = datetime.now() #získává okamžik správného uhodnutí kódu
            doba_trvani = end_time - start_time
            doba_trvani_zaokr = doba_trvani - timedelta(microseconds=doba_trvani.microseconds)
            doba_string = str(doba_trvani_zaokr)
            print(f'Duration of a try: {doba_string}')
            historie_pokusu.append((datetime.now().strftime('%Y-%m-%d %H:%M:%S'), pokusy, doba_string))
            break
        else:
            tiskni_vysledek(bulls, cows)

#zobrazuje historii
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

#funkce pro dotaz zda chce hráč hrát dál
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
