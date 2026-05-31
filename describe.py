import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Rahul', 'Rishav', 'Aman', 'Kushu', 'Umash'],
    "Age": [10, 20, 30, 40, 50, 60, 70],
    "Salary": [100, 200, 300, 400, 500, 600, 700],
    "Performance Score": [85, 90, 95, 75, 54, 55, 34]
}

df = pd.DataFrame(data)

print("Sample DataFrame")
print(df)


# Sample DataFrame
#      Name  Age  Salary  Performance Score
# 0     Ram   10     100                 85
# 1   Shyam   20     200                 90
# 2   Rahul   30     300                 95
# 3  Rishav   40     400                 75
# 4    Aman   50     500                 54
# 5   Kushu   60     600                 55
# 6   Umash   70     700                 34