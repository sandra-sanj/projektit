# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä
# vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat
# merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.


month_number = int(input('Input month number: '))

seasons = ('winter', 'winter', 'spring', 'spring', 'spring', 'summer',
           'summer', 'summer', 'fall', 'fall', 'fall', 'winter')
season_for_month = seasons[month_number - 1]

print(f'Month {month_number} is part of {season_for_month} season')
