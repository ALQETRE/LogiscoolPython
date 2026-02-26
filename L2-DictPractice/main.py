# Review:

muj_dict = {
    "Alice": 10, # <- Can be any type, even another dict -> "Alice": {"Age": 10, "Male?": False}
    "Bob": 54,
    "Clara": 28
}

muj_dict.keys() # -> ["Alice", "Bob", "Clara"]
muj_dict.values() # -> [10, 54, 28]
muj_dict.items() # -> [ ("Alice", 10), ("Bob", 54), ("Clara", 28)]

muj_dict["Bob"] # -> 54
muj_dict["Deril"] = 89 # -> Creates Deril and sets it to 89

for name, age in muj_dict.items(): # <- muj_dict.keys() / muj_dict.values() / muj_dict.items()
    pass
    # Itterates over both keys and values

