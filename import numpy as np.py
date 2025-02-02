import numpy as np
import pandas as pd
ser = pd.Series()
print("Pandas Series : ",ser)
data = np.array(['c','h','r','i','s','t'])
ser = pd.Series(data)
print("Pandas Series:\n", ser)
df = pd.DataFrame()
print(df)
lst = ['Christ','Deemed','To','Be','Univeristy','Bangalore','Karnataka']
df = pd.DataFrame(lst)
print(df)