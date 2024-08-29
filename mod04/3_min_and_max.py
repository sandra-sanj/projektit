# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon
# lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.


numbers = []

number = None
while number != '':
    number = input('Syötä luku: ')

    if number.isnumeric():
        numbers.append(float(number))

print(f'Pienin luku {min(numbers)}')
print(f'Suurin luku {max(numbers)}')
