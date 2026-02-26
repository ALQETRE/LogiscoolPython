# cislo_dec = 9
# print(cislo_dec)

# cislo_bin = bin(cislo_dec)[2:]
# print(cislo_bin)

# cislo_dec = int(cislo_bin, 2)
# print(cislo_dec)

# print()
# for cislice in cislo_bin:
#     print(int(cislice))

# print("\n")





def bit_and(a, b):
    a_bin = bin(a)[2:]
    b_bin = bin(b)[2:]

    out = ""
    for i in range(len(a_bin)):
        a_dig = int(a_bin[i])
        b_dig = int(b_bin[i])
        if a_dig + b_dig == 2:
            out += "1"
        else:
            out += "0"
    return int(out, 2)

print(bit_and(12, 9))

# 1100
# 1001
# 1000 = 8