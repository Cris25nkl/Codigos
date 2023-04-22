import numpy as np
from xml.dom import NotFoundErr

#Esta funcion intenta leer un fichero que contiene la cantidad de nodos y la matriz d adjacencia
def LeerArchivo(archivo):
    lineas = []
    try:
        with open(archivo) as obj:
            lineas = obj.readlines()
    except FileNotFoundError:
        print("El archivo no se a encontrado")
    
    return lineas #Regresa una lista
#----------------------------------------------------------------------------------------------------------#

#Con esta funcion se convierten los datos del archivo ya que se leen como string, se crea y se retorna la lista
#de las etiquetas, y la matriz de adjacencia.
def ConversionDatos(ListaStr):
    #lineas=LeerArchivo(ListaStr)
    MAadj = []
    Etiquetas = [i+1 for i in range(int(ListaStr.pop(0)))]
    aux3=[]
    for elemento in ListaStr:
        aux1=elemento.split()
        aux2=[]
        for i in aux1:
            try:
                i=int(i)
                aux2.append(i)
            except:
                print("No se puede convertir, verifique el contenido de su archivo")
        aux3.append(aux2)
    MAadj = np.array(aux3)    
    
    return MAadj, Etiquetas
#-------------------------------------------------------------------------------------------------------#

#En esta funcion se implementa una busqueda en la matriz para encontrar las aristas que estan unidas con los nodos
def BuscaArista(matriz, etiquetas):
    aristas=[]
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if matriz[i][j] == 1:
                    aristas.append((etiquetas[i],etiquetas[j]))
                
   
    return aristas
#----------------------------------------------------------------------------------------------------------------#

#Funcion main donde se hace los respectivos llamados a las funciones previas en conjunto
def main(ruta):
    ListaBase = LeerArchivo(ruta)
    Mtad, Eti=ConversionDatos(ListaBase)
    Aristas=BuscaArista(Mtad,Eti)


    return Aristas

print(main("Texto.txt"))


