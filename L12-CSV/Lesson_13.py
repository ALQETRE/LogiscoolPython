import csv
import pandas as pd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

# Task 1 - Open and read a csv file
def openCSV():
    csvfile = open("oscar_age_female.csv", newline='')
    data = csv.reader(csvfile, delimiter=" ")
    for row in data:
        print(' '.join(row))
# openCSV()


# Task 2 - Open a csv file with pandas module
def openWithPandas():
    csvfile = pd.read_csv("oscar_age_female.csv")
    print(csvfile.head(20))
# openWithPandas()


# Task 3 - Open specific columns
def openColumns():
    csvfile = pd.read_csv("oscar_age_female.csv", usecols=["Age", "Name"])
    print(csvfile.head(10))
    summ = csvfile["Age"].sum()
    rows = len(csvfile["Age"])
    avg = summ / rows
    print(summ)
    print("The average age of the winners is", round(avg, 2), "years.")
# openColumns()


# Task 4 - Find oldest winner
def oldestWinner():
    csvfile = pd.read_csv("oscar_age_female.csv", usecols=["Age", "Name"])
    max_age = max(csvfile["Age"])
    myRow = csvfile[csvfile["Age"] == max_age]
    print("The oldest winner is " + str(myRow.iloc[0, 0]) + " years old and she is" + str(myRow.iloc[0, 1]).replace("\"",""))
# oldestWinner()


# Task 5 - Find year of Fargo win
def fargoWin():
    csvfile = pd.read_csv("oscar_age_female.csv", usecols=["Year", "Movie"], skipinitialspace=True)
    myRow = csvfile[csvfile["Movie"] == "Fargo"]
    print(str(myRow.iloc[0, 1]) + " won the Oscar in " + str(myRow.iloc[0, 0]))
# fargoWin()


# Task 6 - Data of one row
def dataRow(row):
    csvfile = pd.read_csv("oscar_age_female.csv")
    myRow = csvfile.iloc[row]
    print(myRow)
# dataRow(5)

import matplotlib.pyplot as plt
# Task 7 - Plotting data
def plotData():
    csvfile = pd.read_csv("oscar_age_female.csv", usecols=["Year", "Age"])
    csvfile.plot(x="Year", y="Age", kind='scatter')
    plt.title("Year-Age graph")
    # plt.scatter(csvfile["Year"], csvfile["Age"])
    plt.show()
# plotData()


# Task 8 - Plotting data 2
def plotData2():
    csvfile = pd.read_csv("files\\oscar_age_female.csv", usecols=["Age"])
    piePlot = csvfile.value_counts()
    print(piePlot)
    piePlot.plot(kind='pie')
    plt.title("Rate of winners by age")
    plt.show()
plotData2()


# Task 9 - Number of p+% letters
def commonFreq(p):
    csvfile = pd.read_csv("letter_frequency.csv", skipinitialspace=True)
    number = 0
    for index, row in csvfile.iterrows():
        if row["Percentage"] >= p:
            number += 1
        print(row["Letter"], row["Percentage"])
    print(str(number) + " numbers have " + str(p) + "+% frequency.")
# commonFreq(4)


# Task 10 - Frequency of vowels
def vowelFreq():
    csvfile = pd.read_csv("letter_frequency.csv", skipinitialspace=True)
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    vowel = 0
    for index, row in csvfile.iterrows():
        if row["Letter"] in vowels:
            vowel += row["Percentage"]
    print(str(round(vowel, 2)) + "% is the frequency of vowels.")
# vowelFreq()


# Task 11 - Secret Santa
def secretSanta():
    csvfile = pd.read_csv("secret_santa.csv", skipinitialspace=True)
    new_csv = csvfile.sample(frac=1)
    new_csv.to_csv("secret_santa_final.csv")
    new_csvfile = pd.read_csv("secret_santa_final.csv", skipinitialspace=True)
    for i in range(len(new_csvfile["Name"])):
        if i != len(new_csvfile["Name"])-1:
            print(new_csvfile["Name"][i], "will give the present to", new_csvfile["Name"][i+1])
        else:
            print(new_csvfile["Name"][i], "will give the present to", new_csvfile["Name"][0])
secretSanta()
