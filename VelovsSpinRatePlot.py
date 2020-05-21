#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:24:25 2019

@author: EmilioMartinez
"""

import matplotlib.pyplot as plt 
import pandas as pd  


#Upoload the Excel File and use only the colums I want, which are pitch type, locations, velo, spin rate
file_loc = "/Users/EmilioMartinez/Desktop/BrockBurke_plot_project/brockburkedebutBrooksBaseball.xlsx"
df = pd.read_excel(file_loc,index_col = None , na_values=['NA'], usecols = "P,Y,AF,AG,AS")
#print(df.head(50))
#Rename the colums headers from 'Unnamed' for my own organization
df2 = df.rename(columns={'Unnamed: 0': 'Pitch Type',
    'Unnamed: 1': 'SpinRate',
    'Unnamed: 2': 'HorizLoc',
    'Unnamed: 3': 'VertLoc',
    'Unnamed: 4': 'Velo'})

#Delete the first row, because I made the headers and makes the data eaier to work with
df2 = df2[1:]

#Sort the data by pitch type (aplhabetical order) with highest velocity first
df2 = df2.sort_values(by=['Pitch Type', 'Velo',],ascending=[True, False])

#Set index as the pitch type so I can get data easier 
df2.set_index("Pitch Type", inplace=True)


print('\n---------------------------------------------------\n')
print(df2.head(47))
print('\n--------------------------------------------------------\n')

#Selecting just pitch types and the horizontal and vertical locations

CU = df2.loc[['CU'], ['Velo', 'SpinRate']]
CH = df2.loc[['CH'], ['Velo', 'SpinRate']]
FF = df2.loc[['FF'], ['Velo', 'SpinRate']]
FT = df2.loc[['FT'], ['Velo', 'SpinRate']]
SL = df2.loc[['SL'], ['Velo', 'SpinRate']]


fig = plt.figure()
ax1 = fig.add_subplot(111) 


ax1.scatter(FT.SpinRate,FT.Velo,c = 'b',label = '2sFB')
ax1.scatter(FF.SpinRate,FF.Velo,c = 'r',label = '4seamFB')
ax1.scatter(CH.SpinRate,CH.Velo,c = 'c',label = 'Changeup')
ax1.scatter(CU.SpinRate,CU.Velo,c = 'g',label = 'Curveball')
ax1.scatter(SL.SpinRate,SL.Velo,c = 'm',label = 'Slider')


plt.xlabel('Spin Axis (degrees)')
plt.ylabel('Velocity (mph)')


plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left')
plt.title('Brock Burke MLB Debut\n--------\nSpin X Velocity',y=1,fontweight="bold")


plt.show()

print('\n--------------------------------------------------------\n')
