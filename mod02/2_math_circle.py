from math import pi


radius = float(input('Syötä ympyrän säde (m): '))
area = pi * radius ** 2
print(f'Ympyrän säteen ollessa {radius} m sen pinta-ala on {area:.1f} m^2')
