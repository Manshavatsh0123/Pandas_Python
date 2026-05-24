import pandas as pd

data = {
    "Name": ['Ram', 'Shyan', 'Krish'],
    "Age": [10, 20, 30],
    "City": ['Nagpur', 'Mumbai', 'Delhi']
}

df = pd.DataFrame(data)

print("Display info of Dataset")

print(df.info())


# #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   Name    3 non-null      str  
#  1   Age     3 non-null      int64
#  2   City    3 non-null      str  
# dtypes: int64(1), str(2)
# memory usage: 204.0 bytes
# None