luoti = 13.3  # grammaa
naula = 32 * luoti
leiviska = 20 * naula

leiviska_input = float(input('Syötä leiviskät: '))
naula_input = float(input('Syötä naulat: '))
luoti_input = float(input('Syötä luodit: '))

leiviskat_grammoina = leiviska_input * leiviska
naulat_grammoina = naula_input * naula
luodit_grammoina = luoti_input * luoti

grammat_yhteensa = leiviskat_grammoina + naulat_grammoina + luodit_grammoina

kg = int(grammat_yhteensa // 1000)
g = grammat_yhteensa - (kg * 1000)
print(f'Massa syötettyjen mittojen mukaan on {kg} kilogrammaa ja {round(g, 2)} grammaa.')
