from enum import Enum


# Review:

muj_dict = {
    "Alice": 10, # <- Can be any type, even another dict -> "Alice": {"Age": 10, "Male?": False}
    "Bob": 54,
    "Clara": 28
}

muj_dict.keys() # -> ["Alice", "Bob", "Clara"]
muj_dict.values() # -> [10, 54, 28]
muj_dict.items() # -> [ ("Alice", 10), ("Bob", 54), ("Clara", 28) ]

muj_dict["Bob"] # -> 54
muj_dict["Deril"] = 89 # -> Creates Deril and sets it to 89

muj_dict.pop("Alice") # -> 10 and removes "Alice"

for name, age in muj_dict.items(): # <- muj_dict.keys() / muj_dict.values() / muj_dict.items()
    pass
    # Itterates over both keys and values


class Gender(Enum):
    Male = 0,
    Female = 1,
    Other = 2


# Občan:
#  - ID (Unique)
#  - Jména
#  - Přímení
#  - Věk
#  - Pohlaví (M/Ž)

db = {
    0: {"Jméno": "Alice", "Přímení": "Nováková", "Věk": 53, "Pohlaví": Gender.Female},
    1: {"Jméno": "Bob", "Přímení": "Suchý", "Věk": 12, "Pohlaví": Gender.Male}
}

def add_person(id, name, surname, age, gender):
    data = {"Jméno": name, "Přímení": surname, "Věk": age, "Pohlaví": gender}
    db[id] = data

def print_person(id):
    data = db[id]

    gender = ""
    if data["Pohlaví"] == Gender.Female:
        gender = "Žena"
    elif data["Pohlaví"] == Gender.Male:
        gender = "Muž"
    elif data["Pohlaví"] == Gender.Other:
        gender = "Jiné"

    print(f"#{id} - {data['Jméno']} {data['Přímení']} ({data['Věk']} let), Pohlaví {gender}.")

add_person(2, "Clara", "Bílá", 37, Gender.Female)
print(db)

print_person(1)










