class Nodos:
    def __init__(self,matriz,posRobot,estado,recorrido,nodos_visitados):
        self.matriz = matriz
        self.posRobot = posRobot
        self.estado = estado
        self.recorrido = recorrido
        self.nodos_visitados = nodos_visitados
        

    def condicion_de_ganar(self):
        return self.estado[0] and self.estado[1] and self.estado[2]

    def marcar(self):
        """
        if (self.matriz[self.posRobot[1], self.posRobot[0]] == 2 or self.matriz[self.posRobot[1],self.posRobot[0]]==3) and not(self.estado[0]):
            self.estado[0] = True #Si en cuentra uno deposito el primer estado cambia a True
            self.posPrimerDep = (self.posRobot[1], self.posRobot[0]) #Guarda la posicion del deposito
        """
        x,y= self.posRobot[1], self.posRobot[0]
    
        if self.matriz[x, y] == 2 and not(self.estado[0]) and not(self.estado[1]) and not(self.estado[2]):
            self.estado[0] = True
            self.nodos_visitados = []
         
        

        #Al buscar el seguno deposito y encontarlo el recorrido se reinicia
        if self.estado[0] and self.matriz[x,y] == 3 and not(self.estado[1]):
            self.estado[1] = True
            self.nodos_visitados=[]


       
            
        #Llega al centro y gana la partida
        
        if self.estado[0] and self.estado[1] and self.matriz[x,y]==5:
            self.estado[2] = True

        