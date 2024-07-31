# How you would automate the process of extracting the data?

# To automate the process of extracting the data we could have 2 simple scripts:

# 1: Create a script/routine to fetch the data from the API and save it to a CSV file every hour/day/week/month (just like q1.py).
# The data to be fetched (determined series) can be defined in a configuration file.
# Note: The API fetching process is already simple and automatic, so we can just schedule the script to run on a regular basis.

# 2: Create another script/routine to process the saved CSV and upload the data to a database.
# This code could also provide some extra features like:
# - saving/calculating the year-over-year percentage variation,
# - plotting the data and saving the plot as an image,
# - writing a report with the data and the plot.