from nodo import Nodo

class ListSimp():
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.long = 0

    def insertar(self, dato):
        nodo = Nodo(dato)
        self.long += 1
        if self.cabeza:
            self.cabeza.siguiente = nodo
            self.cabeza = nodo
        else:
            self.cabeza = nodo
            self.cola = nodo
        
    def iterar(self):
        actual = self.cola

        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato

    def buscar(self,dato):
        for n in self.iterar():
            if dato == n:
                return True
        return False

    def __getitem__(self, indice):
        try:
            if indice >=0  and indice < self.long:
                actual = self.cola
                for i in range(indice):
                    actual = actual.siguiente
                return actual.dato
            else:
                print('Error índice fuera de rango!')
        except:
            print()

    def __setitem__(self, indice, nuevoDato):
        try:
            if indice >=0  and indice < self.long:
                actual = self.cola
                for i in range(indice):
                    actual = actual.siguiente
                
                
                actual.dato = nuevoDato
            else:
                print('Error índice fuera de rango!')
        except:
            print()

    def eliminar(self, dato):
        actual = self.cola
        anterior = self.cola

        while actual:
            if actual.dato == dato:
                if actual == self.cola:
                    self.cola = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.long -= 1
                return
            anterior = actual
            actual = actual.siguiente

