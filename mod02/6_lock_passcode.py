import random


three_int_code = ''
for _ in range(3):
    three_int_code += str(random.randint(0, 9))
print(f'Kolmenumeroinen koodi: {three_int_code}')


four_int_code = ''
for _ in range(4):
    four_int_code += str(random.randint(1, 6))
print(f'Nelinumeroinen koodi: {four_int_code}')
