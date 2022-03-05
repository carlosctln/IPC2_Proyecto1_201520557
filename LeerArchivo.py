from logging import root
from pydoc import doc
from tkinter import filedialog, Tk
from traceback import print_tb
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import parse
from listaSimple import ListSimp
from xml.dom import minidom

doc = ''
root = ''
pisos = ''
xml = ''
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
        self.root = root
        self.doc = doc

        print('**********Listado de pisos**********')
        for piso in pisos:
            nombre = piso.getAttribute("nombre")
            print('Nombre:', nombre)

        self.nombrePiso = input('Ingresa el nombre piso a analizar: ')
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
                print( patrones)
                print(len(patrones))
                
                print('el valor de R es: ', R)
                print('el valor de C es: ', C)
                print('el valor de F es: ', F)
                print('el valor de S es: ', S)
                print('**********Patrones encontrados**********')
                for p in range(len(patrones)):
                    patron1 = patrones[0].text.strip()
                    patron2 = patrones[1].text.strip()

                print(patron1)
                print(patron2)
'''
<piso nombre="ejemplo01">
    <R> 2 </R>
    <C> 4 </C>
    <F> 1 </F>
    <S> 1 </S>
    <patrones>
        <patron codigo="cod11"> 
            WBWBWWWB
        </patron>
        <patron codigo="cod12">
            BWBWWWWW
        </patron>
    </patrones>
</piso>
'''