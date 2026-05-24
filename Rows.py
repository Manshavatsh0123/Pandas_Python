# head() - head(n) first n row of dataframe , head() - give 5 rows
# tail() - tail(n) last row of the dataframe , tail() 

import pandas as pd

df = pd.read_json("sales_data_sample.json")

# print("Display first 5 rows:")
# print(df.head(5))

# print("\nDisplay last 5 rows:")
# print(df.tail(5))

# Display first 5 rows:
#    Order_ID       Date     Product Region  Quantity  Unit_Price  Total_Sales
# 0      1001 2026-01-02      Laptop  North         5       16549        82745
# 1      1002 2026-01-03       Mouse  South         2       44848        89696
# 2      1003 2026-01-04  Headphones  North        10       28151       281510
# 3      1004 2026-01-05      Laptop  North         2       14828        29656
# 4      1005 2026-01-06       Mouse  North         9       13531       121779

# Display last 5 rows:
#     Order_ID       Date     Product Region  Quantity  Unit_Price  Total_Sales
# 25      1026 2026-01-27  Headphones   East        10       28577       285770
# 26      1027 2026-01-28  Headphones   West         6       14873        89238
# 27      1028 2026-01-29       Mouse   West         2        3587         7174
# 28      1029 2026-01-30      Laptop  South         3       45096       135288
# 29      1030 2026-01-31     Monitor  North         7       25509       178563


print("Display first rows:")
print(df.head())

print("\nDisplay last rows:")
print(df.tail())

# Display first rows:
#    Order_ID       Date     Product Region  Quantity  Unit_Price  Total_Sales
# 0      1001 2026-01-02      Laptop  North         5       16549        82745
# 1      1002 2026-01-03       Mouse  South         2       44848        89696
# 2      1003 2026-01-04  Headphones  North        10       28151       281510
# 3      1004 2026-01-05      Laptop  North         2       14828        29656
# 4      1005 2026-01-06       Mouse  North         9       13531       121779

# Display last rows:
#     Order_ID       Date     Product Region  Quantity  Unit_Price  Total_Sales
# 25      1026 2026-01-27  Headphones   East        10       28577       285770
# 26      1027 2026-01-28  Headphones   West         6       14873        89238
# 27      1028 2026-01-29       Mouse   West         2        3587         7174
# 28      1029 2026-01-30      Laptop  South         3       45096       135288
# 29      1030 2026-01-31     Monitor  North         7       25509       178563