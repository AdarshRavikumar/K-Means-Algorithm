# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:29:08 2019

@author: STUDENT
"""
from kmeans import kmeans
#n=int(input())
#k=int(input())
#inp1=[]
#for i in range(n):
#    inp=input().split()
#    inp=[float(i) for i in inp]
#    inp1.append(inp)

import pandas as pd
dataset=pd.read_csv('Mall_Customers.csv')
dataset=dataset.iloc[:,[3,4]].values

inp1=[]
for i in range(len(dataset)):
    inp1.append(list(dataset[i]))

k=int(input("Enter number of clusters"))
obj=kmeans(inp1,k)
res,center=obj.controller(inp1,k)

print(center)
print("\n")
for i in range(0,len(res)):
    print("cluster ",i ,"has\n")
    print(res[i])
    print("\n")
klk=['red','blue','green','cyan','violet']
import matplotlib.pyplot as plt
for i in range(len(res)):
    k1=klk[i]
    for j in range(len(res[i])):
        plt.scatter(res[i][j][0],res[i][j][1],label=i,c=k1)

for i in range(len(center)):
    plt.scatter(center[i][0],center[i][1],label='centroid',c='yellow')     
