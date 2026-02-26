import pandas as pd
import numpy as np

# drop unnecesary column
# re-indexing the data
# clean columns - str()
# renaming columns
# skip rows


# Task 1 - Read data and ignore columns we don't need
pd.set_option('display.max_columns', None)  # pd.options.display.max_columns = None
pd.set_option('display.max_rows', None)  # pd.options.display.max_rows = None
# drop ignores while reading it, pop removes columns totally from csv - copy csv before using pop

def read_data():
    library = pd.read_csv("library.csv")
    print(library.head(5))
    print("------------------------------------------------------------------")
    library = library.drop(["Edition Statement", "Corporate Contributors", "Corporate Author", "Contributors", "Former owner",
                  "Engraver", "Issuance type"], axis=1)
    # inplace - if true do operations inplace and returns None
    # 0 = index (row), 1 = label (column)
    print(library.head(5))
    library = library.drop(columns=["Shelfmarks"]) # with columns parameter we don't need the axis
    print("------------------------------------------------------------------")
    print(library.head(5))
# read_data()


# Task 2 - Re-indexing data
def indexing_data():
    library = pd.read_csv("library.csv")
    print(library["Identifier"].is_unique) # check if all ids are unique
    library = library.set_index("Identifier")
    print(library.head())
# indexing_data()


# Task 3 - Read data in a row
def row_data(index):
    library = pd.read_csv("library.csv")
    library = library.set_index("Identifier")
    print(library.loc[index])
# row_data(206)


def row_data2(row):
    library = pd.read_csv("library.csv")
    library = library.set_index("Identifier")
    print(library.iloc[row])
# row_data2(206)


# Task 4 - Clean specific columns
def clean_date():
    library = pd.read_csv("library.csv")
    library = library.set_index("Identifier")
    print(library.loc[1982:, "Date of Publication"].head(20))
    extr = library['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
    library['Date of Publication'] = pd.to_numeric(extr)
    print(library.loc[1982:, "Date of Publication"].head(20))
# Task 5 - Remove NaN values by changing them to average
    print(library['Date of Publication'].isnull().sum() / len(library))  # rate of Nan values
    avg = round(library['Date of Publication'].mean())
    library["Date of Publication"] = library["Date of Publication"].fillna(avg)
    print(library.loc[1982:, "Date of Publication"].head(20))
# clean_date()


# Task 6 - Clean up the place of publication
def clean_place():
    library = pd.read_csv("library.csv")
    library = library.set_index("Identifier")
    print(library['Place of Publication'].head(10))
    london = library['Place of Publication'].str.contains('London')
    oxford = library['Place of Publication'].str.contains('Oxford')
    plymouth = library['Place of Publication'].str.contains('Plymouth')
    library['Place of Publication'] = np.where(london, 'London',
                                               np.where(oxford, 'Oxford',
                                               np.where(plymouth, 'Plymouth',
                                               library['Place of Publication'].str.replace('-', ' '))))
    print(library['Place of Publication'].head(40))
# clean_place()


# Task 7 - Book from 1892, London
def specific_book():
    library = pd.read_csv("library.csv")
    library = library.set_index("Identifier")
    find = library.loc[library["Date of Publication"] == '1892']
    find2 = find.loc[library["Place of Publication"] == 'London']
    print(len(find2)) # ti see how many books match with these settings
    print(find2["Title"])
# specific_book()


# Task 8 - Rename columns
def rename_columns():
    olympics = pd.read_csv("olympics.csv", header=1)
    print(olympics.head(10))
    olympics.rename(columns={'Unnamed: 0': 'Country',
                             '? Summer': 'Summer Olympics',
                             '01 !': 'S_Gold',
                             '02 !': 'S_Silver',
                             '03 !': 'S_Bronze',
                             'Total': 'S_Total',
                             '? Winter': 'Winter Olympics',
                             '01 !.1': 'W_Gold',
                             '02 !.1': 'W_Silver',
                             '03 !.1': 'W_Bronze',
                             'Total.1': 'W_Total',
                             '? Games': '# Games',
                             '01 !.2': '#Gold',
                             '02 !.2': '#Silver',
                             '03 !.2': '#Bronze'}, inplace=True)
    print(olympics.head(10))
rename_columns()