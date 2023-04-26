import os
import tkinter as tk
from tkinter import CENTER, INSERT, RIGHT, Y, Scrollbar, StringVar, filedialog, Tk, ttk
from tkinter.messagebox import showerror, showinfo, showwarning ,askquestion
import webbrowser
from automataFD import AFD 
from argparse import ONE_OR_MORE

almacenar =""
urlAlmacenar = ""
analisisLexico= AFD()

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
            textLeer.delete("1.0","end")
            textLeer.insert("1.0", almacenar)
            
        else :
            showwarning(title="Advertencia", message="No ingresó ningun archivo")
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error"+ str(e))

def guardar():
    try:
        global almacenar
        saveArchivo = open(urlAlmacenar, "w", encoding='utf8')
        saveArchivo.write(textLeer.get("1.0","end"))
        saveArchivo.close()
        
        almacenar = str(textLeer.get("1.0","end"))
        analisisLexico.limpiarDatos()
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")

def guardarComo():
    try:
        guardar_Como = filedialog.asksaveasfilename(initialdir="./", title="Guardar Como", filetypes=(("Archivo texto", ".txt"), ("all files", "*.*")))
        if guardar_Como != "":
            saveComoArchivo = open(guardar_Como +".txt", "w", encoding='utf8') 
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
        analisisLexico.analizando(almacenar)
        analisisLexico.analizadorSintactico()
        analisisLexico.imprimir_tokensSintacticos()
        analisisLexico.imprimir_ErroresSintacticos()

        analisisLexico.escribiendoArchivo()
        #validar si existen errores en la tabla de errores de token y de sintactico
        #Si no existen errores generar las sentencias mongoDB
    except Exception as e:
            showerror(title="Error", message="Ocurrió un error")

# MENU TOKENS ***********************************************************************************
def verTokens():
    try:
        auxiliarTablaTokens = analisisLexico.obtenerTablaTokens()

        ventana_Token = tk.Toplevel()
        ventana_Token.title("Tabla TOKENS")
        ventana_Token.geometry("650x600")
        ventana_Token.configure(bg="yellow")
        ventana_Token.resizable(False, False)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="silver", foreground="black", rowheight=30, fieldbackground="silver")
        style.map("Treeview", background=[("selected", "green")])

        scroll_bar = Scrollbar(ventana_Token)
        scroll_bar.pack(side=RIGHT, fill=Y)

        tablaDinamica = ttk.Treeview(ventana_Token, yscrollcommand=scroll_bar.set, columns=("col1", "col2"),height= 500)
        scroll_bar.config(command=tablaDinamica.yview)
        tablaDinamica.column("#0", width=80)
        tablaDinamica.column("col1", width=200, anchor=CENTER)
        tablaDinamica.column("col2", width=300, anchor=CENTER)

        tablaDinamica.heading("#0", text="Correlativo", anchor=CENTER)
        tablaDinamica.heading("col1", text="Token", anchor=CENTER)
        tablaDinamica.heading("col2", text="Lexema", anchor=CENTER)
    # agregando estilo a las filas
        tablaDinamica.tag_configure("oddrow", background="white")
        tablaDinamica.tag_configure("evenrow", background="lightblue")
    # AGREGANDO LISTA DE OBJETOS A LA TABLA DE ACUERDO AL TAMAÑO DE LA LISTA.
        iterador = 1

        for j in auxiliarTablaTokens:
            t_t = j.tok
            t_lexema = j.lexema

            # MEJOR SE VA A MANEJAR CON WHILE PARA RECORRER LA LISTA OBJETOS.
            if iterador % 2 == 0:
                tablaDinamica.insert("", tk.END, text=str(iterador), values=(t_t,t_lexema), tags=("evenrow",))
            else:
                tablaDinamica.insert("", tk.END, text=str(iterador), values=(t_t,t_lexema), tags=("oddrow",))

            iterador += 1
        tablaDinamica.pack(pady=20)

        ventana_Token.mainloop()

    except Exception as e:
            showerror(title="Error", message="Ocurrió un error"+ str(e))

# MENU ERRORES ***********************************************************************************
def verErrores():
    try:
        auxiliarTablaErrores = analisisLexico.obtenerTablaErrores()
        ventana_Errores = tk.Toplevel()
        ventana_Errores.title("Tabla TOKENS")
        ventana_Errores.geometry("900x600")
        ventana_Errores.configure(bg="yellow")
        ventana_Errores.resizable(False, False)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="silver", foreground="black", rowheight=30, fieldbackground="silver")
        style.map("Treeview", background=[("selected", "green")])

        scroll_bar = Scrollbar(ventana_Errores)
        scroll_bar.pack(side=RIGHT, fill=Y)

        tablaDinamica = ttk.Treeview(ventana_Errores, yscrollcommand=scroll_bar.set, columns=("col1", "col2", "col3", "col4"),height= 500)
        scroll_bar.config(command=tablaDinamica.yview)
        tablaDinamica.column("#0", width=80)
        tablaDinamica.column("col1", width=80, anchor=CENTER)
        tablaDinamica.column("col2", width=80, anchor=CENTER)
        tablaDinamica.column("col3", width=300, anchor=CENTER)
        tablaDinamica.column("col4", width=300, anchor=CENTER)

        tablaDinamica.heading("#0", text="Tipo de Error", anchor=CENTER)
        tablaDinamica.heading("col1", text="Fila", anchor=CENTER)
        tablaDinamica.heading("col2", text="Columna", anchor=CENTER)
        tablaDinamica.heading("col3", text="Lexema o Token", anchor=CENTER)
        tablaDinamica.heading("col4", text="Descripción", anchor=CENTER)
    # agregando estilo a las filas
        tablaDinamica.tag_configure("oddrow", background="white")
        tablaDinamica.tag_configure("evenrow", background="lightblue")
    # AGREGANDO LISTA DE OBJETOS A LA TABLA DE ACUERDO AL TAMAÑO DE LA LISTA.
        iterador = 1

        for j in auxiliarTablaErrores:
            t_fila = j.fila
            t_columna = j.columna
            t_lexema = j.lexema
            t_des = j.tok

            # MEJOR SE VA A MANEJAR CON WHILE PARA RECORRER LA LISTA OBJETOS.
            if iterador % 2 == 0:
                tablaDinamica.insert("", tk.END, text='Lexico', values=(t_fila, t_columna, t_lexema, t_des), tags=("evenrow",))
            else:
                tablaDinamica.insert("", tk.END, text='Lexico', values=(t_fila, t_columna, t_lexema, t_des), tags=("oddrow",))

            iterador += 1

        #Agregar la lectura de errores sintacticos con otro for


        tablaDinamica.pack(pady=20)

        ventana_Errores.mainloop()
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


#https://www.youtube.com/watch?v=wfogZfIS03U
#https://www.youtube.com/watch?v=s3pC93LgP18
#https://github.com/falconmasters/expresiones-regulares/blob/master/Expresiones_Regulares.txt


# EXPRESION REGULAR PARA COMENTARIO DE UNA LINEA    (---)(.+)*

# EXPRESION REGULAR PARA COMENTARIO VARIAS LINEAS (\/\*(\s*|.*?)*\*\/)|(\/\/.*)
# realizada  nuevamente                            \/\*(.+\n.+|.)*\*\/
# ultima verificacion                              \/\*(.*\n.+|.)*|\n\s\*\/

# encontrando todos los comentarios, los multilineas y lineas (\/\*(.*\n.+|.)*|\n\s\*\/)|(---)(.+)*

# EXPRESION PARA FUNCIONES EN UNA LINEA Y SIN PARAMETROS (\w+)\s(\w+)\s=\s(nueva)\s(\w+)\(\);
# EXPRESION PARA FUNCIONES EN UNA LINEA CON UN PARAMETRO O SIN PARAMETROS (\w+)\s(\w+)\s=\s(nueva)\s(\w+)\(("\w+")*\);

#Pruebas*************************** \"\w+\"\,\n\"\n(\{\n\s?\"\w+\"\s\:\s\"\w+\s\w+\"\n\})|\,(\{\n\s?\"\w+\"\s\:\s\"\w+\s\w+\"\n\})*|(\{\n\s?(\$set)\:\s(\{\"\w+\"\s\:\s\"\w+\s\w+\"\})\n\s?\})*\n\s?\"\)\;

#(\w+\s+\w+\s+=\s+nueva\s+\w+\(.*\);)|(\/\*(.*\n.+|.)*|\n\s\*\/)|(---)(.+)*
#(\w+\s+\w+\s+=\s+nueva\s+\w+\(.*\);)|(\/\*(.*\n.+|.)*|\n\s\*\/)|(---)(.+)*
#(\w+\s+\w+\s+=\s+nueva\s+\w+\(.*\);)|(\/\*(.)*\*\/)|((---)(.+)*)