inches = float(input('Syötä tuumat: '))

while inches >= 0:
    cm = inches * 2.54
    print(f'{inches} tuumaa on {cm} cm')

    inches = float(input('Syötä tuumat: '))

print('Syötit negatiivisen luvun. Ohjelma lopetti.')
