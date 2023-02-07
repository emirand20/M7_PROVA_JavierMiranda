import pandas as pd

df = pd.read_csv('Llistat.csv')
deleteNan = df.dropna()
print(deleteNan)