# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma,
# jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.


def get_list_content_sum(numbers):
    return sum(numbers)

list_of_numbers = [1, 5, 3, 9, 4, 2, 11]  # 35
list_sum = get_list_content_sum(list_of_numbers)
print(list_sum)
