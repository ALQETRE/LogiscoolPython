# int   -> celá čísla 10
# float -> desetiná čísla 1.3
# str   -> text
# bool  -> True/False
# list  -> [1, True, "Ahoj"]
# tuple -> ("10",) ("10", 1, False)
# dict  -> Slovníky 

{"age": 10, "name": "bob"}


# input("Heslo: ")

# input()

# input() -> STRING!


# int("123") -> 123

cislo_v_textu = "123"
print( int(cislo_v_textu) * 2 )


# str(123456789) -> "123456789"

# float(10) -> 10.0

print(int(12.3))

# list( (1, 2, 3) ) -> [1, 2, 3]

# bool(0) -> Flase

print(bool(2345678))

# tuple([1, 2, 3]) -> (1, 2, 3)


print(len("Ahoj")) # 4 (Length - Délka)

print(len([1, 2, 3])) # 3


text = "Students who have reached the third\nsemester of the Python course are already wondering if they are ready to take the exam. Well, for the rest of the semester, we’re going to work on practicing everything we’ve learned so far and taking shorter practice exams several times."

word_list = text.split()

print(len(text))
print(len(word_list))

text2 = "...".join(word_list)

print(text2)



print("ahoj" in word_list)


print(max([1, 2, 3], [10, -10]))

num = 15.1234567890
print(round(num, 3))

print(sum([1, 2, 3]))


