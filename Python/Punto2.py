
import networkx as nx
from numpy import append
grafo =nx.Graph()

grafo.add_nodes_from([1,2,3,4])
grafo.add_edges_from([(1,2),(2,3),(3,4),(1,4)])

def k3(grafo, raiz):
    
    aristas=[]
    for i in grafo[raiz]:
        aristas.append(i)
    hay = True
    Res =""
    while hay :
        print(3)
        
        hijoRa = aristas.pop(0)
        if hijoRa in [i for i in grafo[aristas[0]]]:
            print(1)
            Res = "Hay k3"
            hay  = False
        else:
            Res = "No se encontro k3"
            print(2)
    
    return Res


"""
    otros=[]
    for i in grafo[aristas[0]]:
        if i != raiz:
            otros.append(i)
    ultimo=[]
    if len(otros) != 0:
        for i in grafo[otros[0]]:
            ultimo.append(i)
        
    
    if raiz in ultimo:
        print("Es un k3")
    else:
        print("No es k3")

    return aristas, otros
"""
print(k3(grafo,1))