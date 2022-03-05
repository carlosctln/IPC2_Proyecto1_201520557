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

        for piso in pisos:
            nombre = piso.getAttribute("nombre")
            listaPisos.insertar(nombre)
        print('**********Listado de pisos**********')
        print('el tamaño de la lista es: ', listaPisos.long)

        for i in range(1,listaPisos.long):
            for j in range(0,listaPisos.long - i):
                if(listaPisos[j + 1] < listaPisos[j]):
                    aux = listaPisos[j];
                    listaPisos[j] = listaPisos[j + 1];
                    listaPisos[j + 1] = aux;

        for d in listaPisos.iterar():
            print(d)

        self.nombrePiso = input('Ingresa el nombre piso a analizar: ')
        print(listaPisos.buscar(self.nombrePiso))
        self.buscarPiso(self.nombrePiso)

    def buscarPiso(self, nombre):
        nom = nombre
        for elemen in root.findall('piso'):
            if elemen.get('nombre') == nom:
                R = int(elemen.find('./R').text) 
                C = int(elemen.find('./C').text) 
                F = int(elemen.find('./F').text) 
                S = int(elemen.find('./S').text)
                patrones = elemen.findall('./patrones/patron')
                #print( patrones)
                #print(len(patrones))
                
                #print('el valor de R es: ', R)
                #print('el valor de C es: ', C)
                #print('el valor de F es: ', F)
                #print('el valor de S es: ', S)
                #print('**********Patrones encontrados**********')
                for p in range(len(patrones)):
                    long = len(patrones)
                    if p <= long:
                        patron1 = patrones[0].text.strip()
                        patron2 = patrones[1].text.strip()

                #print(patron1)
                #print(patron2)

