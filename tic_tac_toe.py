"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petr Novotný
email: hornstr@seznam.cz
discord: vasilek91_82724
"""
print("""Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game
--------------------------------------------""")
oddelovac = '============================================'


seznam = ['','','','','','','','','']

zacina = 'X'

def zobrazit_desku(seznam):
    deska = ''
    for i in range(3):
        deska += '+---+---+---+\n'
        for j in range(3):
            if seznam[i*3+j] == '':
                deska += f'|   '
            else:
                deska += f'| {seznam[i*3+j]} '
        deska += '| \n'

    deska += '+---+---+---+'
    return deska

#přepnu hráče
def prepnout_hrace(zacina):
    if zacina == 'X':
        return 'O'
    else:
        return 'X'

def kontrola_vitezstvi(seznam):
    for i in range(0,9,3): #kontrola řádků
        if seznam[i] == seznam[i+1] == seznam[i+2] != '':
            print(f'Vyhrál {seznam[i]}')
            return True
    for i in range(3): #kontrola sloupců
        if seznam[i] == seznam[i+3] == seznam[i+6] != '':
            print(f'Vyhrál {seznam[i]}')
            return True
#kontrola \ diagonály
    if seznam[0] == seznam[4] == seznam[8] != '':
        print(f'Vyhrál {seznam[0]}')
        return True
 #kontrola / diagonály
    if seznam[2] == seznam[4] == seznam[6] != '':
        print(f'Vyhrál {seznam[2]}')
        return True
    return False

print(zobrazit_desku(seznam))
while True:

    if '' not in seznam:
        print('Remíza')
        break
    try:
        pozice = int(input(f'{oddelovac} \n Hráč {zacina} zadej pozici od 1 do 9: '))
        print(oddelovac)
        if pozice < 1 or pozice > 9:
            raise ValueError
        if seznam[pozice-1] != '':
            raise IndexError
        seznam[pozice-1] = zacina
        print(zobrazit_desku(seznam))

        zacina = prepnout_hrace(zacina)

        if kontrola_vitezstvi(seznam):
            break

    except ValueError:
        print('Prosím zadej číslo od 1 do 9')
    except IndexError:
        print('Tato pozice je již obsazena. Zkuste to znovu.')
