import pandas as pd

mydataset = {'cars':["BMW", "Volvo", "Ford"],
             'passings':[3,7,2]}
myvar = pd.DataFrame(mydataset)
print(myvar)


a = [1, 7, 2]
myvar2 = pd.Series(a) # serie zonder index, auto index 0, 1, 2 etc
print(myvar2)
print(myvar2[0]) # geeft eerste waarde in de series

myvar3 = pd.Series(a, index = ["x", "y", "z"]) # serie met index
print(myvar3)
print(myvar3["y"]) # zoek de waarde via index

# series maken met key/value object zoals een dictionary
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar4 = pd.Series(calories)
print(myvar4)

myvar5 = pd.Series(calories, index = ["day1", "day2"])  # alleen dag 1 en 2 selecteren
print(myvar5)

# dataframes

data = {"calories": [420, 380, 390],
  "duration": [50, 40, 45]}
myvar6 = pd.DataFrame(data)
print(myvar6)

# locate row
print(myvar6.loc[0])  # returned een series
print(myvar6.loc[[0, 1]])  # returned een dataframe, row 1 en 2

#named indexes
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
print(df.loc["day2"])

# dataframe syntax:
# https://www.w3schools.com/python/pandas/pandas_ref_dataframe.asp

# om meer rows te laten zien kun je de max rows aanpassen:
# pd.options.display.max_rows = 9999

print(df.head()) # eerste 5 rijen
print(df.tail()) # laatste 5 rijen
print(df.info())

# df2 = pd.read_csv(r'C/<locatie>', sep=';')

# rijen met lege cellen verwijderen. De hele rijen verdwijnen dan.
# returned een nieuw dataframe, verandert niet het  origineel. behalve als je .dropna(inplace = True)
# df.dropna()

# lege cellen vullen met een value.
# .fillna()
# .fillna(130)
# df["calories"].fillna(130, inplace = True) doet dit alleen in die kolom.

# .to_string of .to_html zijn heel handig

# wrong format en wrong data en removing duplicates  geskipt

# data correlations
# .corr() berekent de correlatie in je data set, tussen elke kolom. negeert niet numerieke kolommen.
# geeft uitkomst tussen 1 en -1. 1 en -1 zijn hele goede correlatie. dichter bij 0 heel slecht.
# vanaf 0.6 is best goede correlatie.

# grafieken met pandas maken
# .plot()
# met pyplot van matplotlib kun je meer tekenen. hier is ook een tutorial van
# import matplotlib.pyplot
# rest van pandas plotting geskipt
