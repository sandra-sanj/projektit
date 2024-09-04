# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.


number = int(input('Syötä kokonaisluku: '))

is_prime_number = True
if number <= 1:
    is_prime_number = False

for num in range(2, number - 1):
    if number % num == 0:
        is_prime_number = False

print(f'Luku {number} {"on" if is_prime_number else "ei ole"} alkuluku.')
