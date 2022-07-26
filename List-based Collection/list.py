#numpy array is faster than list
#both store a collection of ordered, alterable data objects

l = ['a','b','c','d']
print(l[1:3]) #list slice l[initial:end:index jump], where end will not be printed

#The len() in python can be carried out in O(1) 

##################################
#Comparison of numpy array vs list
##################################
import numpy as np
from time import time

arr = np.random.rand(1000000)
l = list(arr)

start_arr = time()
np_mean = np.mean(arr)
print("Mean of numpy array = {}".format(np_mean))
end_arr = time()
print("Time taken for numpy array = {}".format(end_arr - start_arr))

start_list = time()
np_mean = np.mean(l)
print("Mean of list = {}".format(np_mean))
end_list = time()
print("Time take for list = {}".format(end_list - start_list))

#However, numpy array is not always faster than list.
#List performs faster in terms of appending
