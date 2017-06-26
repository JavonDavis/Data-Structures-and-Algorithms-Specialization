def explore(v):
    visited[v] = True
    for (v, w) in edges:
        if not visited[w]:
            explore(w)
            
def dfs(G):
    for all v in vertices mark v unvisited
    for v in vertices:
        if not visited[v]:
            explore(v)
            

# Goal is to find all the connected components in a graph G,
# Can be done with a simple modification to explore and dfs
# Basical we're going to label the connected components as 
# we do the dfs
def connected_components(G):
    for all v in vertices mark v unvisited
    cc = 1
    for v in vertices:
        if not visited[v]:
            explore(v, cc)
            cc += 1

# Modification to explore for connected components algorithm          
def explore(v, cc):
    visited[v] = True
    cComponent[v] = cc
    for (v, w) in edges:
        if not visited[w]:
            explore(w)
            
            
# Previsit and Postvisit Orderings
# Modification to explore to handle previsit and postvist functions
def explore(v):
    visited[v] = True
    previsit(v) # This function can be used to store additional information about the traversal
    for (v, w) in edges:
        if not visited[w]:
            explore(w)
    postvisit(v) # This function can be used to store additional information about the traversal