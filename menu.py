from LeerArchivo import LeerXML
class Menu:
    def PrintMenu(self,opcion):
        try:    
            while opcion != 5:
                print('╔══════════════════════════════════════════╗')
                print('║                   Menú                   ║')
                print('║══════════════════════════════════════════║')
                print('║ 1. Cargar Archivo XML.                   ║')
                print('║ 2. opcion 2            .                 ║')
                print('║ 3. opcion 3.                             ║')
                print('║ 4. Reportes.                             ║')
                print('║ 5. Salir.                                ║')
                print('╚══════════════════════════════════════════╝')
                opcion = int(input("Elige un número del menú de opciones: "))
                self.OpcionesDelMenu(opcion)
                print("") 
        except Exception as e:
            opcion = 0
            self.PrintMenu(opcion)

    def OpcionesDelMenu(self,opcion): 
        if opcion == 1:
            LeerXML.cargar()
        elif opcion == 2:
            print('Esta es la opción 2')
        elif opcion == 3:
            print('Esta es la opción 3')
        elif opcion == 4:
            print('Esta es la opción 4')
        elif opcion == 5:
            print("¡Programa finalizado!")
        else:
            print("\n\n¡La opción que has elegido no existe!")

opcion = 0
call = Menu()
call.PrintMenu(opcion)