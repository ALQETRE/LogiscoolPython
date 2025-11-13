# %%
import pandas as pd

# %%
data = {
    "Name": ["Alan", "Bob", "Clara", "Dave"],
    "Age": [21, 10, 68, 13],
    "English": [True, False, False, True],
    "Place": ["Dejvice", "Smíchov", "Holešovice", "Barandov"],
    "Score": [100, 200, 150, 50]
}

df = pd.DataFrame(data, index= ["A", "B", "C", "D"])

df # <- Pokud používáme JupiterNotebook, tak můžeme jen napsat co chceme vytisknout

# %%
# Chceme získat pouze jména
# + jména a věk

df.loc[:, "Name"]

# %%
df["Name"]

# %%
# Chceme získat místo na řádku C
# + na řádku C a D

df.loc[["C", "D"], "Place"]

# %%
# Pouze řádky 1 a 2 

df.iloc[[1, 2]]

# %%
# Ukázat jenom řádky 1 a 2, ale za použití bool

df.loc[ [False, True, True, False] ]

# %%
# Vytisknout řádky se jménem Bob
# + Bob a Klára

df["Name"] == "Bob"

# %%
df.loc[  df["Name"] == "Bob"  ]

# %%
df["Name"]

# %%
df["Name"].isin( ["Bob", "Clara"] )


# %%
df.loc[  df["Name"].isin(["Bob", "Clara"])  ]

# %%
# Vytvoř nový sloupec Old který bude True pokud Age > 60

df["Old"] = df["Age"] > 60

df

# %%
# Přidej nový řádek s daty ["Eve", 18, True, "Řepy", 250, False]

len(df)

# %%
df.loc[len(df)] = ["Eve", 18, True, "Řepy", 250, False]
df

# %%
# Pomocí concat (Tohle je lepší)

new_row = pd.DataFrame({
    "Name": ["Frank"],
    "Age": [45],
    "English": [False],
    "Place": ["Břevnov"],
    "Score": [150],
    "Old": [False]
})

new_row

# %%
df = pd.concat([df, new_row])
df

# %%
# Vytvořte si DataFrame o alespoň 3 sloupcích
# + použijte na něj 3 různé filtry ( pomocí .loc .iloc nebo [] )


