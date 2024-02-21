import pandas as pd
import matplotlib.pyplot as plt
#check

# read csv files
file_path = r'Drug_Poisoning_deaths_and_rates.csv'
data = pd.read_csv(file_path, skiprows=[0,1382], on_bad_lines='skip')

# Assigning column names to the DataFrame
data.columns = ['Year', 'Gender', 'Intent', '', 'DrugType', '<1year', '1-4year', '5-14year', '15-24year', '25-34year', '35-44year', '45-54year', '55-64year', '65-74year', '75-84year', '85+year', 'NotStated', 'AllAges']


print(data.head())
# print(data['Year'])

population = []
checked_year = []
years = []


# for i, y in enumerate(data['Year']): # i is index number y is year
#     # print(i)
#     # print(y)
#     checked_year[0] = y[0]
#     population[0] = data['AllAges'][0]
#     if checked_year[] == y[]

#     else checked_year[] == y[]
for idx, row in data.iterrows():
    year = row['Year']
    population_val = row['AllAges']
    
    # check year
    if checked_year is None or checked_year != year:
        checked_year = year
        # save the year and population
        population.append(population_val)
        years.append(year)

    # if same no change
    else:
        pass

# plot
plt.figure(figsize=(10, 6))
plt.bar(years, population, color='skyblue')
plt.title('Drug Overdose Death vs Year')
plt.xlabel('Year')
plt.ylabel('Death Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
