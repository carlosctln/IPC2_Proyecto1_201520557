from tkinter import filedialog, Tk
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import parse
from listaSimple import ListSimp
from xml.dom import minidom

doc = ''
root = ''
pisos = ''
xml = ''
listaPisos = ''
datosmatriz = ListSimp()
class LeerXML:
    def __init__(self):
        self.archivoXml = ''
        self.doc = ''
        self.doc1 = ''
        self.root = ''
        self.xmleFile = ''
        self.nombrePiso = ''

    def cargar(self):
        global doc
        global root
        global xml
        global pisos
        try:
            Tk().withdraw()
            self.archivoXml = filedialog.askopenfilename(
                title='Selecciona un archivo con extención .xml',
                filetypes=(
                    ("Archivos XML", "*.xml"),
                    ("Todos los archivos", "*.*")
                )
            )
            self.xmleFile = open(self.archivoXml)

            if self.xmleFile.readable():
                self.doc = ET.parse(self.xmleFile)
                self.doc1 = minidom.parse(self.archivoXml)
                pisos = self.doc1.getElementsByTagName('piso')
                self.root = self.doc.getroot()
                doc = self.doc
                root = self.root
                xml = self.doc1
                print('¡Lectura exitosa!')
            else:
                print('¡Error en la lectura del archivo!')
        except:
            print('Error vuelve a intentarlo')
        
    def Procesar(self):
        global listaPisos
        self.root = root
        self.doc = doc
        listaPisos = ListSimp()
        lista = ListSimp()
        lista1 = ListSimp()

        for piso in pisos:
            lista.insertar(piso)

        for piso in pisos:
            nombre = piso.getAttribute("nombre")
            lista1.insertar(nombre)

        print('**********Listado de pisos**********')

        for i in range(1,lista1.long):
            for j in range(0,lista1.long - i):
                if(lista1[j + 1] < lista1[j]):
                    aux = lista1[j]
                    lista1[j] = lista1[j + 1]
                    lista1[j + 1] = aux

        for i in range(lista1.long):
            aux = lista1[i]
            for j in range(lista.long):
                aux1 = lista[j]
                if aux1.getAttribute("nombre") == aux:
                    listaPisos.insertar(aux1)

        for d in listaPisos.iterar():
            aux2 = d.getAttribute("nombre")
            print(aux2)

        self.nombrePiso = input('Ingresa el nombre piso a analizar: ')
        self.buscarPiso(self.nombrePiso)

    def buscarPiso(self, nombre):
        listPatrones = ListSimp()
        listPatronesColor = ListSimp()
        nom = nombre

        for elemen in root.findall('piso'):
                    if elemen.get('nombre') == nom:
                        patrones = elemen.findall('./patrones/patron')
                        for p in range(len(patrones)):
                            long = len(patrones)
                            if p <= long:
                                listPatronesColor.insertar(patrones[p].text.strip())
        listPatronesColor1 = ListSimp()
        for i in range(listPatronesColor.long):
            aux = str(i) + '  ' + listPatronesColor[i]
            listPatronesColor1.insertar(aux)

        listPatronesColor = listPatronesColor1

        for elemen in listaPisos.iterar():
            if elemen.getAttribute('nombre') == nom:
                R = elemen.getElementsByTagName("R")[0].firstChild.data
                C = elemen.getElementsByTagName("C")[0].firstChild.data
                F = elemen.getElementsByTagName("F")[0].firstChild.data
                S = elemen.getElementsByTagName("S")[0].firstChild.data

                R = int(R)
                C = int(C)
                F = int(F)
                S = int(S)

                print('**********Patrones encontrados**********')
                patrones = elemen.getElementsByTagName("patrones")[0]
                patrones1 = patrones.getElementsByTagName('patron')
                
                objPatrones = ListSimp()
                for d in patrones1:
                    objPatrones.insertar(d)

                nomPatrones = ListSimp()
                nomPatrones1 = ListSimp()
                cont = 0
                for d in patrones1:
                    nomPatrones.insertar(d.getAttribute('codigo'))
                    nomPatrones1.insertar(str(cont) + '  ' + d.getAttribute('codigo'))
                    cont += 1

                for i in range(1,nomPatrones.long):
                    for j in range(0,nomPatrones.long - i):
                        if(nomPatrones[j + 1] < nomPatrones[j]):
                            aux = nomPatrones[j]
                            nomPatrones[j] = nomPatrones[j + 1]
                            nomPatrones[j + 1] = aux

                for i in range(nomPatrones.long):
                    aux = nomPatrones[i]
                    for j in range(objPatrones.long):
                        aux1 = objPatrones[j]
                        if aux1.getAttribute("codigo") == aux:
                            listPatrones.insertar(aux1)

                '''for d in listPatrones.iterar():
                    print(d.getAttribute("codigo"))'''

        cont = 0
        aux1 = ''
        aux = ''
        
        lisPatComp = ListSimp()
        for i in range(nomPatrones1.long):
            cont1 = str(i) + '  '
            aux = str(nomPatrones1[i]).startswith(cont1)
            aux1 = str(nomPatrones1[i]).replace(cont1, '')
            if aux:
                for j in range(listPatronesColor.long):
                    cont2 = str(j) + '  '
                    aux2 = str(listPatronesColor[j]).startswith(cont2)
                    aux3 = str(listPatronesColor[i]).replace(cont2, '')
                    if i == j:
                        aux4 = aux1 + ' : ' + aux3
                        lisPatComp.insertar(aux4)
                    
        for i in range(1,lisPatComp.long):
            for j in range(0,lisPatComp.long - i):
                if(lisPatComp[j + 1] < lisPatComp[j]):
                    aux = lisPatComp[j]
                    lisPatComp[j] = lisPatComp[j + 1]
                    lisPatComp[j + 1] = aux

        for i in lisPatComp.iterar():
            print(i)

        global datosmatriz
        if datosmatriz.long > 0:
            datosmatriz = ListSimp()

        if R > 0:
            if C > 0:
                if F > 0:
                    if S > 0:
                        datosmatriz.insertar(nom)
                        patronInicial = input('Ingrese el nonmbre del patron inicial: ')
                        for d in range(lisPatComp.long):
                            aux = str(lisPatComp[d]).startswith(patronInicial)
                            if aux:
                                datosmatriz.insertar(lisPatComp[d])

                        patronFinal = input('Ingrese el nonmbre del patron final: ')
                        for d in range(lisPatComp.long):
                            aux = str(lisPatComp[d]).startswith(patronFinal)
                            if aux:
                                datosmatriz.insertar(lisPatComp[d])
                        datosmatriz.insertar(R)
                        datosmatriz.insertar(C)
                        datosmatriz.insertar(F)
                        datosmatriz.insertar(S)
            
        else:
            print('Error un paramétro es menor a 0')

        print('**********Se creara una matriz con los siguientes datos**********')
        try:
            print('Nombre:', datosmatriz[0])
            print('Patron inicial: ',datosmatriz[1])
            print('Patron final: ',datosmatriz[2])
            print('Filas:', datosmatriz[3])
            print('columnas:', datosmatriz[4])
            print('costo por volteo:', datosmatriz[5])
            print('Costo por intercambio:', datosmatriz[6])
        except:
            print('Error faltan elementos para crear la matiz')


