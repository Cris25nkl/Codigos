#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
"""
Autores: Cristian David Florez Lopez
         Codigo: 1974001

"""
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#

#                                       TALLER MATEMATICAS DISCRETAS II                                                #

# PUNTO 1: APLICACION DE ALGORITMOS SOBRE GRAFOS
    # BUSQUEDA POR PROFUNDIDAD

import networkx as nx

#CREACION DE UN GRAFO USANDO LAS LIBRERIAS NETWORKVX
grafo=nx.Graph()
grafo.add_nodes_from([1,2,3,4,5])
grafo.add_edges_from([(1,4),(3,4),(5,4),(3,2),(1,5),(4,1),(4,3),(4,5),(2,3),(5,1)])

grafo2=nx.Graph()
grafo2.add_nodes_from([1,2,3])
grafo2.add_edges_from([(1,2),(1,3)])


#---------------------------------------------------------------------------------------------------------------#
# FUNCION AUXILIAR QUE BUSCA Y GUARDA EN UNA LISTA LOS NODOS CONECTADOS CON LA RAIZ
# AL NO SER ARBOLES LA RAIZ SE DEBE INDICAR (Por que nodo desea iniciar)

def Vecino(grafoa, raiz, vecinos=[]):
    for veci in grafoa[raiz]:
        vecinos.append(veci)   
    return vecinos  
#---------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------#
# IMPLEMENTACION DE LA BUSQUEDA POR PROFUNDIDAD ADAPATADA PARA USAR CON GRAFOS

def BFS(grafob,raizb,pila = []):
    
    pila.append(raizb) #Añado la raiz
    salida = []
    Repe=[]#LISTA AUXILIAR DONDE SE GUARDAN LOS NODOS QUE YA SE VISITARON
    
    #CICLO QUE RECORRE EL GRAFO Y LA PILA 
    while len(pila)>0:
        nodo = pila.pop(-1)
        
        if not(nodo) in salida:
            aux1=[]
            aux2=[]
            Vecino(grafob, nodo, aux1)
            #CON ESTOS DOS FOR SE INVIERTEN LOS DATOS DE LOS NODOS PARA GARANTIZAR QUE SE REMPLEZE CORRECTAMENTE LA PILA
            for i in aux1:
                aux2.insert(0, i)

            for i in aux2:
                pila.append(i)
            #-----------------------------------------------------------------------------------------------------------#
            print(f'aux1: {aux1}')
            print(f'aux2: {aux2}')
            print(f'Pila: {pila}')    
            salida.append(nodo)
        else:
            Repe.append(nodo)

           
    print(pila)
    return salida

print(f'Salida definitiva {BFS(grafo,1)}')
print(f'Salida definitiva {BFS(grafo2,1)}')