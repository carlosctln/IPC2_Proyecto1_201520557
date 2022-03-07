from LeerArchivo import LeerXML
class Menu:
    def __init__(self):
        self.opcion = 0

    def PrintMenu(self,opcion):
        self.opcion = opcion
        #try:    
        while self.opcion != 5:
            print('╔══════════════════════════════════════════╗')
            print('║                   Menú                   ║')
            print('║══════════════════════════════════════════║')
            print('║ 1. Cargar Archivo XML.                   ║')
            print('║ 2. Analizar piso.                        ║')
            print('║ 3. Salir.                                ║')
            print('╚══════════════════════════════════════════╝')
            self.opcion = int(input("Elige un número del menú de opciones: "))
            self.OpcionesDelMenu(self.opcion)
            print("") 
        #except Exception as e:
            #print('Error', e)
            #self.opcion = 0
            #self.PrintMenu(self.opcion)

    def OpcionesDelMenu(self,opcion):
        self.opcion = opcion

        if self.opcion == 1:
            self.cargar = LeerXML()
            self.cargar.cargar()

        elif self.opcion == 2:
            self.procesar = LeerXML()
            self.procesar.Procesar()
        elif self.opcion == 3:
            print("¡Programa finalizado!")
        else:
            print("\n\n¡La opción que has elegido no existe!")

opcion = 0
call = Menu()
call.PrintMenu(opcion)