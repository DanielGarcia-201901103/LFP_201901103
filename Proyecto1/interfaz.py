import sys
import tkinter as tk
from tkinter import CENTER, RIGHT, Y, Scrollbar, filedialog, Tk, ttk
from tkinter.messagebox import showerror, showinfo, showwarning
import webbrowser
from automataAFD import AFD 

datos =""
#Metodos y Funciones para la sección de Archivo *********************************************************************************
def abrir():
    urlArchivo = filedialog.askopenfilename(initialdir="./", title="Seleccione un Archivo", filetypes=(("Archivo json", "*.json"), ("all files", "*.*")))
    if urlArchivo != "":
        leer = open(urlArchivo, "rt")
        global datos
        datos = leer.read()
        leer.close()
        showinfo(title="Abierto", message="Archivo leído exitosamente")
    else :
        #showerror(title="Error", message="El tamaño maximo de organismos es: 1000 \nPorfavor ingrese menos organismos")
        showwarning(title="Advertencia", message="No ingresó ningun archivo")

def guardar():
    pass

def guardarComo():
    guardar_Como = filedialog.asksaveasfilename(initialdir="./", title="Guardar Como", filetypes=(("Archivo json", "*.json"), ("all files", "*.*")))
    if guardar_Como != "":
        showinfo(title="Guardado", message="Archivo guardado exitosamente")
    else :
        showwarning(title="Advertencia", message="¡Si no guarda el archivo se perderan los datos!")

def analizar():
    global datos
    enviandoAnalisis = AFD()
    enviandoAnalisis.analizando(datos)
    enviandoAnalisis.imprimir_tokens()
def errores():
    pass
#\********************************************************************************************************************************
#Metodos y funciones para la seccion de Ayuda ************************************************************************************
def manualUsuario():
    pathUsuario = "Proyecto1\Documentacion\Manual Usuario.pdf"
    webbrowser.open_new(pathUsuario)

def manualTecnico():
    pathTecnico = "Proyecto1\Documentacion\Manual Tecnico.pdf"
    webbrowser.open_new(pathTecnico)

def temasAyuda():
    showinfo(title="Información del desarrollador", message="Josué Daniel Rojché García\nCarnet: 201901103")
#\********************************************************************************************************************************
#Main
if __name__ == '__main__':
    menu = tk.Tk()
    menu.title("PROYECTO NO.1")
    menu.geometry("607x400")
    menu.configure(bg="#212F3C")
    menu.resizable(False, False)

    tk.Label(menu, text="Archivo", bg="#000000", fg="#FFFFFF",width= 33, font=("Arial", 13)).grid(row=0,column=0)
    tk.Label(menu, text="Ayuda", bg="#000000", fg="#FFFFFF",width= 33, font=("Arial", 13)).grid(row=0,column=1)

    tk.Button(menu, text="Abrir", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: abrir()).place(x=70, y=60)
    tk.Button(menu, text="Guardar", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: guardar()).place(x=70, y=105)
    tk.Button(menu, text="Guardar Como", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: guardarComo()).place(x=70, y=150)
    tk.Button(menu, text="Analizar", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: analizar()).place(x=70, y=195)
    tk.Button(menu, text="Errores", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: errores()).place(x=70, y=240)
    tk.Button(menu, text="Salir", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command= menu.quit).place(x=70, y=285)
    
    tk.Button(menu, text="Manual de Usuario", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: manualUsuario()).place(x=370, y=60)
    tk.Button(menu, text="Manual Técnico", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: manualTecnico()).place(x=370, y=105)
    tk.Button(menu, text="Temas de Ayuda", width=20, anchor="c", bg="#895C09", fg="Black", font=("Arial Black", 10), command=lambda: temasAyuda()).place(x=370, y=150)

    menu.mainloop() # Permite mostrar la ventana 