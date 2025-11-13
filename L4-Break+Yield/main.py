# # Break:

# for cislo in range(1, 10):
#     if (cislo % 3 == 0) and (cislo % 2 == 0):
#         print(cislo, "je delitelny 3 a 2")
#         break
# print("hi")

# # Co dělá tento program? ^

# # 1 2 3 4 5 6


# i = 10
# while True:
#     i -= 1
#     print(i)
#     if i == 0:
#         break








# Chceme udělat funkci co bude přiřazovat ID


def get_id():
    id = 1
    while True:
        yield id
        id += 1

id_generator = get_id()

for i in range(50):
    print(next(id_generator))





# Min pouzijete 3 funkce tak aby meli aspon jeden return a brali argumenty





cislo1 = float(input("Zadej první číslo: "))
cislo2 = float(input("Zadej druhé číslo: "))


def soucet(a, b):
    return

vysledek = soucet(2, 3)
print("Součet je:", vysledek)









def secti_cisla(cislo1, cislo2):
    soucet = cislo1 + cislo2
    return soucet

number1 = float(input("Zadej první číslo: "))
number2 = float(input("Zadej druhé číslo: "))
vysledek = secti_cisla(number1, number2)

print("Součet je:", vysledek)




# Docházka:
#   David J.
#   Michael G.
#   Michal S.
#   Ondra A.
#   Milan N.
#   Patrik C.