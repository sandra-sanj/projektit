# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

username = 'python'
password = 'rules'

total_guesses = 5
used_guesses = 0

while used_guesses < 5:
    username_input = input('Syötä käyttäjätunnus: ')
    password_input = input('Syötä salasana: ')

    used_guesses += 1

    if username_input == username and password_input == password:
        print('Tervetuloa')
        break
    elif (username_input != username or password_input != password) and used_guesses < 5:
        print(f'Käyttäjätunnus tai salasana on väärin. Voit kokeilla vielä {total_guesses - used_guesses} kertaa')

else:
    print('Pääsy evätty')