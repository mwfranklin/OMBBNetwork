from collections import Counter
import re
import glob
import sys
import numpy as np

cutoff = 1

all_barrels = []
with open("BarrelChars85.txt", "r") as barrel_list:
    for line in barrel_list:
        if "Barrel" not in line:
            line = line.split("\t")
            all_barrels.append(line[0])

graph = {} #relationship list for each node
with open("data/FiltData_E20_v6_2018_Renumb_2.txt", "r") as inData:
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

#print(multiple_edges)                
for key in stubs:
    del graph[key]
#graph now only consists of pdbs with multiple connections to the same pdb

multi_edge_lines = []
with open("data/FiltData_E20_v6_2018_Renumb_2.txt", "r") as inData, open("data/NoMultiEdgesE%s_v6_2.txt"%cutoff, "w+") as all_edges, open("data/MultiEdgesE%s_v6_2.txt"%cutoff, "w+") as multi_edges, open("data/MultiEdgesE%s_v6_DontCheck_2.txt"%cutoff, "w+") as dontcheck:
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
                    all_edges.write("\t".join(line) + "\t1\n")
        else:
            all_edges.write(line.strip() + "\tInCyto?\n")
            multi_edges.write(line.strip() + "\tInCyto?\n")
    
    #remove the obvious near duplicates
    for value in multiple_edges: #for each pair of PDBs with multiconnections:
        #print(value)
        edges = [] #edges relating to that pair
        for line in multi_edge_lines:
            if (value[0] in line and value[1] in line):
                edges.append(line)
        
        if len(edges) == 1: 
            print("Something went wrong ", line)
            all_edges.write("\t".join(line) + "\n")
        else:
            kept_edges = []
            #print("starting:")
            #print(edges)    
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
                    elif (abs(int(edges[x][7]) - int(first_row[7])) < 6 and abs(int(edges[x][9]) - int(first_row[9])) < 6):
                        #print(first_row, edges[x])
                        #print("ends the same", abs(int(edges[x][8]) - int(first_row[8])), abs(int(edges[x][10]) - int(first_row[10])))
                        if abs( abs(int(edges[x][6]) - int(first_row[6])) + abs(int(edges[x][8]) - int(first_row[8])) ) < 15:
                            #print("start ~same", abs(int(edges[x][7]) - int(first_row[7])), abs(int(edges[x][9]) - int(first_row[9])))
                            if float(edges[x][2]) <= e_value: 
                                del edges[0]
                                print_row = False
                                break
                            else:
                                pop_list.append(x)
                        #check if alignment is a perfect subset
                        else:
                            #print("Ends identical ", first_row, edges[x])
                            if int(edges[x][3]) < int(first_row[3]):
                                if len(first_row[10].split(edges[x][10][5:-5])) == 2 and len(first_row[11].split(edges[x][11][5:-5])) == 2:
                                    #print(first_row, edges[x])
                                    pop_list.append(x)
                            elif int(edges[x][3]) > int(first_row[3]):
                                if len(edges[x][10].split(first_row[10][5:-5])) == 2 and len(edges[x][11].split(first_row[11][5:-5])) == 2:
                                    #print(first_row, edges[x])
                                    del edges[0]
                                    print_row = False
                                    break
                    #check if alignment is a perfect subset
                    else:
                        #print("Starts identical ", first_row, edges[x])
                        if int(edges[x][3]) < int(first_row[3]):
                            if len(first_row[10].split(edges[x][10][5:-5])) == 2 and len(first_row[11].split(edges[x][11][5:-5])) == 2:
                                #print(first_row, edges[x])
                                pop_list.append(x)
                        elif int(edges[x][3]) > int(first_row[3]):
                            if len(edges[x][10].split(first_row[10][5:-5])) == 2 and len(edges[x][11].split(first_row[11][5:-5])) == 2:
                                #print(first_row, edges[x])
                                del edges[0]
                                print_row = False
                                break
                                
                #if value[1] == "1pho_A" and value[0] == "2wjr_A": print(pop_list, print_row)
                for y in reversed(pop_list): del edges[y]
                
                if print_row == True: 
                    #all_edges.write("\t".join(first_row) + "\n")
                    kept_edges.append(first_row)
                    del edges[0]
            
            #print("Final edges: ")
            #print(kept_edges)
            
            if len(kept_edges) == 1:
                all_edges.write("\t".join(kept_edges[0]) + "\t1\n")
            else:
                keep_row = kept_edges[0]
                for x in range(1,len(kept_edges)):
                    if float(kept_edges[x][2]) < float(keep_row[2]):
                        keep_row = kept_edges[x]
                        
                if len(kept_edges) == 2:
                    if (int(kept_edges[1][7]) < int(kept_edges[0][6])+10) or (int(kept_edges[1][6]) > int(kept_edges[0][7])-10) or (int(kept_edges[1][9]) < int(kept_edges[0][8])+10) or (int(kept_edges[1][8]) > int(kept_edges[0][9])-10):
                        for value in kept_edges:
                            if value == keep_row:
                                dontcheck.write("\t".join(value) + "\t1\n")
                            else:
                                dontcheck.write("\t".join(value) + "\t0\n")
                    elif (abs(int(kept_edges[1][7]) - int(kept_edges[0][7])) < 10 and abs(int(kept_edges[1][8]) - int(kept_edges[0][8])) < 10 and abs(int(kept_edges[1][6]) - int(kept_edges[0][6])) > 25 and abs(int(kept_edges[1][9]) - int(kept_edges[0][9])) > 25):
                        for value in kept_edges:
                            if value == keep_row:
                                dontcheck.write("\t".join(value) + "\t1\n")
                            else:
                                dontcheck.write("\t".join(value) + "\t0\n")             
                    elif (abs(int(kept_edges[1][7]) - int(kept_edges[0][7])) > 25 and abs(int(kept_edges[1][8]) - int(kept_edges[0][8])) > 25 and abs(int(kept_edges[1][6]) - int(kept_edges[0][6])) < 10 and abs(int(kept_edges[1][9]) - int(kept_edges[0][9])) < 10):
                        for value in kept_edges:
                            if value == keep_row:
                                dontcheck.write("\t".join(value) + "\t1\n")
                            else:
                                dontcheck.write("\t".join(value) + "\t0\n")
                    elif (abs(int(kept_edges[1][7]) - int(kept_edges[0][7])) < 6 and abs(int(kept_edges[1][9]) - int(kept_edges[0][9])) > 25) or (abs(int(kept_edges[1][7]) - int(kept_edges[0][7])) > 25 and abs(int(kept_edges[1][9]) - int(kept_edges[0][9])) < 6):
                        for value in kept_edges:
                            if value == keep_row:
                                dontcheck.write("\t".join(value) + "\t1\n")
                            else:
                                dontcheck.write("\t".join(value) + "\t0\n")
                    elif (abs(int(kept_edges[1][6]) - int(kept_edges[0][6])) < 6 and abs(int(kept_edges[1][8]) - int(kept_edges[0][8])) > 25) or (abs(int(kept_edges[1][6]) - int(kept_edges[0][6])) > 25 and abs(int(kept_edges[1][8]) - int(kept_edges[0][8])) < 6):
                        for value in kept_edges:
                            if value == keep_row:
                                dontcheck.write("\t".join(value) + "\t1\n")
                            else:
                                dontcheck.write("\t".join(value) + "\t0\n")                                       
                    else:
                        for value in kept_edges:
                            if value == keep_row:
                                multi_edges.write("\t".join(value) + "\t1\n")
                            else:
                                multi_edges.write("\t".join(value) + "\t0\n")
                else:
                    for value in kept_edges:
                        if value == keep_row:
                            multi_edges.write("\t".join(value) + "\t1\n")
                        else:
                            multi_edges.write("\t".join(value) + "\t0\n")