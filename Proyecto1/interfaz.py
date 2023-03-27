import os
import tkinter as tk
from tkinter import CENTER, RIGHT, Y, Scrollbar, filedialog, Tk, ttk
from tkinter.messagebox import showerror, showinfo, showwarning
import webbrowser
from automataAFD import AFD 
#import graphviz

almacenar =""
urlAlmacenar = ""
enviandoAnalisis = AFD()
#Metodos y Funciones para la sección de Archivo *********************************************************************************
def abrir(event = None):
    try:
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
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")
def guardar(event = None):
    try:
        global almacenar
        saveArchivo = open(urlAlmacenar, "w")
        saveArchivo.write(textLeer.get("1.0","end"))
        saveArchivo.close()
        
        almacenar = str(textLeer.get("1.0","end"))
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")
    
def guardarComo(event = None):
    try:
        guardar_Como = filedialog.asksaveasfilename(initialdir="./", title="Guardar Como", filetypes=(("Archivo json", ".json"), ("all files", "*.*")))
        if guardar_Como != "":
            saveComoArchivo = open(guardar_Como +".json", "w") #+".json"
            saveComoArchivo.write(textLeer.get("1.0","end"))
            saveComoArchivo.close()
            
            showinfo(title="Guardado", message="Archivo guardado exitosamente")
        else :
            showwarning(title="Advertencia", message="¡Si no guarda el archivo se perderan los datos!")
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")
def analizar(event = None):
    #https://docs.python.org/es/3/reference/lexical_analysis.html
    global almacenar
    if almacenar != "":
        try:
            enviandoAnalisis.analizando(almacenar)
            #enviandoAnalisis.imprimir_tokens()
            
            operacionesGra = enviandoAnalisis.analizandoSintacticamente()
            #ESCRIBIENDO .DOT
            archivoGrafica = open(".\Proyecto1\RESULTADOS_201901103.dot","w")
            archivoGrafica.write(operacionesGra)
            archivoGrafica.close()
            os.system("dot -Tpdf .\Proyecto1\RESULTADOS_201901103.dot -o  .\Proyecto1\RESULTADOS_201901103.pdf")
            pathOperaciones = ".\Proyecto1\RESULTADOS_201901103.pdf"
            webbrowser.open_new(pathOperaciones)
        except Exception as e:
            showerror(title="Error", message="Por favor corregir los errores\nluego guarde el archivo nuevamente")
            
    else:
        showwarning(title="Advertencia", message="Por favor cargue un archivo")

def errores(event = None):
    try:
        global almacenar
        if almacenar != "":
            textErores.configure(state=tk.NORMAL)
            escribiendoE = enviandoAnalisis.erroresValidados()
            textErores.insert("1.0", escribiendoE)
            textErores.configure(state="disabled")

            archivoErrores = open(".\Proyecto1\ERRORES_201901103.json","w")
            archivoErrores.write(escribiendoE)
            archivoErrores.close()

            enviandoAnalisis.limpiarDatos()
        else:
            showwarning(title="Advertencia", message="Por favor cargue un archivo")
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")
def inicializar():
    try:
        global almacenar
        almacenar = ""
        enviandoAnalisis.limpiarDatos()
        textLeer.delete("1.0","end")
        textErores.configure(state=tk.NORMAL)
        textErores.delete("1.0","end")
        textErores.configure(state="disabled")
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")
#\********************************************************************************************************************************
#Metodos y funciones para la seccion de Ayuda ************************************************************************************
def manualUsuario(event = None):
    try:
        pathUsuario = "Proyecto1\Documentacion\Manual Usuario.pdf"
        webbrowser.open_new(pathUsuario)
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")

def manualTecnico(event = None):
    try:
        pathTecnico = "Proyecto1\Documentacion\Manual Tecnico.pdf"
        webbrowser.open_new(pathTecnico)
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")
def temasAyuda(event = None):
    try:
        showinfo(title="Información del desarrollador", message="Josué Daniel Rojché García\nCarnet: 201901103\nLenguajes Formales y de Programación\nSección: A-")
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")
#\********************************************************************************************************************************
#Main
if __name__ == '__main__':
    try:
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
        menuArchivo.add_command(label="Inicializar", command= inicializar)
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
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")
    #https://recursospython.com/codigos-de-fuente/bloc-de-notas-simple-con-tkinter/
    #https://www.delftstack.com/es/howto/python-tkinter/how-to-get-the-input-from-tkinter-text-box/