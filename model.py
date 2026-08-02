import pandas as pd

# had issues seeing the tables that pandas was formatting
# used these lines to improve visibility
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

#reads the CSV back into a dataframe (a "DF")
df = pd.read_csv("tiktok_data.csv")

print(df.head())

# prints the type of each column (e.g. likes, views, etc)
print(df.dtypes)