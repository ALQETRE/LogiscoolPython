# def add(a: int, b: int) -> int:
#     output = a + b
#     return output, 10



# output_a, cislo = add(2, 6)
# print(output_a)
# print(cislo)


def total_cena(cena, pocet= 10):
    return pocet * cena

print(total_cena(18.9))
print(total_cena(10.9))
print(total_cena(99.9))
print(total_cena(4.9, pocet= 20))


def loop(a):
    a += 1
    print(a)

    if a < 100:
        loop(a)


loop(1)


def fib(n):
    if n < 2:
        return n

    return fib(n-1) + fib(n-2)

# print(fib(10))

a = 0
b = 1
c = 0

for i in range(20000):
    c = b
    b += a
    a = c
print(b)