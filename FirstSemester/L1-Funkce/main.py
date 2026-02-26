def add():
    cislo_a = int(input("Cislo a: "))
    cislo_b = int(input("Cislo b: "))
    ans = cislo_a + cislo_b
    print(ans)

# add() # <- Důležité, aby se to spustilo

def add_with_args(cislo_a, cislo_b):
    print(cislo_a + cislo_b)

add_with_args(6, 12)



def ukol2(cislo_ve_str):
    cislo = int(cislo_ve_str)
    cislo += 5
    delka = len(str(cislo))
    print(delka)

# ukol2("123") # 123+5 -> 128 -> 3
# ukol2("996") # 996+5 -> 1001 -> 4


def ukol3(cislo_ve_str, a= "Hello World!", hodnota_navic= 5):
    cislo = int(cislo_ve_str)
    cislo += hodnota_navic
    delka = len(str(cislo))
    print(a)
    print(delka)

# ukol3("123") # 123+5 -> 128 -> 3
# ukol3("996", hodnota_navic= 6) # 996+5 -> 1001 -> 4

def objednavka(price, amount= 10):
    total = price*amount
    if total < 0:
        return 0
    else:
        return total
    
    print("ahoj")

# total1 = objednavka(10.99) # -> -109.9
# print(objednavka(10.99, amount= 11)) # -> 120.89

# print(total1)

# litre/100km
# miles/gallon

# l * 3,7 = G
# G / 3,7 = l

# km * 0,6 = mi
# mi / 0,6 = km

# 1/litry_na_100km = 100km_na_litry

def eu_to_us(litry_na_100km):
    galons_na_100km = litry_na_100km * 3.7
    hundredKM_na_galon = 1/galons_na_100km
    hundredMI_na_galon = hundredKM_na_galon * 0.6
    mile_na_galon = hundredMI_na_galon * 100
    return mile_na_galon

def us_to_eu(miles_na_galon):
    km_na_galon = miles_na_galon / 0.6
    galon_na_km = 1/km_na_galon
    litr_na_km = galon_na_km / 3.7
    litr_na_100km = litr_na_km * 100
    return litr_na_100km

# litry_na_100km_org = 30
# miles_na_galon = eu_to_us(litry_na_100km_org)
# print(miles_na_galon)
# litry_na_100km_new = us_to_eu(miles_na_galon)
# print(litry_na_100km_new)


def test():
    total = 10
    a = "ahoj"
    return total, a

total_ret, a_ret = test()

print(a_ret)
print(total_ret)

# Docházka:

# Michal S. (Online)
# David J. (Online)
# Ondřej A. (Byl Online, bude online ale je napsaný pres.)
# Milan N. (Byl Online, bude pres.)

# Začali jsme v čas ale spustil jsem to o 20min pozdě