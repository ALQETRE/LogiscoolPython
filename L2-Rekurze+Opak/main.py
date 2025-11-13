def loop(a):
    a += 1
    print(a)
    if a < 200:
        loop(a)

# loop(1)


# Fibbonaci sequance

# 0 1 1 2 3 5 8 13 21 34 ...
# posledni dvě cisla sum (+) a to je dalsi cislo


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(10))

n = 10

a = 0
b = 1
for i in range(n):
    a += b
    c = a
    a = b
    b = c

print(a)

# n -   0 1 2 3 4 5 6
# fib - 0 1 1 2 3 5 8






key = 3
msg = "Helloworld"
# Kho...



abc = "abcdefghijklmnopqrstuvwxyz"

def encrypt(msg, key):
    new_msg = ""
    for letter in msg.lower():
        i = abc.index(letter)
        i += key
        new_msg += abc[i%26]
    return new_msg

def decrypt(msg, key):
    new_msg = ""
    for letter in msg.lower():
        i = abc.index(letter)
        i -= key
        new_msg += abc[i%26]
    return new_msg

encrypted_msg = encrypt("Supertajnazprava", 12)
print(encrypted_msg)
msg = decrypt(encrypted_msg, 12)
print(msg)


# Docházka:

# Milan N.
# Ondřej A. (online)
# Michal S. (online)
# Michael G. (online)