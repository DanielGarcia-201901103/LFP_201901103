import sys
import tkinter as tk
from tkinter import CENTER, RIGHT, Y, Scrollbar, filedialog, Tk, ttk
from tkinter.messagebox import showerror, showinfo, showwarning
import webbrowser
from automataAFD import AFD 
from operar import Operaciones
almacenar =""
urlAlmacenar = ""
enviandoAnalisis = AFD()
#Metodos y Funciones para la sección de Archivo *********************************************************************************
def abrir(event = None):
    global urlAlmacenar
    urlArchivo = filedialog.askopenfilename(initialdir="./", title="Seleccione un Archivo", filetypes=(("Archivo json", "*.json"), ("all files", "*.*")))
    if urlArchivo != "":

        leer = open(urlArchivo, "rt")
        urlAlmacenar = urlArchivo
        global almacenar
        almacenar = leer.read()
        leer.close()

        textLeer.configure(state=tk.NORMAL)
        textLeer.insert("1.0", almacenar)
        
        menuArchivo.entryconfig(1,state = tk.NORMAL)
        menuArchivo.entryconfig(2,state = tk.NORMAL)
        menuArchivo.entryconfig(3,state = tk.NORMAL)
        menuArchivo.entryconfig(4,state = tk.NORMAL)
        
        showinfo(title="Abierto", message="Archivo leído exitosamente")
    else :
        #showerror(title="Error", message="El tamaño maximo de organismos es: 1000 \nPorfavor ingrese menos organismos")
        showwarning(title="Advertencia", message="No ingresó ningun archivo")
def guardar(event = None):
    saveArchivo = open(urlAlmacenar, "w")
    saveArchivo.write(textLeer.get("1.0","end"))
    saveArchivo.close()

def guardarComo(event = None):
    guardar_Como = filedialog.asksaveasfilename(initialdir="./", title="Guardar Como", filetypes=(("Archivo json", ".json"), ("all files", "*.*")))
    if guardar_Como != "":
        saveComoArchivo = open(guardar_Como +".json", "w") #+".json"
        saveComoArchivo.write(textLeer.get("1.0","end"))
        saveComoArchivo.close()
        
        showinfo(title="Guardado", message="Archivo guardado exitosamente")
    else :
        showwarning(title="Advertencia", message="¡Si no guarda el archivo se perderan los datos!")

def analizar(event = None):
    #https://docs.python.org/es/3/reference/lexical_analysis.html
    global almacenar
    if almacenar != "":
        try:
            enviandoAnalisis.analizando(almacenar)
            #enviandoAnalisis.imprimir_tokens()
            enviandoAnalisis.analizandoSintacticamente()
        except Exception as e:
            pass
    else:
        showwarning(title="Advertencia", message="Por favor cargue un archivo")

def errores(event = None):
    global almacenar
    if almacenar != "":
        textErores.configure(state=tk.NORMAL)
        escribiendoE = enviandoAnalisis.erroresValidados()
        textErores.insert("1.0", escribiendoE)
        textErores.configure(state="disabled")

        archivoErrores = open(".\Proyecto1\ERRORES_201901103.json","w")
        archivoErrores.write(escribiendoE)
        archivoErrores.close()
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
    showinfo(title="Información del desarrollador", message="Josué Daniel Rojché García\nCarnet: 201901103\nLenguajes Formales y de Programación\nSección: A-")
#\********************************************************************************************************************************
#Main
if __name__ == '__main__':
    menu = tk.Tk()
    menu.title("PROYECTO NO.1")
    menu.geometry("900x400")
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

    textLeer = tk.Text()
    textLeer.configure(bg="#C8C885", state="disabled")
    textLeer.place(x= 5, y =5, height= 350, width= 440)

    textErores = tk.Text()
    textErores.configure(bg="#BFBF02", state="disabled") #, state="disabled"
    textErores.place(x= 455, y =5, height= 350, width= 440)

    label1 = tk.Label(menu, text="Archivo abierto", bg="#212F3C", fg="#FFFFFF",width= 20, font=("Arial", 13)).place(x= 125, y =370)

    label1 = tk.Label(menu, text="Archivo Errores", bg="#212F3C", fg="#FFFFFF",width= 20, font=("Arial", 13)).place(x= 575, y =370)

    menu.config(menu=barra_Menu)
    menu.mainloop() # Permite mostrar la ventana 

    #https://recursospython.com/codigos-de-fuente/bloc-de-notas-simple-con-tkinter/
    #https://www.delftstack.com/es/howto/python-tkinter/how-to-get-the-input-from-tkinter-text-box/