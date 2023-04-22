
from operator import index
from tracemalloc import stop
from xml.etree.ElementTree import PI
import networkx as nx
grafo=nx.Graph()
grafo.add_nodes_from([1,2,3,4,5])
grafo.add_edges_from([(1,4),(3,4),(5,4),(3,2),(1,5),(4,1),(4,3),(4,5),(2,3),(5,1)])

def Vecino(grafoa, raiz, vecinos=[]):
    
    for veci in grafoa[raiz]:
        vecinos.append(veci)
        
        
    return vecinos  

def BFS(grafob,raizb,pila = []):
    
    pila.append(raizb) #Añado la raiz
    salida = []
    Repe=[]
    
    while len(pila)>0:
        nodo = pila.pop(-1)
        
        if not(nodo) in salida:
            aux1=[]
            aux2=[]
            Vecino(grafob, nodo, aux1)
            for i in aux1:
                aux2.insert(0, i)

            for i in aux2:
                pila.append(i)
            print(f'aux1: {aux1}')
            print(f'aux2: {aux2}')
            print(f'Pila: {pila}')    
            salida.append(nodo)
        else:
            Repe.append(nodo)

           
    print(pila)
    return salida
print(f'Salida definitiva {BFS(grafo,1)}')
Pila= [5, 4]
h=[1, 3, 5]
aux=[]
for i in h:
    aux.insert(0, i)

print(aux)
Pila.pop(-1)
for i in aux:
    Pila.append(i)


print(Pila)