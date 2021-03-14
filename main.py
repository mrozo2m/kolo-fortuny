import random
import time

def blind (password):
    password_blind = ''
    for i in range(0, len(password)):
        password_blind = password_blind + chr(95)
    return password_blind

def show_game ():
    print('\n')
    print('==========================================================')
    print("Kategoria:", category, '  Punkty:', player_points)
    print("Hasło do odgadnięcia:", password_blind)
    print('==========================================================')

def turn_the_wheel ():
    draw = random.choice(wheel)
    print('Kręcisz kołem ...')
    time.sleep(1)
    print('koło zatrzymało się na:', draw)
    return draw

def check_pass (quess, password):
    if len(quess) > 1 and quess == password:
        return True
    else:
        return False

def check_consonant (quess, password, draw):
    global consonants, password_blind, player_points
    if quess in consonants:
        discovering_letters(quess, password, draw)
        consonants.remove(quess)
        show_game()
        if password_blind != password and player_points >= 200 and quess in password:
            buy_vowel(password, draw)
    elif len(quess) == 1:
        print("Spółgłoska", quess, "już była użyta lub nie jest to spółgłoska - wybierz inną nastepnym razem")
    else:
        print("Nie prawidłowe hasło")

def buy_vowel (password, draw):
    global vowels, password_blind, player_points, vowels_cost
    print('Czy chcesz wykupić samogłoskę t/n')
    k = input()
    if k == 't':
        show_game()
        print('Podaj samogłoskę z hasła')
        quess = input()
        if quess in vowels:
            discovering_letters(quess, password, draw)
            vowels.remove(quess)
            player_points = player_points - vowels_cost
        elif len(quess) == 1:
            print("Samogłoska", quess, "już była użyta lub nie jest to samogłoska - wybierz inną nastepnym razem")

def discovering_letters (quess, password, draw):
    global password_blind, player_points
    j = 0
    for i in password:
        j = j + 1
        if quess == i:
            password_blind = password_blind[:j - 1] + quess + password_blind[j:]
            if quess in consonants:
                player_points = player_points + draw

category = input('Podaj kategorię hasła ')
password = input('Podaj hasło ')
print('\n\n\n\n\n')

wheel = [100, 150, 200, 250, 300, 350, 400, 500, 750, 1000, 1500, 2000, 2500, 3000, 5000, 'Bankrut', 'Bankrut']
vowels = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'ó', 'y']
vowels_cost = 200
consonants = ['b','c','d','f','g','h','j','k','l','ł','m','n','p','r','s','t','w','z','ć','ń','ż','ź','x']
player_points = 0
password_blind = blind(password)

while password != password_blind:
    show_game()
    draw = turn_the_wheel()
    if draw == 'Bankrut':
        player_points = 0
        continue
    print('Podaj spółgłoskę z hasła lub odgaduj hasło')
    quess = input()
    if check_pass(quess, password):
        player_points = player_points + draw
        break
    else:
        check_consonant(quess, password, draw)
print('Brawo ! Odgadnięte hasło to:', password)
print('Twój wynik to:', player_points)