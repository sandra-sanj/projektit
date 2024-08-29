year = int(input('Syötä vuosi: '))

leap_year = False

if year % 4 == 0:
    leap_year = True

    if year % 100 == 0 and year % 400 == 0:
        leap_year = True
    elif year % 100 == 0 and year % 400 != 0:
        leap_year = False

if leap_year:
    print(f'{year} on karkausvuosi')
else:
    print(f'{year} ei ole karkausvuosi')

