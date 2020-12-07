# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:33:53 2020

@author: Lenovo-PC
"""
"""
def transitive_closure(a):
    closure = set(a)
    while True:
        new_relations = set((x,w) for x,y in closure for q,w in closure )

        closure_until_now = closure | new_relations

        if closure_until_now == closure:
            break
        

        closure = closure_until_now

    return closure
print(transitive_closure([(1, 2),(1, 3),(2, 4),(4, 5)]))"""
"""
def transitive_closure(a):
    closure = []
    for i in a:
        b=list(i)
        closure.append(b)
        a=closure
        for i in a:
            if [i[0],i[0]] not in closure:
                closure.append([i[0],i[0]])
            if [i[1],i[1]] not in closure:
                closure.append([i[1],i[1]])
        
        for j in range(len(closure)):
            for i in range(len(closure)):
                for k in range(len(closure)):
                    
                    if ([a[i][0],a[j][1]] and [a[j][0],a[k][1]] in closure)and not([a[i][0],a[k][1]]  in closure):
                        closure.append([a[i][0],a[k][1]])
                    
    print(closure)"""


def transitive_closure(a):
    closure = []
    for i in a:
        b=list(i)
        closure.append(b)
        a=closure
        setA=[]
        
    for i in a:
        
        if [i[0],i[0]] not in closure:
            closure.append([i[0],i[0]])
        if i[0] not in setA:
            setA.append(i[0])
            
        if [i[1],i[1]] not in closure:
            closure.append([i[1],i[1]])
        if i[1] not in setA:
            setA.append(i[1])
        """"    
    for j in range(len(setA)):
        for i in range(len(setA)):
            for k in range(len(setA)):
                if (([setA[i],setA[j]] in closure) and( [setA[j],setA[k]] in closure))and not([setA[i],setA[k]]  in closure):
                    closure.append([setA[i],setA[k]])
                    """
                 
    for i in range(len(setA)):
        i_tuple=[]
        i_tuple.append(i for i in range(len(setA)))
        for j in i_tuple:
            check=[]
            for k in range(i) :
               check.append([i_tuple[k],i_tuple[k+1]])
               if i_tuple[k+1]==i_tuple[-1]:
                   break
             
            if closure.__contains__(check):
                closure.append([i_tuple[0],i_tuple[-1]])
    closureSet=set()
    for i in closure:
        i=tuple(i)
        closureSet.add(i)
        
    
        
    print(closureSet)
        
            
 
            
                        
                    
        
         
    
    
        
        
    
   # for i in closure:
       # for i in closure:
     
transitive_closure([("a","b"),("a","c"),("b","d"),("d","e")])



"""
def warshall(a):
    assert (len(row) == len(a) for row in a)
    n = len(a)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j] = a[i][j] or (a[i][k] and a[k][j])
    return a
warshall([[1,2],[1,3],[2,4],[4,5]])
"""
"""
# Floyd Warshall Algorithm in python


# The number of vertices
nV = 2




# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print(distance)


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G =[[1,2],[1,3],[2,4],[4,5]]
floyd_warshall(G)
"""

        