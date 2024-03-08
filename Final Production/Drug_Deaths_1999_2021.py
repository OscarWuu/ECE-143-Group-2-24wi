import pandas as pd
import matplotlib.pyplot as plt

# read csv files
file_path = r'Drug_Poisoning_deaths_and_rates.csv'
df = pd.read_csv(file_path, 
                 skiprows=[0,1382], 
                 on_bad_lines='skip')

# Assigning column names to the DataFrame
df.columns = ['Year', 
              'Gender', 
              'Intent', 
              '', 
              'DrugType', 
              '<1year', 
              '1-4year', 
              '5-14year', 
              '15-24year', 
              '25-34year', 
              '35-44year', 
              '45-54year', 
              '55-64year',
              '65-74year', 
              '75-84year',
              '85+year', 
              'NotStated', 
              'AllAges']

print(df.head())

# Grouping Total deaths by Drug Type and Year
cond_extra = ((df['Intent'] == 'All (preventable, intentional, undetermined)')
              & (df['Gender'] == 'Both sexes'))
grp = df[cond_extra].groupby(['DrugType','Year'])['AllAges'].sum()
drugs = list(set(grp.index.get_level_values(0)))
years = list(set(grp.index.get_level_values(1)))



print('================ Table ================\n',grp)
print('\n================ Drugs ================\n',drugs)
print('================ Years ================\n',years)
assert grp['All drugs'][2021] == 106699




fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot()

ax.set_title('Escalating Impact of Opioids: Drug-Related Deaths from 1999 to 2021',
             size=22,
             pad=25)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(visible=True,
        which='major',
        axis='both',
        alpha=.4)

# Formatting X-Axis
ax.set_xlabel('Year',
              labelpad=10.0,
              size=24)
ax.set_xticks(list(range(1999,2022,2))+[2021])
ax.set_xticklabels(years[::2]+[2021], 
                   size=15,
                   rotation=45)
ax.set_xlim(left=min(years),
            right=max(years))

# Formatting Y-Axis
ax.set_ylabel('Number of Deaths',
           labelpad=20,
           size=24)
y_labels = [10000*scal 
               for scal in range(0,11,2)]+[max(grp['All drugs'])]
ax.set_yticks(y_labels)
ax.set_yticklabels(labels=y_labels,
                   size=14)
ax.set_ylim(bottom=0,
            top=grp['All drugs'][2021])

# Plotting lines for each drug
for drug in drugs:
   if drug == 'Any Opioid':
      continue
   elif False:
      ax.fill_between(years,
                   grp[drug],
                   alpha=.2 if not drug == 'All drugs' else .5,
                   label=drug)
   else:
      fmt = ('c-' if drug == 'All drugs' 
                     or drug == 'Opioid subgroup – including fentanyl'
                  else 'g-')
      ax.plot(years,grp[drug],
              fmt,
              label=drug)

ax.legend(loc='upper left')
plt.show()




