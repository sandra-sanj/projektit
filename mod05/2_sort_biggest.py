# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.


numbers = []

number = None
while number != '':
    number = input('Syötä luku: ')

    if number.isnumeric():
        numbers.append(int(number))

numbers.sort(reverse=True)

five_largest_numbers = []
for number in numbers:
    if numbers.index(number) < 5:
        five_largest_numbers.append(number)

print(f'Viisi suurinta numeroa: {five_largest_numbers}')
