cabin = input('Syötä hyttiluokka (LUX, A, B, C): ')

if cabin == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif cabin == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif cabin == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif cabin == 'C':
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka.')
