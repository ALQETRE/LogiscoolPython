def add_tax(price, tax):
    final_price = price + (price * tax)
    return final_price

def add_discount(price, discount):
    final_price = price - (price * discount / 100)
    return final_price

def calc_price(price, discount= 0):
    final_price = add_tax(price, 0.2)
    final_price = add_discount(final_price, discount)
    return final_price

print(calc_price(100)) # -> 120