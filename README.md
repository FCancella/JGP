## Q1:
**Output:**

[`Fetched csv`](cpi_data.csv)

## Q2:
**Output:**
![Q2 Output](q2_output.png)

(Frequency was kept monthly)

## Q3:
How you would automate the process of extracting the data?

To automate the process of extracting the data we could have two simple scripts:

1. Create a script/routine to fetch the data from the API and save it to a CSV file every hour/day/week/month (just like `q1.py`).
   - The data to be fetched (determined series) could be defined in a configuration file.
   - Note: The API fetching process is already simple and automatic, so we can just schedule the script to run on a regular basis.

2. Create another script/routine to process the saved CSV and upload the data to a database.
   - This code could also provide some extra features like:
     - Saving/calculating the year-over-year percentage variation.
     - Plotting the data and saving the plot as an image.
     - Writing a report with the data and the plot.

## Q4:
Explain how you would relate the price series (All items) with the Gasoline (Gasoline) price series:

To analyze the relationship between CPI All items and CPI Gasoline price series in a simple way, we could do the following:

1. **Correlation analysis (linear and year-over-year percentage variation):**
   - Linear correlation helps to understand the direct relationship between the two datasets over time.
   - Year-over-year percentage variation correlation allows identifying how the growth rate of all items prices is related to the growth rate of gasoline prices.

2. **Plot for visual analysis:**
   - Plotting the data may provide a visual view of the relationship between the two time series.

3. **Compare statistics like standard deviation:**
   - Comparing the standard deviation of the two datasets can give an idea of how volatile both prices are over time.

**Output:**

- Pearson correlation coefficient: 0.8044789669584937
- Pearson correlation coefficient of year-over-year percentage variation: 0.7572940527036165
- Standard deviation of all items: 21.400672490735214
- Standard deviation of gasoline: 57.06203789192502
  
![Q4 Output](q4_output.png)

## Bonus:

\> uvicorn bonus:app

![Bonus Output](bonus_output_1.png)

![Bonus Output](bonus_output_3.png)

![Bonus Output](bonus_output_2.png)
