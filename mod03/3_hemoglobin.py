biological_gender = input('Syötä biologinen sukupuoli: ')

if biological_gender not in ('nainen', 'mies'):
    print('Biologinen sukupuoli ei ole mies tai nainen.')
    exit()

hemoglobin = int(input('Syötä hemoglobiiniarvo (g/l): '))

high_hemoglobin_border = 0
low_hemoglobin_border = 0

women_high_hemoglobin_border = 175
women_low_hemoglobin_border = 117

men_high_hemoglobin_border = 195
men_low_hemoglobin_border = 134

if biological_gender == 'nainen':
    high_hemoglobin_border = women_high_hemoglobin_border
    low_hemoglobin_border = women_low_hemoglobin_border

elif biological_gender == 'mies':
    high_hemoglobin_border = men_high_hemoglobin_border
    low_hemoglobin_border = men_low_hemoglobin_border


if hemoglobin > high_hemoglobin_border:
    print('Hemoglobiini on korkea.')
elif low_hemoglobin_border <= hemoglobin <= high_hemoglobin_border:
    print('Hemoglobiini on normaali.')
elif hemoglobin < low_hemoglobin_border:
    print('Hemoglobiini on alhainen.')
