# ages = {
#     "Alice": 25,
#     "Bob": 16,
#     "Clara": 34,
# }

# print( ages["Bob"] )

# ages["Bob"] += 1

# print( ages["Bob"] )

# ages["Derek"] = 0

# print(ages)
# print()

# for a, b in ages.items():
#     print(f"{a} - {b}")

# print()

# .keys()    klíče   (jména)
# .values()  hodnoty (věky)
# .items()   oboje   (jmena, věky)



# ages = {
#     "Alice": 25,
#     "Bob": 16,
#     "Clara": 34,
#     "Alice": 85,
# }

# print( ages )



students = {
    "Alice": [1, 2],
    "Bob": [2, 1],
    "Clara": [3, 2],
    "Derek": [5, 4],
}

def show_grades():
    for name in students.keys():
        grades = students[name]
        print(f"{name} - {grades}")

def add_marks(marks):
    for value, mark in zip(students.values(), marks):
        value.append(mark)


marks = [1, 1, 2, 3]
add_marks(marks)
show_grades()





















# Docházka:
#   Patrik C.
#   Milan N.
#   Michal S.
#   Michael G.
#   David J. 