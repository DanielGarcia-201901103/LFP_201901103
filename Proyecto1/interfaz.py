import sys
import tkinter as tk
from tkinter import CENTER, RIGHT, Y, Scrollbar, filedialog, Tk, ttk
from tkinter.messagebox import showerror, showinfo, showwarning
import webbrowser
from automataAFD import AFD 
from operar import Operaciones
almacenar =""
#Metodos y Funciones para la sección de Archivo *********************************************************************************
def abrir(event = None):
    urlArchivo = filedialog.askopenfilename(initialdir="./", title="Seleccione un Archivo", filetypes=(("Archivo json", "*.json"), ("all files", "*.*")))
    if urlArchivo != "":
        leer = open(urlArchivo, "rt")
        global almacenar
        almacenar = leer.read()
        leer.close()
        showinfo(title="Abierto", message="Archivo leído exitosamente")
        menuArchivo.entryconfig(1,state = tk.NORMAL)
        menuArchivo.entryconfig(2,state = tk.NORMAL)
        menuArchivo.entryconfig(3,state = tk.NORMAL)
        menuArchivo.entryconfig(4,state = tk.NORMAL)
    else :
        #showerror(title="Error", message="El tamaño maximo de organismos es: 1000 \nPorfavor ingrese menos organismos")
        showwarning(title="Advertencia", message="No ingresó ningun archivo")
def guardar(event = None):
    pass

def guardarComo(event = None):
    guardar_Como = filedialog.asksaveasfilename(initialdir="./", title="Guardar Como", filetypes=(("Archivo json", "*.json"), ("all files", "*.*")))
    if guardar_Como != "":
        showinfo(title="Guardado", message="Archivo guardado exitosamente")
    else :
        showwarning(title="Advertencia", message="¡Si no guarda el archivo se perderan los datos!")

def analizar(event = None):
    global almacenar
    if almacenar != "":
        enviandoAnalisis = AFD()
        enviandoAnalisis.analizando(almacenar)
        enviandoAnalisis.imprimir_tokens()

        tablaoperaciones = enviandoAnalisis.tabla
        print(tablaoperaciones[2].row)
        print(tablaoperaciones[3].lexema)
        #validar que cada vez que abra una llave omitiendo la primera llave     del archivo
        #y cuando termine esa llave sea una operacion
        #luego dentro de esa validacion validar si viene corchetes sea otra     operacion y esa operacion se debe realizar primero antes que la     anterior
        contador = 1
        while tablaoperaciones[contador].lexema != "}":
            if tablaoperaciones[contador].lexema.lower() == "operacion":
                print("operacion")
                pass
            contador +=1

            pass
        #La siguiente linea servirá para enviar los datos al objeto de  operaciones
        #operarD = Operaciones(valor1,valor2,tipo)
    else:
        showwarning(title="Advertencia", message="Por favor cargue un archivo")

def errores(event = None):
    global almacenar
    if almacenar != "":
        pass
    else:
        showwarning(title="Advertencia", message="Por favor cargue un archivo")

#\********************************************************************************************************************************
#Metodos y funciones para la seccion de Ayuda ************************************************************************************
def manualUsuario(event = None):
    pathUsuario = "Proyecto1\Documentacion\Manual Usuario.pdf"
    webbrowser.open_new(pathUsuario)

def manualTecnico(event = None):
    pathTecnico = "Proyecto1\Documentacion\Manual Tecnico.pdf"
    webbrowser.open_new(pathTecnico)

def temasAyuda(event = None):
    showinfo(title="Información del desarrollador", message="Josué Daniel Rojché García\nCarnet: 201901103")
#\********************************************************************************************************************************
#Main
if __name__ == '__main__':
    menu = tk.Tk()
    menu.title("PROYECTO NO.1")
    menu.geometry("607x400")
    menu.configure(bg="#212F3C")
    menu.resizable(False, False)
    #Crea la barra del menu
    barra_Menu = tk.Menu()
    #Crea el primer elemento el cual será para archivo y se enlaza a la barra
    menuArchivo = tk.Menu(barra_Menu, tearoff=False)
    #Al add_command se le puede pasar el parametro accelerator="Ctrl+N" para agregar un atajo con el teclado
    menuArchivo.add_command(label="Abrir",accelerator="Ctrl+N",command= abrir)
    menu.bind_all("<Control-n>",abrir )
    menuArchivo.add_command(label="Guardar", command= guardar, state=tk.DISABLED)
    menuArchivo.add_command(label="Guardar Como", command=guardarComo, state=tk.DISABLED)
    menuArchivo.add_command(label="Analizar", command= analizar, state=tk.DISABLED)
    menuArchivo.add_command(label="Errores", command= errores, state=tk.DISABLED)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Salir", command=menu.quit, activebackground="Red")

    menuAyuda= tk.Menu(barra_Menu, tearoff=False)
    menuAyuda.add_command(label="Manual de Usuario", command= manualUsuario)
    menuAyuda.add_command(label="Manual Tecnico", command= manualTecnico)
    menuAyuda.add_command(label="Temas de Ayuda", command= temasAyuda)

    # a la barra menú le agregamos el menuArchivo
    barra_Menu.add_cascade(menu= menuArchivo, label= "Archivo")
    barra_Menu.add_cascade(menu= menuAyuda, label= "Ayuda")

    menu.config(menu=barra_Menu)
    menu.mainloop() # Permite mostrar la ventana 