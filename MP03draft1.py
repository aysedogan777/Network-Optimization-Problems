# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 23:32:17 2020

@author: adoga
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 20:39:55 2020

@author: adogan
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 20:36:53 2020

@author: adogan
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 11:23:39 2020

@author: adogan
"""

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
#name = 'matrix_100_1_3_1.graph'
#loc = str(location)+ '\\'+name
#df = pd.read_csv(loc, skip_blank_lines = False)
df =pd.read_csv(r'C:\Users\adogan\OneDrive - Oklahoma A and M System\Classified\Codes\matrix_100_1_3_1.gr', error_bad_lines=False)# skip_blank_lines = False)

if type(df.iloc[-1,0]) != str:
    df = df.drop(df.shape[0]-1,axis = 0)
#create clean dataframe
#df = df.iloc[2:,:]
c = 'c'
df_dropped = pd.DataFrame()
i = 2
df.columns = [0]
for i in range(df.shape[0]):
    line = str(df.iloc[i,:])#df.shape[0] -1 -
    
    if line[:6] == '0    a':
        new_line = line[:].index('\n')
        a_ind = line[:new_line].rindex('a')
        line = line[a_ind+2:new_line]
        df_line = pd.DataFrame(line, index =[1], columns =[0]) 
        df_dropped = df_dropped.append(df_line)
    elif line[:6] == '0    p':
        new_line = line[:].index('\n')
        p_ind = line[:new_line].rindex('p')
        line = line[p_ind+2:new_line]
        mn = line.split()
        n = int(mn[0])
        m = int(mn[1])

    
df_dropped.index = pd.RangeIndex(start=0, stop=len(df_dropped), step=1)
rows= df_dropped[df_dropped.columns[0]].str.split(" ", n = df_dropped.shape[0], expand = True)
#convert the dataframe to dictionary and make the vertices integer
rows = rows.astype(int)

#creating multidimensional dictionary    
graph = {}
#graph[rows.iloc[0,0]] = []
j = 0
for i in range(rows[0].shape[0]):
    arr = list()
    arr_dict = {}
    for j in range(rows[0].shape[0]):
        if rows.iloc[i,0]== rows.iloc[j, 0]:
            print(j,i)
            arr_dict[rows.iloc[j,1]] = rows.iloc[j,2]
    graph[rows.iloc[i,0]] = arr_dict #append(rows.iloc[j,1])

# For each node prepare the destination and predecessor 
def initial_dict(graph, source):
    d = {} # distance
    p = {} # predecessor
    for node in graph:
        d[node] = float('Inf') # All verteices are infinitely far
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    p[source] = 0 # For the source we know distance
    return d, p

d,p = initial_dict(graph, 1)

def relax(u, v, graph, d, p):
    # If the distance between the u and the v is lower than I have 
    if d[v] > d[u] + graph[u][v]:
        # Update distance
        d[v]  = d[u] + graph[u][v]
        p[v] = u
    elif d[u] == float('Inf'):
        d[u] = n *  rows[2].max()
        p[u] = -1        
        
def bellman_ford(graph, source):
    d, p = initial_dict(graph, source)
    for i in range(len(graph)-1): #Run this until is converges
        for u in graph: #the first u vertex in the graph
            for v in graph[u]: #each neighbour of u
                relax(u, v, graph, d, p) 
    return d, p
                          
        # print all distance
d, p = bellman_ford(graph, 1)#, graph_weight)

for i in range(1,n+1):
    if i not in list(d.keys()):
        d[i] = n *  rows[2].max()
        p[i] = -1
#del d[-1]
if list(d.keys()) ==  list(p.keys()):
    print(True)
#dataframe for output
output = pd.DataFrame()
output['Vertex'] = d.keys()
output['Distance'] = d.values()
output['Predecessor'] = p.values()

output = output.sort_values(by='Vertex',ascending=True)
output.to_csv('matrix_100_1_3_1.csv',index=False, index_label=None)
