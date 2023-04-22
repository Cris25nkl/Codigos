import Lectura2 as l
from Nodos import Nodos
import BuscarDirectorio as b
"""
0 si es una casilla libre
1 si es un obstaculo
2 si es la casilla que tiene el deposito de basura de 2 kilos
3 si es la casilla que tiene el deposito de basura de 3 kilos
4 si es el punto de inicio
5 si es el punto de reciclaje
"""

Mapa = l.main(b.abrir())

def bfs (mapa):
    nodosCreados= 0
    nodosExpandidos = 0

    for i in range(mapa.shape[0]):
        for j in range(mapa.shape[1]):
            if mapa[i][j] == 4:
                posRobot = (j,i) #x,y
                mapa[i][j] = 0
                break
    raiz = Nodos(
        mapa,
        posRobot,
        [False,False,False],
        [posRobot], #Recorrio
        [posRobot],  #Visitado      
    )
   

    cola = [raiz]

    while len(cola) > 0:
        nodo = cola.pop(0)
        nodosExpandidos += 1
        if (nodo.condicion_de_ganar()):
            return nodo.recorrido, nodosCreados, nodosExpandidos #Solucion

        x  = nodo.posRobot[0]
        y = nodo.posRobot[1]

        #Generar hijos

        #Arriba

        xI = x
        yI = y - 1

        if yI >= 0 and not((xI,yI) in nodo.nodos_visitados) and nodo.matriz[y,x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()
            nodos_visitados.append((xI, yI))
            recorrido = nodo.recorrido.copy()
            recorrido.append((xI,yI))
            estado = nodo.estado.copy()

            hijo = Nodos(
                nodo.matriz,
                (xI, yI),
                estado,
                recorrido,
                nodos_visitados
            )
            nodosCreados += 1
            hijo.marcar()
            cola.append(hijo)
            
        #Abajo

        xI = x
        yI = y + 1

        if yI < mapa.shape[0] and not((xI,yI) in nodo.nodos_visitados) and nodo.matriz[y,x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()
            nodos_visitados.append((xI, yI))
            recorrido = nodo.recorrido.copy()
            recorrido.append((xI,yI))
            estado = nodo.estado.copy()

            hijo = Nodos(
                        nodo.matriz,
                        (xI, yI),
                        estado,
                        recorrido,
                        nodos_visitados
            )
            nodosCreados += 1
            hijo.marcar()
            cola.append(hijo)
        


        #Izquierda

        xI = x - 1
        yI = y

        if xI >= 0 and not((xI,yI) in nodo.nodos_visitados) and nodo.matriz[y,x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()
            nodos_visitados.append((xI, yI))
            recorrido = nodo.recorrido.copy()
            recorrido.append((xI,yI))
            estado = nodo.estado.copy()

            hijo = Nodos(
                        nodo.matriz,
                        (xI, yI),
                        estado,
                        recorrido,
                        nodos_visitados
            )
            nodosCreados += 1
            hijo.marcar()
            cola.append(hijo)

        #Derecha

        xI = x + 1
        yI = y

        if xI < mapa.shape[1] and not((xI,yI) in nodo.nodos_visitados) and nodo.matriz[y,x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()
            nodos_visitados.append((xI, yI)) 
            recorrido = nodo.recorrido.copy()
            recorrido.append((xI,yI))
            estado = nodo.estado.copy()

            hijo = Nodos(
                        nodo.matriz,
                        (xI, yI),
                        estado,
                        recorrido,
                        nodos_visitados
            )
            nodosCreados += 1
            hijo.marcar()
            cola.append(hijo)

    return "No hay solucion", nodosCreados, nodosExpandidos
    
    
print(bfs(Mapa))