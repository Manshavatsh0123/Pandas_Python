import pandas as pd

# # Read the data from CSV into a dataframe
# df = pd.read_csv("/home/mansha-vatsh/Desktop/Pandas/sales_data_sample.csv")

#Read the data from Excel Into a dataset
# df = pd.read_excel("/home/mansha-vatsh/Desktop/Pandas/sales_data_sample.xlsx")

# Read the data from Excel Into a dataset
df = pd.read_json("sales_data_sample.json")

print(df)
