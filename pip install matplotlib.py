
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
djia_data = pd.read_csv("HistoricalPrices.csv")
djia_data.head()
plt.scatter(djia_data['Date'],djia_data['Close'])
#plt.bar(djia_data['Date'],djia_data['Open'])
plt.grid()
plt.show()
#plt.show()
plt.bar(djia_data['Date'],djia_data['Open'])
plt.grid()
plt.show()