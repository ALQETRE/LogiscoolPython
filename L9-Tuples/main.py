# Tuples!

# my_tuple = (1, 2, 3, 4) # <- Immutable
# print(my_tuple)

# my_list = [1, 2, 3] # <- Not immutable
# print(my_list)



# tuple2 = (4,)
# tuple3 = (4)

# print(type(tuple2))
# print(type(tuple3))


# for cislo in my_tuple:
#     print(cislo)

# print(my_list)
# tuple_from = tuple("abc")
# print(tuple_from)


# str_tuple = ("A", "B", "c")
# print(str_tuple)


# letter1, letter2, letter3 = str_tuple
# print(letter2)



# a = "ahoj"
# b = "svete"

# b, a = (a, b)

# print(a)
# print(b)



# jmena = ["alice", "bob", "clara"]
# tupleI2 = [(0, "alice"), (1, "bob"), (2, "clara")]



# ages = [20, 13, 18]
# sizes = [123, 456, 678]

# tupleI = [("alice", 20), ("bob", 13), ("clara", 18)]

# print(tupleI == list(zip(jmena, ages)))

# for i in range(len(jmena)):
#     jmeno = jmena[i]
#     age = ages[i]
#     print("Jmeno:", jmeno)
#     print("Age:", age)
#     print()

# Jm: alice
# Age: 20

# Jm: bob
# Age: 13

# Jm: clara
# Age: 18

# for jmeno, age, size in zip(jmena, ages, sizes):
#     print("Jmeno:", jmeno)
#     print("Age:", age)
#     print("Size:", size)
#     print()


# for a, b in [(1, 2), ("A", "B"), ("x", "y"), (True, False)]:
#     print(a)
#     print(b)
#     print()




# for idx, jmeno in enumerate(jmena):
#     print(f"{idx}, {jmeno}")







# my_list = [1, 2, 3]
# my_list[1] = 5
# print(my_list)

# my_tuple = (1, 2, 3)
# my_tuple[1] = 5
# print(my_tuple)









# print("Int: ")
# num = 1
# print(id(num))

# num += 1
# print(id(num))


# print()


# print("Str: ")
# text = "Hi"
# print(id(text))

# text += "!"
# print(id(text))


# print()


# print("List: ")
# table = [1, 2, 3]
# print(id(table))

# table.append(4)
# print(id(table))


# print()


# print("Tuple: ")
# info = ("bob", 20)
# print(id(info))

# info += ("hi",)
# print(id(info))















# print(f"Jmeno: {jmeno}, Age: {age}")





# zip()
# # or
# enumerate()






# list1 = ["Meta", "3"]
# list2 = ["Quest" , "S"]
# nameOfVR = zip(list1,list2)
# list3 = list(nameOfVR)
# print(list3)


# ukoly = [

#     "Uklidit pokoj",

#     "Nakrmit psa",

#     "Napsat domácí úkol",

#     "Připravit si věci do školy"

# ]
 
# splneno = []
 
# for i, u in enumerate(ukoly):

#     print(i+1, u)

#     hotovo = input("Hotovo? (ano/ne): ")

#     if hotovo == "ano":

#         splneno.append(u)
 
# print("\nSplněné úkoly:")

# for j, s in enumerate(splneno, start=1):

#     print(j, s)

 


# a = [1, 2, 3]
# b = ["a", "b", "c"]
# c = zip(a, b)
# print("zip():", list(c))


pracovnici = ("Adam", "Beda", "Cenda", "David", "Emil", "Fenda")
vydaje = (24000, 25000, 30000, 21000, 28000, 23000)

for zamestnanci, plat in zip(pracovnici, vydaje):
    print("Zaměstnanec:", zamestnanci)
    print("Má plat:", plat)
    print(f"Zaměstnanec {zamestnanci} má plat {plat}Kč.")
    print(" ")



# Docházka:
# Patrik C. (presencne)
# Ondrej A. (Chybí)
# Ostatní (Online)