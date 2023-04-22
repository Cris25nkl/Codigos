import networkx as nx
import matplotlib.pyplot as plt
import numpy as np



"""
grafo = nx.Graph()
grafo = grafo.to_undirected()

grafo.add_nodes_from([1,2,3,4,5,6])
grafo.add_edges_from([(1,2),(1,3),(2,5),(6,4)])

nx.draw(grafo, with_labels=True)
#plt.show()
print(nx.adjacency_matrix(grafo).todense())
"""
grafo = np.array(
    [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
    ]
)
nodos=[1,2,3,4]

aristas=[]

for i in range(grafo.shape[0]):
    for j in range(grafo.shape[1]):
        if grafo[i][j] == 1:
            aristas.append((nodos[i],nodos[j]))

print(grafo)
print(aristas)


Dgrafo=nx.Graph()
Dgrafo = Dgrafo.to_undirected()
Dgrafo.add_nodes_from(nodos)
Dgrafo.add_edges_from(aristas)
print(Dgrafo.nodes)
#nx.draw(Dgrafo, with_labels=True)
#plt.show()

