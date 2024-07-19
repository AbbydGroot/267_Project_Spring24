#!/usr/bin/env python
# coding: utf-8

# In[21]:


import math
import numpy as np
import matplotlib.pyplot as plt
import numpy as np 

## PHYS 267, Spring 2024, Final Project
## Abigail deGroot 
## 21012489



## measured data, copied from excel, average and standard deviation generated in excel 
## index 0 - 4 are meaured times, index 5 is the average, index 6 is standard deviation
controlData = [14.95, 14.83, 14.35, 15.03, 15.37, 14.91, 0.37]	
UpbeatData = [11.64, 12.14, 13.37, 12.54, 11.43, 12.22, 0.77]	
SadData = [21.18, 23.24, 21.39, 22.70, 21.38, 21.98, 0.93]	
MetalData = [11.27, 8.53, 13.45, 11.38, 9.76, 10.88, 1.86]	
CalmData =[18.80, 16.04, 16.34, 17.61, 15.03, 16.76, 1.46]

Data = [controlData, UpbeatData, SadData, MetalData, CalmData] #array containing all data
Genres = ["Control", "Upbeat", "Sad", "Metal", "Classical"]

def averages(): 
    lst = []
    for i in range(len(Data)): 
        lst.append(Data[i][5])
    return lst
avg = averages()

def standardDev(): 
    lst = []
    for i in range(len(Data)): 
        lst.append(Data[i][6])
    return lst
stddev = standardDev()

colour = ["lightsteelblue", "gold", "steelblue", "mediumpurple", "lightpink"]

plt.bar(Genres, avg, yerr = stddev, color = colour, ecolor = "sienna", capsize = 15)
plt.title("\nHow Long Fifteen Seconds Feels \nWhen Listening to Different Music\n")
plt.xlabel("\nGenre")
plt.ylabel("Time (s)")
plt.show()


# In[ ]:




