# print("Case1:")


# while True:
#     try:
#         x = int(input("   Number 1: "))
#         break
#     except ValueError as e:
#         pass

# print()

# while True:
#     try:
#         y = int(input("   Number 2: "))
#         if y != 0:
#             break
#     except ValueError as e:
#         pass

# print("  ", x / y)


# while True:
#     try:
#         cislo = int(input("Cislo: "))
#         break
#     except ValueError as e:
#         pass

# print(f"Your num*2 is: {cislo*2}")






























# print("Case2:")
# data = {"value": "42.5"}
# result = int(data["value"])
# print(f"   {result}")


# print("Case3:")
# def average(numbers: list):
#     return sum(numbers) / len(numbers)

# print("  ", average( [1, 2, 3] ))
# # print("  ", average( ["A", "B", "C"] ))
# print("  ", average( [] ))










# int("abc") # -> ValueError

# list = ["A", "B", "C"]
# list["hello"] # -> TypeError

# 123456 / 0 # -> ZeroDivisionError

# prin("hello") # -> NameError

# whil True:      # -> SyntaxError
#     print("Hi")

# msg = "Hello World"
# print(msg.lowe()) # -> AttributeError




# try:
#     cislo = input("Enter a number: ")
#     cislo = int(cislo)
#     print(1/cislo)

# except ValueError as e:
#     print("Number was not entered")

# # except ZeroDivisionError as e:
# #     print("You cant divide by zero")

# # except Exception as e:
# #     print(e)

# else:
#     print("Bum")

# finally:
#     print("End")

# print("Hii")




# Colpiled:

# program.cs -> program.exe -> run
#            ^
#         Compiler (Windows 10, Win11, Linux, MacOS)


# Interpreted:

# main.py  -> machine code
#          ^
#       Run time (Interpreter -> VM)


class MujTyp(Exception): pass

raise TypeError("Moje prvni chyba")