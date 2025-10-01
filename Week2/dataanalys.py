import pandas as pd
import numpy as np
import pygwalker as pg

dt = pd.read_csv('/home/nexy/Code/AIVIETNAM/Documentss/data.csv')
print(dt.head(5))
dt = dt.drop(['customer_id'] , axis = 1)
print(dt.head(5))