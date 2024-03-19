import pandas as pd
import os

mydt = pd.DataFrame({
 'ID': [11, 12, 13, 14, 15],
 'first_name': ['David', 'Jamie', 'Steve', 'Stevart', 'John'],
 'company': ['Aon', 'TCS', 'Google', 'RBS', '.'],
 'salary': [74, 76, 96, 71, 78]})

print(mydt)
# Check working directory
os.getcwd()

# change the working directory ,Save data as CSV
os.chdir("/file/4")
mydt.to_csv('workingfile.csv', index=False)
mydata = pd.read_csv("workingfile.csv")

# Read CSV file with header row
print(pd.read_csv("workingfile.csv", header=0))

# Specify missing values
mydata00 = pd.read_csv("workingfile.csv", na_values=['.'])

print(mydata00)

# skip_footer not an argument
# mydata04 = pd.read_csv("http://winterolympicsmedals.com/medals.csv", skipfooter=2,)
# print(mydata04)

# Read CSV File from External URL
# mydata02 =pd.read_csv("http://winterolympicsmedals.com/medals.csv")


# Read only first 3 rows
mydata05 = pd.read_csv("workingfile.csv", nrows=3)
print(mydata05)

# Read only specific columns
mydata07 = pd.read_csv("workingfile.csv", usecols=[1, 3])
print(mydata07)

# Read Excel File
# myExeldata = pd.read_excel('DM/Cities_Brazil_IBGE.xlsx', skiprows=2)
# print(myExeldata)

# Read Text File
myTextdata = pd.read_table("/DM/dataset/dataset1.txt")
print(myTextdata)

# Read CSV file
myirisdata = pd.read_csv("/DM/iris.csv")

print(myirisdata.loc[3])                      # access all data of the forth row

print(myirisdata.loc[1:4, 'petal_width'])     # specific column for certain rows

# Select or Drop Variable:to keep one or more variable
print(myirisdata.loc[:, ['petal_width', 'petal_width']])
print(myirisdata.loc[:, 'petal_width'])

print(myirisdata.iloc[:2])               # select variable by column position

# Drop specified labels from rows or columns
print(myirisdata.drop(['petal_width', 'petal_width'], axis=1))   # axis=1 for cols
print(myirisdata.drop([1, 2, 3, 4, 5, 6], axis=0))               # axis=0 for rows

print(myirisdata.describe())                    # To summarize Data

print(myirisdata.describe(include=['O']))       # To summaries all the character variables

# To select only a particular variable
print(myirisdata['petal_length'].describe())
print(myirisdata['petal_length'].mean())
print(myirisdata['petal_length'].min())

# Filter Data
d1 = myirisdata.query('(species=="Setosa")')
print(d1)
print(myirisdata.query('(species=="Setosa")&(petal_length>= 1.5)'))

# Sort Data
print(d1.sort_values(by='petal_length', ascending=False))
print(d1.sort_values(by='petal_length', ascending=True))

print(myirisdata["species"].astype('category'))   # Define Categorical Variable

print(myirisdata['petal_length'].hist())          # Generate Histogram

print(myirisdata.boxplot(column='petal_length'))  # BoxPlot
