import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## READ DATA
df = pd.read_csv("../data/USDJPY_1M_3Y.csv")
print(df.head())

## CREATE VWAP
df['VxC'] = df['Volume'] * df['Close']
vwap_steps = 20
vwaps = [x for x in range(5,100,15)]

for vwap_steps in vwaps:
    print('Creating vwap{}'.format(vwap_steps))
    df['vwap{}'.format(vwap_steps)] = 0
    for i in range(vwap_steps, df.shape[0] + 1):
        df.loc[i - 1,'vwap{}'.format(vwap_steps)] = df.loc[i-vwap_steps:i,'VxC'].sum() / df.loc[i-vwap_steps:i,'Volume'].sum()
        if(i % 100000 == 0):
            print(i)

df = df[vwaps[-1] - 1:]
df.drop('VxC', axis = 1)
df.reset_index(drop=True, inplace=True)
print(df.head())
print(df.tail())

## SAVE MODEL
print('Saving model')
file_name = '../data/USDJPY_1M_vwap.csv'
df.to_csv(file_name, index = False)