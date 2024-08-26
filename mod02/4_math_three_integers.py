integer1 = int(input('Syötä kokonaisluku 1: '))
integer2 = int(input('Syötä kokonaisluku 2: '))
integer3 = int(input('Syötä kokonaisluku 3: '))

sum_this = integer1 + integer2 + integer3
multiplication = integer1 * integer2 * integer3
average = (integer1 + integer2 + integer3) / 3

print(f'Lukujen {integer1}, {integer2} ja {integer3} summa on {sum_this}')
print(f'Lukujen {integer1}, {integer2} ja {integer3} tulo on {multiplication}')
print(f'Lukujen {integer1}, {integer2} ja {integer3} keskiarvo on {average:.1f}')
