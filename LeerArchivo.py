from tkinter import filedialog, Tk

class LeerXML:
    def cargar():
        archXML = ''
        Tk().withdraw()
        archivo = filedialog.askopenfilename(
            title= 'Seleccionar un archivo',
            filetypes=[('Archivo XML', '*.xml'),
            ('All Files', '*')])
        with open(archivo, 'r', encoding='utf8') as file:
            if archivo is None:
                print('No se seleccionó ningún archivo\n')
                return None
            else:
                archXML = file.read()
                file.close()
                print('Lectura exitosa\n')
                print(archXML)