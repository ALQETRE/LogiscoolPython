from random import randrange


# muj_list = [
#     1, 2, 3, 5, 2, 0, 7
# ]
# test = 2
# print( muj_list[test + 4] )

# muj_list.append(4) # Přidá nakonec
# print(muj_list)

# idx = muj_list.index(1)
# print(idx)

# hodnota = muj_list.pop(3)
# print(muj_list)
# print(hodnota)

# muj_list.remove(2)
# print(muj_list)

# muj_list.sort()
# print(muj_list)


# print("\n")

# matrix = [
#     [1, 2, 3, 4],
#     ["A", "B", "C", "D"],
#     [True, True, False, True],
#     [10.1, 20.2, 67.2, 54.9]
# ]

# for radek in matrix:
#     print(radek)


# number_matrix = []
# current_num = 1
# for y in range(10):
    
#     radek = []

#     for x in range(10):
#         radek.append(current_num)
#         current_num += 1

#     number_matrix.append(radek)



# for radek in number_matrix:
#     print(radek)


# # 10x10


# # Priklad 3x3 vysledek:
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print()


# number_matrix = []
# for y in range(10):
    
#     radek = []

#     for x in range(10):
#         radek.append(y*10 + x + 1)

#     number_matrix.append(radek)

# for radek in number_matrix:
#     print(radek)


number_matrix = []
for y in range(10):
    
    radek = []

    for x in range(10):
        radek.append(randrange(0, 10))

    number_matrix.append(radek)

for radek in number_matrix:
    print(radek)




print()
for radek in number_matrix:
    radek.sort()

number_matrix.sort()

for radek in number_matrix:
    print(radek)

# Docházka:
# vsichni
# patrik presencne