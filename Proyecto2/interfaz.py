import os
import tkinter as tk
from tkinter import CENTER, INSERT, RIGHT, Y, Scrollbar, StringVar, filedialog, Tk, ttk
from tkinter.messagebox import showerror, showinfo, showwarning ,askquestion
import webbrowser

from argparse import ONE_OR_MORE

almacenar =""
urlAlmacenar = ""

def imprimir():
    print("Estoy Aquí")

# MENU ARCHIVO ***********************************************************************************
def nuevo():
    global urlAlmacenar
    try:
        if urlAlmacenar == "":
            inicializar()
            #textLeer.delete("1.0","end")
            #textLeer.insert("1.0", "---Area de edición de codigo.")
        else:
            res = askquestion(title="Advertencia", message="¿Está seguro que desea salir sin guardar?\nSi desea guardar presione No, de lo contrario presione Sí.")

            if res != "yes":
                guardarComo()
            else:
                inicializar()
                #textLeer.delete("1.0","end")
                #textLeer.insert("1.0", "---Area de edición de codigo.")
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")

def abrir(event = None):
    try:
        global urlAlmacenar
        urlArchivo = filedialog.askopenfilename(initialdir="./", title="Seleccione un Archivo", filetypes=(("Archivo Texto", "*.txt"), ("all files", "*.*")))
        if urlArchivo != "":

            leer = open(urlArchivo, "r", encoding='utf8')
            urlAlmacenar = urlArchivo
            global almacenar
            almacenar = leer.read()
            leer.close()

            #textLeer.configure(state=tk.NORMAL)
            textLeer.insert("1.0", almacenar)
            
        else :
            showwarning(title="Advertencia", message="No ingresó ningun archivo")
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error"+ str(e))

def guardar():
    try:
        global almacenar
        saveArchivo = open(urlAlmacenar, "w")
        saveArchivo.write(textLeer.get("1.0","end"))
        saveArchivo.close()
        
        almacenar = str(textLeer.get("1.0","end"))
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")

def guardarComo():
    try:
        guardar_Como = filedialog.asksaveasfilename(initialdir="./", title="Guardar Como", filetypes=(("Archivo texto", ".txt"), ("all files", "*.*")))
        if guardar_Como != "":
            saveComoArchivo = open(guardar_Como +".txt", "w") #+".json"
            saveComoArchivo.write(textLeer.get("1.0","end"))
            saveComoArchivo.close()
            
            showinfo(title="Guardado", message="Archivo guardado exitosamente")
        else :
            showwarning(title="Advertencia", message="¡Si no guarda el archivo se perderan los datos!")
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")

# MENU ANALISIS ***********************************************************************************
def generarSentenciasMDB():
    try:
        imprimir()
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")

# MENU TOKENS ***********************************************************************************
def verTokens():
    try:
        imprimir()
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")

# MENU ERRORES ***********************************************************************************
def verErrores():
    try:
        imprimir()
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")

# OTROS ***********************************************************************************
def inicializar():
    try:
        global almacenar
        almacenar = ""
        global urlAlmacenar
        urlAlmacenar = ""
        textLeer.delete("1.0","end")
        textLeer.insert("1.0", "---Area de edición de codigo.")
        #textLeer.configure(state="disabled")
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")

#Main

try:
    menu = tk.Tk()
    menu.title("PROYECTO NO.2")
    menu.geometry("800x650")
    menu.configure(bg="#212F3C")
    menu.resizable(False, False)
    #Crea la barra del menu
    barra_Menu = tk.Menu()
    #Crea el primer elemento el cual será para archivo y se enlaza ala barra
    menuArchivo = tk.Menu(barra_Menu, tearoff=False)
    #Al add_command se le puede pasar el parametro accelerator="Ctr+N" para agregar un atajo con el teclado
    menuArchivo.add_command(label="Abrir",accelerator="Ctrl+N",command= abrir)
    menu.bind_all("<Control-n>",abrir )
    menuArchivo.add_command(label="Nuevo", command= nuevo)
    menuArchivo.add_command(label="Guardar", command= guardar)
    menuArchivo.add_command(label="Guardar Como",command=guardarComo)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Inicializar", command=inicializar)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Salir", command=menu.quit,activebackground="Red")
    menuAnalisis= tk.Menu(barra_Menu, tearoff=False)
    menuAnalisis.add_command(label="Generar Sentencias MongoDB",command= generarSentenciasMDB)
    menuTokens = tk.Menu(barra_Menu, tearoff= False)
    menuTokens.add_command(label="Ver Tokens", command= verTokens)
    menuErrores = tk.Menu(barra_Menu, tearoff= False)
    menuErrores.add_command(label="Ver Errores", command= verErrores)
    # a la barra menú le agregamos el menuArchivo
    barra_Menu.add_cascade(menu= menuArchivo, label= "Archivo")
    barra_Menu.add_cascade(menu= menuAnalisis, label= "Análisis")
    barra_Menu.add_cascade(menu= menuTokens, label= "Tokens")
    barra_Menu.add_cascade(menu= menuErrores, label= "Errores")
    posX = StringVar()
    posY = StringVar()
    def posicionXY(event):
        global posX 
        global posY 
        xy = textLeer.index(INSERT)
        aux = xy.split('.')
        posX.set(aux[0])
        posY.set(aux[1])
        #print('Coordenada x:',posX, 'Coordenada y', posY)
        
    textLeer = tk.Text()
    textLeer.configure(bg="#C8C885")
    textLeer.place(x= 5, y =5, height= 600, width= 690)
    textLeer.insert("1.0", "---Area de edición de codigo.")
    textLeer.bind("<Button-1>", posicionXY)
    menu.config(menu=barra_Menu)
    anchoTotal = menu.winfo_screenwidth()
    altoTotal = menu.winfo_screenheight()
    posicionAncho = round(anchoTotal/2 - 700/2)
    posicionAlto = round(altoTotal/2 - 650/2)
    
    menu.geometry("800x650"+"+"+str(posicionAncho)+"+"+str(posicionAlto))
    
    label1 = tk.Label(menu, text="Archivo abierto", bg="#212F3C",fg="#FFFFFF",width= 20, font=("Arial", 13)).place(x= 250, y =615)
    tk.Label(menu, text="Linea:", bg="#212F3C", fg="#FFFFFF", font=("Arial", 10)).place(x= 710, y =10)
    tk.Label(menu, text="Columna:", bg="#212F3C", fg="#FFFFFF", font=("Arial", 10)).place(x= 710, y =80)
    tk.Label(menu, textvariable = posX, bg="#212F3C", fg="#FFFFFF",font=("Arial", 10)).place(x =750,y=40)
    tk.Label(menu, textvariable = posY, bg="#212F3C", fg="#FFFFFF",font=("Arial", 10)).place(x =750,y=100)
    
    
    menu.mainloop()
except Exception as e:
        showerror(title="Error", message="Ocurrió un error"+str(e))