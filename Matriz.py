from nodoOr import NodoOr

class MatrizOrtogonal:
    def __init__(self):
        self.cabeza = None
        self.contador = 0

    def vacio(self):
        return self.cabeza==None

    def ingresardatos(self, dato, fila, columna):
        if self.vacio():
            nuevoprin = NodoOr(dato, fila, columna)
            self.cabeza = nuevoprin
            self.contador+=1
        else:
            aux = self.cabeza
            while aux.abajo!=None:
                aux = aux.abajo
            if self.contador!=fila:
                self.contador+=1
                nuevoprin = NodoOr(dato, fila, columna)
                aux.abajo = nuevoprin
                nuevoprin.arriba = aux
            else:
                while aux.siguiente!=None:
                    aux = aux.siguiente
                nuevoprin = NodoOr(dato, fila, columna)
                aux.siguiente = nuevoprin
                nuevoprin.anterior = aux
                if self.contador>1:
                    aux2 = aux.arriba.siguiente
                    aux2.abajo = nuevoprin
                    nuevoprin.arriba = aux2

    def mostrarMatriz(self):
        aux = self.cabeza
        img =""
        while (aux.abajo!=None) | (aux.siguiente!=None):
            img = img + aux.dato
            if aux.siguiente !=None:
                aux = aux.siguiente
            else:
                img = img + "\n"
                if aux.abajo!=None:
                    aux = aux.abajo
                    while aux.anterior!=None:
                        aux = aux.anterior
        img = img+aux.dato
        return img
