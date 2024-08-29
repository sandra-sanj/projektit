index = 1
numbers_divided_by_three = []

while index <= 1000:
    if index % 3 == 0:
        numbers_divided_by_three.append(index)
    index += 1

print(f'Kolmella jaolliset numerot välillä 1..1000: \n{numbers_divided_by_three}')
