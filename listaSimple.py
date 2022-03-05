from importlib import import_module
from nodo import Nodo

class ListSimp():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def agregarUltimo(self, dato):
        if self.vacia() == True:
            self.primero = Nodo(dato)
            self. ultimo = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
        
    def recorrido(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente

    def eliminarUltimo(self):
        aux = self.primero
        while aux.siguiente != self.ultimo:
            aux = aux.siguiente
        aux.siguiente = None
        self.ultimo = aux