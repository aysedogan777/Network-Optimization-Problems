# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:31:17 2020

@author: adogan
"""

## importing libraries
import pandas as pd
import numpy as np

## Empty dictionary for graph
d = {}
#load data
#location if the data
import pathlib
location = pathlib.Path().absolute()
#name of the graph that you need to change in here
name = 'netscience.graph'
loc = str(location)+ '\\'+name
df = pd.read_csv(loc, skip_blank_lines = False)
#df =pd.read_csv(r'C:\Users\adogan\OneDrive - Oklahoma A and M System\Network Optimization\testcomp.graph',  skip_blank_lines = False)
if type(df.iloc[-1,0]) != str:
    df = df.drop(df.shape[0]-1,axis = 0)
#create clean dataframe
rows= df[df.columns[0]].str.split(" ", n = df.shape[0], expand = True)
rows = rows.replace('', 0) 
rows = rows.replace('None',0)
rows =rows.fillna(value=np.nan)
rows = rows.fillna(0)

ver_set = {}
visited = {}
#convert the dataframe to dictionary and make the vertices integer
rows = rows.astype(int)
for i in range(rows.shape[0]):
    for j in range(rows.shape[1]):
        #rows.iloc[i,j] = int(rows.iloc[i,j])
        #value = list(rows.iloc[i,:])
        d[int(i+1)] = list(rows.iloc[i,:])
        #ver_set[i+1] = False
        visited[i+1] = False

    #delete the 0 which is not a node in graph
    #check the efficiency by deleting and without deleting them
    while sum(x is 0 for x in d[i+1]) != 0:
#        print(i)
        if d[i+1][-1] == 0:
            del d[i+1][-1]
#all vertices in the graph            
comp = list(d.keys())    

#dfs function    
def dfs(V):
    #check the vertices if they are visited or not
    visited[V] = True
    #recod the dfs
    ver_set[i].append(V)
#    print(i)
    for neighbours in d[V]:
        if visited[neighbours] == False:
            dfs(neighbours)
    return ver_set

#Call dfs for the vertices 
i = 0
for j in comp:
    if visited[j] == False:
        i = i+1
        ver_set[i] = []
        dfs(j)
#        print(i, ver_set[i])
#        print('starting vertex',j)
with open('Component_List_netscience.txt', 'w') as filehandle:
    for j in range(1,len(ver_set)+1):
        #print(listitem)
        filehandle.write('Component {} : %s\n'.format(j) % ver_set[j])
        
