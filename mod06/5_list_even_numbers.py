# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan,
# joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota
# ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def get_even_numbers(numbers_list):
    # save item from list to new list if item is even
    new_numbers_list = [number for number in numbers_list if number % 2 == 0]
    return new_numbers_list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
result = get_even_numbers(numbers)
print(f'Original list: {numbers}\nList with even numbers only: {result}')
