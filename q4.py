# Explain how you would relate the price series (All items) with the Gasoline (Gasoline) price series.:

# To analyse the relationship between CPI All items and CPI Gasoline price series in a simples way, we could do the following:
# 1. correlation analysis (linear and year-over-year percentage variation):
#    - Linear correlation help to understand the direct relationship between the two datasets over time.
#    - Year-over-year percentage variation correlation allows to identify how the growth rate of all items prices is related to the growth rate of gasoline prices.
# 2. plot to do a visual analysis:
#    - Plotting the data may provide a visual view of the relationship between the two time series.
# 3. compare statistics like standard deviation:
#    - Comparing the standard deviation of the two datasets can give an idea of how volatile both prices are over time.

import pandas as pd
import plotly.express as px

df = pd.read_csv('cpi_data.csv')

# Correlation analysis between all items and gasoline
all_time = df['CUSR0000SA0']
gasoline = df['CUSR0000SETB01']
linear_correlation = all_time.corr(gasoline)
print(f'Pearson correlation coefficient: {linear_correlation}')

# Year-over-year percentage variation correlation analysis
all_time_pct_change = all_time.pct_change(12).dropna()
gasoline_pct_change = gasoline.pct_change(12).dropna()
pct_change_correlation = all_time_pct_change.corr(gasoline_pct_change)
print(f'Pearson correlation coefficient of year-over-year percentage variation: {pct_change_correlation}')

# Standard deviation comparison
all_time_std = all_time.std()
gasoline_std = gasoline.std()
print(f'Standard deviation of all items: {all_time_std}')
print(f'Standard deviation of gasoline: {gasoline_std}')

# Normalizing the data to plot
df['norm_all_time'] = all_time / all_time.iloc[0]
df['norm_gasoline'] = gasoline / gasoline.iloc[0]

# Plotting the data for visual analysis
fig = px.line(df, x='date', y=['norm_all_time', 'norm_gasoline'], title='Normalized CPI Data')
fig.show()