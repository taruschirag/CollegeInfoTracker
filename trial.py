import pandas as pd

print(pd.__version__)
df = pd.read_excel('./Lil Master.xlsx', 'US-Colleges')
print(df)