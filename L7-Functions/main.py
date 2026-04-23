
def greet(jmeno, den):
    print(f"Ahoj, {jmeno}")
    print(f"Dnes je {den}")
    print()

greet("Alice", "Čtvrtek")
greet("Bobe", "Středa")
greet("Claro", "Pondělí")


def calc_speed(speed_limit):
    return speed_limit * 0.8

def calc_travel(time, speed_limit= 50, traffic= False):
    speed = calc_speed(speed_limit)
    if traffic:
        speed /= 2
    dist = speed * time
    return dist, speed

dist, speed_of_travel = calc_travel(3, traffic= True, speed_limit= 100)
print(dist)
print(speed_of_travel)



studenti = ["Alice", "Bob", "Clara"]
znamky = [
    [1, 3, 2, 1],
    [2, 5, 4],
    [2, 2, 3]
]


def prumer_studenta(jmeno):
    idx = studenti.index(jmeno)
    prumer = sum(znamky[idx]) / len(znamky[idx])
    return prumer

prumer = prumer_studenta("Bob")
print(prumer)

def prumer_tridy():
    total = 0
    for student in studenti:
        total += prumer_studenta(student)

    return total / len(studenti)

prumer = prumer_tridy()
print(prumer)

def ukaz_student(jmeno):
    prumer = prumer_studenta(jmeno)
    idx = studenti.index(jmeno)
    print(f"Jméno: {jmeno}")
    print(f"Známky: {znamky[idx]}")
    print(f"Průměr: {prumer}")
    print()

ukaz_student("Clara")