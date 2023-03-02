import sys
import tkinter as tk
from tkinter import CENTER, RIGHT, Y, Scrollbar, filedialog, Tk, ttk
from tkinter.messagebox import showerror, showinfo, showwarning
import json

#para hacer json https://www.w3schools.com/python/python_json.asp
#Metodos y Funciones para la sección de Archivo *********************************************************************************
def abrir():
    pass
def guardar():
    pass
def guardarComo():
    pass 
def analizar():
    pass
def errores():
    pass
#\********************************************************************************************************************************
#Metodos y funciones para la seccion de Ayuda ************************************************************************************
def manualUsuario():
    pass

def manualTecnico():
    pass

def temasAyuda():
    pass
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