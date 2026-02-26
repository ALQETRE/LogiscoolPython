import csv
import pandas as pd
import matplotlib.pyplot as plt


def read_csv(show_names= False):
    with open("files\\oscar_age_female.csv", mode= "r", encoding= "utf-8", newline="") as fd:
        reader = csv.reader(fd)
        
        if not show_names:
            next(reader)

        for line in reader:
            print( line )

# read_csv(show_names= True)


data = pd.read_csv("files\\oscar_age_female.csv", skipinitialspace=True, quotechar= "\"", usecols= ["Age", "Year"])
# print(data.max())


# s = pd.Series([10, 5, 30, 20])
# print(s.idxmax())


# nejstarsi = data.loc[ data["Age"].idxmax() ]
# print(nejstarsi)

# nejstarsi = data.loc[ data["Age"] == data["Age"].max() ]
# print(nejstarsi)


# sr = pd.Series([1, 2, 3, 4, 5])
# sr2 = pd.Series(["A", "B", "C", "D", "E"])


# idx = sr == 5
# print(idx)
# print(sr2.loc[idx])


data.plot(x= "Year", y= "Age", kind= "scatter")
plt.title("Age-Year-Graf")
plt.show()

data["Age"].value_counts().plot(kind="pie")
plt.title("Age Distribution")
plt.show()











# Docházka:
#  Chybí Antoňů O., Cichra P.
#  Ostatní online
#  Navíc Beneš G.