from collections import Counter
import re
import glob
import sys
import numpy as np

cutoff = 20

all_barrels = []
with open("BarrelChars85.txt", "r") as barrel_list:
    for line in barrel_list:
        if "Barrel" not in line:
            line = line.split("\t")
            all_barrels.append(line[0])

graph = {} #relationship list for each node
with open("FiltData_E20_v6_2018_Renumb.txt", "r") as inData:
    for line in inData:
        if "dom1" not in line:
            line = line.strip().split("\t")
            dom1 = line[0]
            dom2 = line[1]
            e_value = float(line[2])        
        
            if e_value <= cutoff:
                if dom1 in graph.keys():
                    graph[dom1].append(dom2)
                else:
                    graph[dom1] = [dom2]
                    
                if dom2 in graph.keys():
                    graph[dom2].append(dom1)
                else:
                    graph[dom2] = [dom1]

multiple_edges = [] #pairs of PDBs with multiple connections between them
stubs = []
for key in graph.keys():
    if len(graph[key]) == 1: 
        #print(key, graph[key])
        pop_from = graph[key][0]
        stubs.append(key)
        #print(graph[pop_from])
        graph[pop_from].remove(key)
        #print(graph[pop_from])
    else:
        #print(key, graph[key])
        edges = Counter(graph[key])
        for value in edges:
            if edges[value] >= 2:
                #find those pairs with more than one connection between them
                if [value, key] in multiple_edges: continue #print("In list already")
                else: multiple_edges.append([key, value])

print(multiple_edges)                
for key in stubs:
    del graph[key]
#graph now only consists of pdbs with multiple connections to the same pdb

multi_edge_lines = []
with open("FiltData_E20_v6_2018_Renumb.txt", "r") as inData, open("NoMultiEdgesE<20_v6.txt", "w+") as all_edges, open("MultiEdgesE<20_v6.txt", "w+") as multi_edges:
    for line in inData:
        if "dom1" not in line:
            line = line.strip().split("\t")
            dom1 = line[0]
            dom2 = line[1]
            e_value = float(line[2])      
            if e_value <= cutoff:                
                if ([dom1, dom2] in multiple_edges or [dom2, dom1] in multiple_edges):
                    multi_edge_lines.append(line)
                else:
                    all_edges.write("\t".join(line) + "1\n")
        else:
            all_edges.write(line)
    
    #remove the obvious near duplicates
    for value in multiple_edges: #for each pair of PDBs with multiconnections:
        print(value)
        edges = [] #edges relating to that pair
        for line in multi_edge_lines:
            if (value[0] in line and value[1] in line):
                edges.append(line)
        
        if len(edges) == 1: 
            print("Something went wrong ", line)
            all_edges.write("\t".join(line) + "\n")
        else:
            kept_edges = []    
            while len(edges) >0:
                first_row = edges[0]
                e_value = float(first_row[2])
                pop_list = []
                print_row = True
                #print(len(edges), edges)
                for x in range(1, len(edges)):
                    if edges[x][6:10] == first_row[6:10]:
                        if float(edges[x][2]) <= e_value: 
                            del edges[0]
                            print_row = False
                            break
                        else:
                            pop_list.append(x)
                        
                    #check if nearly identical segments
                    elif (abs(int(edges[x][7]) - int(first_row[7])) < 3 and abs(int(edges[x][9]) - int(first_row[9])) < 3):
                        #print("ends the same", abs(int(edges[x][8]) - int(first_row[8])), abs(int(edges[x][10]) - int(first_row[10])))
                        if abs( abs(int(edges[x][6]) - int(first_row[6])) + abs(int(edges[x][8]) - int(first_row[8])) ) < 10:
                            #print("start ~same", abs(int(edges[x][7]) - int(first_row[7])), abs(int(edges[x][9]) - int(first_row[9])))
                            if float(edges[x][2]) <= e_value: 
                                del edges[0]
                                print_row = False
                                break
                            else:
                                pop_list.append(x)
                
                #if value[1] == "1pho_A" and value[0] == "2wjr_A": print(pop_list, print_row)
                for y in reversed(pop_list): del edges[y]
                
                if print_row == True: 
                    #all_edges.write("\t".join(first_row) + "\n")
                    kept_edges.append(first_row)
                    del edges[0]
  
  
            keep_row = kept_edges[0]
            for x in range(1,len(kept_edges)):
                if float(kept_edges[x][2]) < float(keep_row[2]):
                    keep_row = kept_edges[x]
    
            for value in kept_edges:
                if value == keep_row:
                    multi_edges.write("\t".join(value) + " 1\n")
                else:
                    multi_edges.write("\t".join(value) + " 0\n")