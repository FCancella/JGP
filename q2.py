import plotly.express as px
import pandas as pd

df = pd.read_csv('cpi_data.csv')

# CPI All items, less food and energy, seasonally adjusted = CUSR0000SA0L1E
df = df[['date', 'CUSR0000SA0L1E']]

# "year-over-year percentage variation"
df['CUSR0000SA0L1E'] = df['CUSR0000SA0L1E'].pct_change(12) * 100

# Plotting the data
fig = px.line(df, x='date', y='CUSR0000SA0L1E', title='Year-over-Year Percentage Variation of CPI All items, less food and energy')
fig.show()
