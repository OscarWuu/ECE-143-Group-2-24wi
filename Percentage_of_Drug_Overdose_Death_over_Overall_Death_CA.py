import pandas as pd
import matplotlib.pyplot as plt


# read csv files
file_path = r'D:\College_life\ECE 143\Number_of_Deaths_n_Number_of_Drug_Overdose_Deaths.xlsx'
data = pd.read_excel(file_path)


# Assigning column names to the DataFrame
# Number1 refers to Number of Drug Overdose Deaths, Number2 refers to Number of Overall Deaths
data.columns = ['State', 'Year', 'Month', 'Description1', 'Number1', 'Description2', 'Number2']


print(data.head())

#initialization
use1 = [0]*9
use2 = [0]*9
yearStart = 2015
y = [0]*9
year = []

#Store data into lists
for idx, row in data.iterrows():
    Number1 = row['Number1']  #Number of Drug Overdose Deaths
    Number2 = row['Number2']  #Number of Overall Deaths
    Number3 = row['Year']     #Year
    #print(Number3-yearStart)
    use1[Number3 - yearStart] += Number1
    use2[Number3 - yearStart] += Number2
    year.append(Number3)

#Calculate the percentage
for i in range(len(use1)):
    y[i] = use1[i]/use2[i]

#Change data Number3 which is years into year and remove duplicates
unique_years = sorted(set(year))


# plot
plt.figure(figsize=(10, 6))
plt.bar(unique_years, y, color='red')
plt.title('Percentage of Drug Overdose Death over Overall Death vs Year in CA')
plt.xlabel('Year')
plt.ylabel('Percentage of Drug Overdose Death over Overall Death in CA')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
