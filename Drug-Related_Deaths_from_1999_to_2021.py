# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
# read csv files
file_path = r'Drug_Poisoning_deaths_and_rates.csv'
df = pd.read_csv(file_path, skiprows=[0,1382], on_bad_lines='skip')

# %%
# Assigning column names to the DataFrame
df.columns = ['Year', 'Gender', 'Intent', '', 'DrugType', '<1year', '1-4year', '5-14year', '15-24year', '25-34year', '35-44year', '45-54year', '55-64year', '65-74year', '75-84year', '85+year', 'NotStated', 'AllAges']
print(df.head())

# %%
# Filtering the data for the two conditions
all_drugs = df[(df['DrugType'] == 'All drugs') & (df['Intent'] == 'All (preventable, intentional, undetermined)') & (df['Gender'] == 'Both sexes')]['AllAges'].tolist()
opioid_fentanyl = df[(df['DrugType'] == 'Opioid subgroup – including fentanyl') & (df['Intent'] == 'All (preventable, intentional, undetermined)') & (df['Gender'] == 'Both sexes')]['AllAges'].tolist()
years = df[(df['DrugType'] == 'All drugs') & (df['Intent'] == 'All (preventable, intentional, undetermined)') & (df['Gender'] == 'Both sexes')]['Year'].tolist()


# %%
print(len(all_drugs))
print(len(opioid_fentanyl))
print(len(years))

# %%
print(all_drugs)
print(opioid_fentanyl)
print(years)

# %%
plt.figure(figsize=(15, 8))

# Plotting the area for 'All drugs'
plt.fill_between(years, all_drugs, color="skyblue", alpha=0.4, label='All Drugs')

# Plotting the area for 'Opioids including fentanyl' on top
plt.fill_between(years, opioid_fentanyl, color="sandybrown", alpha=0.5, label='Opioids Including Fentanyl')

# Customizing the plot
plt.title('Escalating Impact of Opioids: Drug-Related Deaths from 1999 to 2021')
plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.xticks(years)
plt.legend()

# Show the plot
plt.show()


