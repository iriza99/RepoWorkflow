import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
athletes_data = pd.read_csv("Forbes Richest Atheletes (Forbes Richest Athletes 1990-2020).csv")

# Group athletes by year and calculate mean earnings for each group
athletes_by_year = athletes_data.groupby('Year')
mean_earnings_by_year = athletes_by_year.mean(numeric_only=True)

# Plot the temporal evolution of the earnings
plt.plot(mean_earnings_by_year.index, mean_earnings_by_year['earnings ($ million)'])
plt.xlabel('Year')
plt.ylabel('Mean earnings ($ million)')
plt.title('Temporal Analysis of the Earnings of the Top 10 Athletes per Year')
plt.savefig('Top10EarningsPerYear.png')
plt.show()
