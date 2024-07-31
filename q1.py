import requests
import pandas as pd

# https://www.bls.gov/help/hlpforma.htm#CU
# https://download.bls.gov/pub/time.series/cu/cu.item
# CPI All items, seasonally adjusted = CUSR0000SA0
# CPI All items, less food and energy, seasonally adjusted = CUSR0000SA0L1E
# CPI Gasoline (all types), seasonally adjusted = CUSR0000SETB01

headers = {'Content-type': 'application/json'}
data = {
    #"registrationkey": "...",
    "seriesid": ['CUSR0000SA0', 'CUSR0000SA0L1E', 'CUSR0000SETB01'],
    "startyear":"2019",
    "endyear":"2024"
}

response = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', json=data, headers=headers)
json_data = response.json()

# Iterating through the series (just like the API's tutorial/example) and building the final DataFrame
final_df = pd.DataFrame()
for series in json_data['Results']['series']:
    series_id = series['seriesID']

    series_data = [] # Individual series data
    for item in series['data']:
        date = f"{item['period'][1:]}/1/{item['year']}"
        series_data.append([date, item['value']])

    series_df = pd.DataFrame(series_data, columns=['date', series_id])
    series_df['date'] = pd.to_datetime(series_df['date'], format='%m/%d/%Y')
    
    # Merging the series data into the final DataFrame
    if final_df.empty:
        final_df = series_df
    else:
        final_df = pd.merge(final_df, series_df, on='date', how='outer')

final_df.to_csv('cpi_data.csv', index=False)
