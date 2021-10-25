import numpy as np
import pandas as pdpy
import matplotlib.pyplot as plt
from pandas import Series,DataFrame

bream_length= [25.4, 26.3, 26.5, 29, 29, 29.7, 29.7, 30, 30, 30.7, 
                          31, 31, 31.5, 32, 32, 32, 33, 33, 33.5, 33.5, 34, 34, 
                          34.5, 35, 35, 35, 35, 36, 36, 37, 38.5, 38.5, 39.5, 41, 41]

bream_weight= [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]      


smelt_length=  [9.8, 10.5, 10.6, 11, 11.2, 11.3 ,11.8
                            ,11.8, 12, 12.2, 12.4, 13, 14.3 ,15]

smelt_weight= [6.7, 7.5, 7, 9.7, 9.8, 8.7, 10, 9.9, 9.8, 
                            12.2,13.4,12.2,19.7, 19.9]                                


bream_length = np.array(bream_length)
bream_weight = np.array(bream_weight)

smelt_length = np.array(smelt_length)
smelt_weight = np.array(smelt_weight)

bream_data = np.column_stack((bream_length, bream_weight))
smelt_data = np.column_stack((smelt_length, smelt_weight))

plt.scatter(bream_data[:,0], bream_data[:,1])
plt.scatter(smelt_data[:,0], smelt_data[:,1])
plt.xlabel("length")
plt.ylabel("weight")
plt.show()

fish_length = bream_length + smelt_length
fish_weight = bream_weight + smelt_weight                
fish_target = np.concatenate((np.ones(35), np.zeros(14)))

fish_data = np.column_stack((fish_length, fish_weight))
print(fish_data)
print(fish_target)



index = np.arange(49) 
np.random.shuffle(index)
print(index)


train_input = fish_data[index[:35]] 
train_target = fish_target[index[:35]] 



test_input = fish_data[index[35:]] 
test_target = fish_target[index[35:]] 


plt.scatter(train_input[:,0], train_input[:,1]) 
plt.scatter(test_input[:,0], test_input[:,1]) 

plt.xlabel("length")
plt.ylabel("weight")
plt.show()