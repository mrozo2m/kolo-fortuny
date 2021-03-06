"""print("Podaj kategorię hasła")
category = input()
print("Podaj hasło")
password = input()"""
category = "marka samochodu"
password = "mercedes"

password_blind = ''
for i in range (0,len(password)):
    password_blind = password_blind + chr(95)

while password != password_blind:
    print('==========================================================')
    print("Hasło do odgadnięcia", password_blind, "Kategori", category)
    j = 0
    hit = 0
    print('Podaj literę z hasła lub odgaduj hasło')
    quess = input()
    if quess == password:
        print('Brawo ! Odgadnięte hasło to:', password)
        break
    else:
        for i in password:
            j = j + 1
            if quess == i:
                password_blind = password_blind[:j-1] + quess + password_blind[j:]
                hit = 1
    if hit > 0:
        print("Tarfiłeś")
    else:
        print('Pudło')

print('Brawo ! Odgadnięte hasło to:', password)





