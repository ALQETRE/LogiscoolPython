import pandas as pd
# pip install pandas


df = pd.DataFrame(
    [
        [1, 2, 3],
        [4, 5, 6],
        ["A", "b", "c"]
    ]
)

# print(df)

df.to_csv("table.csv", index= False, header= False)


df1 = pd.read_csv("example.csv", skipinitialspace= True, header= 0)


# print(df1)
























knizky = ["A", "B", "C"]
autori = ["Capek", "Autor2", "Autor3"]

knihovna = {
    "A": "Capek",
    "B": "Autor2"
}

def add_book(name, autor):
    knizky.append(name)
    autori.append(autor)

def remove_book(name):
    if not name in knizky:
        return

    idx = knizky.index(name)

    autori.pop(idx)
    knizky.pop(idx)

add_book("D", "Autor2")
add_book("E", "Capek")

remove_book("F")

print(knizky)
print(autori)