import pandas as pd
# pip install pandas


df = pd.DataFrame(
    [
        [1, 2, 3],
        [4, 5, 6],
        ["A", "b", "c"]
    ],
)

print(df)

df.to_csv("example2.csv", index= False, header= ["Sloupec1", "Sloupec2", "Sloupec3"])


df_read = pd.read_csv("example.csv", skipinitialspace= True, header= 0)
# df1 = pd.read_csv("example.csv", skipinitialspace= True, header= 0)

print(len(df_read.loc[2, "CisloB"]))
























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

remove_book("B")

# print(knizky)
# print(autori)