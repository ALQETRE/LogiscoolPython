import pandas
import numpy


# Annual income per region:

# Prague Region
prague_region = [
    [850000, 920000, 780000, 1100000, 980000, 870000, 1020000, 940000, 890000, 995000],  # Prague
    [600000, 640000, 590000, 630000, 610000, 650000, 580000, 620000, 670000, 600000]     # Říčany
]

# Plzeň Region
plzen_region = [
    [560000, 590000, 620000, 650000, 700000, 720000, 680000, 660000, 640000, 710000],    # Plzeň
    [480000, 500000, 520000, 540000, 560000, 580000, 590000, 600000, 610000, 620000]     # Klatovy
]

# South Bohemian (Jihočeský) Region
jihocesky_region = [
    [510000, 530000, 550000, 560000, 540000, 580000, 590000, 600000, 610000, 620000],    # České Budějovice
    [450000, 460000, 470000, 480000, 490000, 500000, 510000, 520000, 530000, 540000]     # Tábor
]


# === Tax Rules1 ===
# Prague: 21% -> *0.21
# Plzeň: 18% -> *0.18
# Jihočeský: 15% -> *0.15


def do_taxes1(region, rate):
    taxes = []
    for city in region:
        tax_per_city = []
        for person in city:
            tax = person / 100 * rate
            tax_per_city.append(tax)
        taxes.append(tax_per_city)
    return taxes


prague_taxes = do_taxes1(prague_region, 21)
plzen_taxes = do_taxes1(plzen_region, 18)
jihocesky_taxes = do_taxes1(jihocesky_region, 15)

for city in prague_taxes:
    print(city)

print()





# 850,000 CZK 21%    25%
# 1,000,000 CZK 35%

# === Tax Rules2 ===
# Prague Region:
#     - 21% for incomes up to 900,000 CZK
#     - 35% for incomes above 900,000 CZK
#
# Plzeň Region:
#     - 18% for incomes up to 650,000 CZK
#     - 25% for incomes above 650,000 CZK
#
# Jihočeský Region:
#     - 15% for incomes up to 600,000 CZK
#     - 22% for incomes above 600,000 CZK


def do_taxes2(region, rateL, rateH, limit):
    taxes = []
    for city in region:
        tax_per_city = []
        for person in city:
            if person > limit:
                tax = person / 100 * rateH
            else:
                tax = person /100 * rateL

            tax_per_city.append(tax)
        taxes.append(tax_per_city)
    return taxes


prague_taxes = do_taxes2(prague_region, 21, 35, 900000)
plzen_taxes = do_taxes2(plzen_region, 18, 25, 650000)
jihocesky_taxes = do_taxes2(jihocesky_region, 15, 22, 600000)

for city in prague_taxes:
    print(city)


print("\n")








def do_taxes_2(region, rate_high, rate_low, limit):
    taxes = []
    for city in region:
        tax_per_city = []
        for person in city:
            if person >= limit:
                tax = person * rate_high
            else:
                tax = person * rate_low
            tax_per_city.append(tax)
        taxes.append(tax_per_city)
        return taxes

prague_taxes = do_taxes_2(prague_region, 0.35, 0.21, 900000)
plzen_taxes = do_taxes_2(plzen_region, 0.25, 0.18, 650000)
jihocesky_taxes = do_taxes_2(jihocesky_region, 0.22, 0.15, 600000)

# print(prague_taxes)
# print(plzen_taxes)
# print(jihocesky_taxes)



def do_taxes2(region):
    taxes = []
    for city in region:
        tax_per_city = []
        for person in city:
            if person >= 900000:
               tax = person * 0.35
            else:
               tax = person * 0.21
            tax_per_city.append(tax)
        taxes.append(tax_per_city)

    return taxes



# === Tax Rules3 ===
#
# Prague Region:
#     - 21% for incomes up to 900,000 CZK
#     - 35% for incomes above 900,000 CZK
#     - Additional fixed fee: 10,000 CZK per person
#
# Plzeň Region:
#     - 18% for incomes up to 650,000 CZK
#     - 25% for incomes above 650,000 CZK
#     - Additional fixed fee: 8,000 CZK per person
#
# Jihočeský Region:
#     - 15% for incomes up to 600,000 CZK
#     - 22% for incomes above 600,000 CZK
#     - Additional fixed fee: 7,000 CZK per person


def do_taxes3(region, rateL, rateH, limit, fee):
    taxes = []
    for city in region:
        tax_per_city = []
        for person in city:
            if person > limit:
                tax = person / 100 * rateH
            else:
                tax = person /100 * rateL
            tax += fee
            tax_per_city.append(tax)
        taxes.append(tax_per_city)
    return taxes


prague_taxes = do_taxes3(prague_region, 21, 35, 900000, 10000)
plzen_taxes = do_taxes3(plzen_region, 18, 25, 650000, 8000)
jihocesky_taxes = do_taxes3(jihocesky_region, 15, 22, 600000, 7000)

for city in prague_taxes:
    print(city)


print("\n")







# Docházka:
# Chybý Patrik C.
# Všichni Presencne