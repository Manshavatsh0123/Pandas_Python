import pandas as pd

data = {
    "Name": ['Ram', 'Shyan', 'Krish'],
    "Age": [10, 20, 30],
    "City": ['Nagpur', 'Mumbai', 'Delhi']
}

df = pd.DataFrame(data)

print(df)

# Save CSV file
# df.to_csv("output.csv", index=False)

# Save Excel file
# df.to_excel("output.xlsx", index=False)

# Save JSON File
df.to_json("Output.json",index=False)