

# -------------------------------------------metodos del menu gestionar peliculas
def mostrarPeliculas():
    pass

def mostrarActores():
    pass

# -------------------------------------------metodos del menu filtrado
def filtradoActor():
    pass

def filtradoYear():
    pass

def filtradoGenero():
    pass

#   -------------------------------------------metodos del menu principal
def cargarArchivo():
    pass

def menuGestionar():
    while True:
        print("\n------- Menu Gestionar Peliculas --------")
        print("1. Mostrar peliculas"+"\n2. Mostrar actores"+"\n3. Regresar")
        # recibe la opcion ingresada y la guarda como entero
        opcion1 = int(input("Ingrese una opcion: "))
        print()
        if opcion1 == 1:
            mostrarPeliculas()
        elif opcion1 == 2:
            mostrarActores()
        elif opcion1 == 3:
            break
        else:
            print("Ingrese una opcion correcta")

def menuFiltrado():
    while True:
        print("\n------- Menu Filtrado --------")
        print("1. Filtrado por actor"+"\n2. Filtrado por año"+"\n3. Filtrado por genero"+"\n4. Regresar")
        # recibe la opcion ingresada y la guarda como entero
        opcion2 = int(input("Ingrese una opcion: "))
        print()
        if opcion2 == 1:
            print("Filtrado por actor")
        elif opcion2 == 2:
            print("Filtrado por año")
        elif opcion2 == 3:
            print("Filtrado por genero")
        elif opcion2 == 4:
            break
        else:
            print("Ingrese una opcion correcta")

def graficar():
    pass
#   -------------------------------------------metodo main

if __name__ == '__main__':
    print("\n*********************************************")
    print("        Información del desarrollador")
    print("Lenguajes Formales y de Programación \n"+"Sección: A-\n" + "Carné: 201901103\n"+"Josué Daniel Rojché García")
    print("*********************************************\n")

    print("-----Escriba la letra 'c' y presione enter para continuar-----")
    presionar = str(input())
    if presionar == "c":

        while True:
            print("\n------- Menu Principal --------")
            print("1. Cargar archivo de entrada"+"\n2. Gestionar peliculas"+"\n3. Filtrado"+"\n4. Gráfica"+"\n5. Salir")
            # recibe la opcion ingresada y la guarda como entero
            opcion = int(input("Ingrese una opcion: "))
            print()
            if opcion == 1:
                cargarArchivo()
            elif opcion == 2:
                menuGestionar()
            elif opcion == 3:
                menuFiltrado()
            elif opcion == 4:
                graficar()
            elif opcion == 5:
                print("Gracias por utilizar el programa")
                break
            else:
                print("Ingrese una opcion correcta")
