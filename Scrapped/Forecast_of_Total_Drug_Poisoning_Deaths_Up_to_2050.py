# Re-importing necessary libraries after the code execution state reset
import pandas as pd

# The user has re-uploaded the same file. Let's attempt to load it again for analysis, addressing the previous issue.
# file_path_new = '/mnt/data/Drug_Poisoning_deaths_and_rates.csv'
# data_reloaded = pd.read_csv(file_path_new, skiprows=1)  # Attempting to skip the misleading header again
file_path = r'Drug_Poisoning_deaths_and_rates.csv'
data_reloaded = pd.read_csv(file_path, skiprows=[0,1382], on_bad_lines='skip')


# Displaying the first few rows to confirm it's loaded correctly
data_reloaded.head()

# Importing necessary libraries for analysis and plotting
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Aggregating total deaths by year
data_reloaded['Year'] = pd.to_numeric(data_reloaded['Year'], errors='coerce')  # Ensure 'Year' is numeric
total_deaths_by_year = data_reloaded.groupby('Year')['All ages'].sum()

# Plotting the trend of total drug poisoning deaths over time
plt.figure(figsize=(12, 6))
total_deaths_by_year.plot(kind='line', marker='o', color='teal')
plt.title('Total Drug Poisoning Deaths by Year')
plt.xlabel('Year')
plt.ylabel('Total Deaths')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Preparing data for linear regression model to forecast future trend
X = total_deaths_by_year.index.values.reshape(-1, 1)  # Years
y = total_deaths_by_year.values  # Total Deaths

# Fitting the linear regression model
model = LinearRegression()
model.fit(X, y)

# Generating future years up to 2050
future_years = np.arange(2022, 2051).reshape(-1, 1)

# Predicting future deaths
future_predictions = model.predict(future_years)

# Plotting the forecast
plt.figure(figsize=(12, 6))
plt.plot(X, y, label='Actual Total Deaths', marker='o', color='teal')
plt.plot(future_years, future_predictions, label='Forecasted Total Deaths', linestyle='--', color='orange')
plt.title('Forecast of Total Drug Poisoning Deaths Up to 2050')
plt.xlabel('Year')
plt.ylabel('Total Deaths')
plt.legend()
plt.grid(True)
plt.xticks(np.arange(1999, 2051, 5), rotation=45)
plt.tight_layout()
plt.show()
