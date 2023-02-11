from pelicula import Pelicula
import msvcrt
objetoPelicula = []
# -------------------------------------------metodos del menu gestionar peliculas
def mostrarPeliculas():
    #Recorrer los listados 
    print("********** Lista Peliculas**********\n")
    print("No.  | Año     | Genero    --> Pelicula")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    no_numero = 1
    for j in objetoPelicula:
        print(str(no_numero) + "    | " + str(j.getYear())+"    | " + j.getGeneroPelicula()+"    --> " + j.getNombrePelicula())
        no_numero +=1    

def mostrarActores():
    print("********** Listado de las Peliculas**********\n")
    print("No.  | Pelicula")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    try:
        no_numero1 = 1
        for k in objetoPelicula:
            print(str(no_numero1)+"    | " + k.getNombrePelicula())
            no_numero1 +=1
        print("\nElija el numero de la pelicula de la cual quiere ver los actores:")
        elejirMostrar = int(input())
        #mostrando los actores
        print("Pelicula elegida: " + objetoPelicula[elejirMostrar-1].getNombrePelicula())
        print("\n********** Lista Actores**********")
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        for ob in objetoPelicula[elejirMostrar-1].actores:
            print("\t -"+ob.strip())
    except ValueError:
        print("\nPor favor ingrese un solo numeros")

'''    
def buscarPelicula(ingresadoN):
    #metodo de busqueda por pelicula
    inferior = 0
    superior = len(objetoPelicula) - 1
    medio = int((inferior+superior+1)/2)
    ubicacion = -1
    while ((inferior <=superior) and (ubicacion == -1)):
        if (objetoPelicula[ingresadoN].getNombrePelicula() == objetoPelicula[medio].getNombrePelicula()):
            ubicacion = medio
        elif(ingresadoN < objetoPelicula[medio]):
            superior = medio - 1
        else:
            inferior = medio + 1
        medio = int((inferior + superior + 1)/2)
    #para mejorar la busqueda agregar a objetos un iterador
    return ubicacion
'''

# -------------------------------------------metodos del menu filtrado
def filtradoActor():
    pass

def filtradoYear():
    pass

def filtradoGenero():
    pass

#   -------------------------------------------metodos del menu principal
def cargarArchivo():
    listaLinea = []
    try:
        print("\nIngrese la ruta del archivo:")
        ruta = str(input())
        leerArchivo = open(ruta, "r", encoding="utf8")
        if leerArchivo is None: # Valida si no se seleccionó un archivo
            print("No ha ingresado un archivo")
        else:
            texto = leerArchivo.readlines() # si el archivo existe lee todo el contenido del archivo
            for linea in texto:
                if linea.strip() == "":  # si una linea está vacia la omite
                    pass
                else: # guarda cada linea que no esté vacía
                    listaLinea.append(linea.strip("\n"))
            leerArchivo.close()
            print("\nArchivo leído correctamente")
    except IOError:
        print("\nPor favor ingrese una ruta de archivo valida")

    for i in listaLinea: #recorremos la lista de las lineas leídas en el archivo
        #separar los campos por los punto y comas
        textoTemporal = str(i)
        temp = textoTemporal.split(";")
        nombre_pelicula = str(temp[0])
        actores_pelicula = str(temp[1])
        year_pelicula = int(temp[2])
        genero_pelicula = str(temp[3])
        #separar los nombres de los actores en una lista de actores
        actoresLista = actores_pelicula.split(",")
        #enviar los datos al objeto
        peli = Pelicula(nombre_pelicula.strip(),actoresLista,year_pelicula,genero_pelicula.strip())
        objetoPelicula.append(peli)
        '''
        print(nombre_pelicula+"\n"+actores_pelicula+"\n"+str(year_pelicula)+"\n"+genero_pelicula)

        '''
    
    #Buscar los datos que se repiten y eliminarlos
    count = 0
    while count < len(objetoPelicula):
        numeroPosiciones = [] #lista que almacena las posiciones de los datos repetidos
        l = objetoPelicula[count]
        eliminarPeliculaRepetida = l.getNombrePelicula()
        iteratorEliminar =0
        for r in objetoPelicula:
            eliminarPeliculaRepetidaAuxiliar= r.getNombrePelicula()
            if eliminarPeliculaRepetida ==eliminarPeliculaRepetidaAuxiliar:
                numeroPosiciones.append(iteratorEliminar)
            else:
                pass
            iteratorEliminar +=1
        longiturIteraciones = len(numeroPosiciones)
        if longiturIteraciones >=2:
            count1 =0
            while count1 <= (longiturIteraciones-2):
                objetoPelicula.pop(int(numeroPosiciones[count1])-count1)
                count1 +=1
            count -=1
            print("\nLos datos repetidos fueron eliminados correctamente")
        else:
            pass
        count +=1
    
    '''Recorrer los listados 
    for j in objetoPelicula:
        print(j.getNombrePelicula()+ " "+j.actores[0] +" "+ str(j.getYear())+" " + j.getGeneroPelicula())    

    '''
    
def menuGestionar():
    try:
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
    except ValueError:
        print("\nPor favor ingrese un solo numeros")

def menuFiltrado():
    try:
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
    except ValueError:
        print("\nPor favor ingrese un solo numeros")

def graficar():
    pass
#   -------------------------------------------metodo main

if __name__ == '__main__':
    print("\n*********************************************")
    print("        Información del desarrollador")
    print("Lenguajes Formales y de Programación \n"+"Sección: A-\n" + "Carné: 201901103\n"+"Josué Daniel Rojché García")
    print("*********************************************\n")
    

    print("-----Presione una tecla para continuar-----")
    #presionar = str(input())
    msvcrt.getch()
    try:
        while True:
            print("\n------- Menu Principal --------")
            print("1. Cargar archivo de entrada"+"\n2. Gestionar peliculas"+"\n3. Filtrado"+"\n4. Gráfica"+"\n5. Salir")
            # recibe la opcion ingresada y la guarda como entero
            opcion = int(input("Ingrese el número de la opción: "))
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
                print("Gracias por utilizar el programa\n")
                break
            else:
                print("Ingrese una opcion correcta\n")
    except ValueError:
        print("\nPor favor ingrese un solo numeros")