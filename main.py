import random
import time

category = input('Podaj kategorię hasła ')
password = input('Podaj hasło ')
print('\n\n\n\n\n')

whell = [100, 150, 200, 250, 300, 350, 400, 500, 750, 1000, 1500, 2000, 2500, 3000, 5000, 'Bankrut', 'Bankrut']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','ł','m','n','o','p','r','s','t','u','w','y','z','ą','ć','ń','ż','ź','x','ó']
player_points = 0
password_blind = ''
for i in range(0,len(password)):
    password_blind = password_blind + chr(95)

while password != password_blind:
    print('\n==========================================================')
    print("Kategoria:", category, '  Punkty:', player_points)
    print("Hasło do odgadnięcia:", password_blind)
    print('==========================================================')
    draw = random.choice(whell)
    print('Kręcisz kołem ...')
    time.sleep(2)
    print('koło zatrzymało się na:', draw)
    if draw == 'Bankrut':
        player_points = 0
        continue
    j = 0
    hit = 0
    print('Podaj literę z hasła lub odgaduj hasło')
    quess = input()
    if len(quess) > 1 and quess == password:
        print('Brawo ! Odgadnięte hasło to:', password)
        player_points = player_points + draw
        break
    else:
        if quess in alphabet:
            for i in password:
                j = j + 1
                if quess == i:
                    password_blind = password_blind[:j-1] + quess + password_blind[j:]
                    player_points = player_points + draw
                    hit = 1
            alphabet.remove(quess)
        elif len(quess) == 1:
            print("Litera", quess, "już była użyta - wybierz inną")
        else:
            print("Nie prawidłowe hasło")
    if hit > 0:
        print("Tarfiłeś")

print('Brawo ! Odgadnięte hasło to:', password)
print('Twój wynik to:', player_points)