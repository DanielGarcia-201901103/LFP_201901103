from token import Token

class AFD:
    def __init__(self):
        self.letrasComentarios = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-','{','}','[',']','.']
        self.identificacion = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','_']
        self.nueva = ['n','u','e','v']
        self.letrasJson = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-','{','}','"','.',',','$',':']
        self.tipoFuncion = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.reservadasFunciones =['CrearBD','EliminarBD','CrearColeccion','EliminarColeccion','InsertarUnico','ActualizarUnico','EliminarUnico','BuscarTodo','BuscarUnico']
        self.fila = 1
        self.columna = 0
        self.estadoActual = 'A'
        self.estadoAnterior = ''
        self.estadoFinal = ['L', 'J']
        self.tabla = []
        self.tablaErrores = []
        self.tablaSintactico = []
        self.tablaErroresSintacticos = []

    def analizando(self, texto1):
        tok = ''
        # Eliminando espacios y saltos de linea de la cadena
        validandoError = False
        texto = texto1
        # recorriendo el texto
        while len(texto) > 0:
            caracter = texto[0]
            '''
            if caracter == '\n':
                self.fila += 1
                self.columna = 0
                texto = texto[1:]
                continue
            elif caracter == ' ':
                self.columna += 1
                texto = texto[1:]
                continue
            '''
            # validaciones de acuerdo al caracter que se está leyendo
            if self.estadoActual == 'A':
                if caracter.lower() in self.tipoFuncion:
                    tok += caracter
                    self.estadoAnterior = 'A'
                    self.estadoActual = 'B'
                elif caracter == '/':
                    self.almacenarToken(caracter,"barra")
                    self.estadoAnterior = 'A'
                    self.estadoActual = 'C'
                elif caracter == '-':
                    self.almacenarToken(caracter,"guion")
                    self.estadoAnterior = 'A'
                    self.estadoActual = 'D'
                elif caracter == '\n':
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    self.estadoAnterior = 'A'
                    self.estadoActual = 'A'
                    continue
                elif caracter == ' ':
                    self.columna += 1
                    texto = texto[1:]
                    self.estadoAnterior = 'A'
                    self.estadoActual = 'A'
                    continue
                elif caracter == '\t':
                    self.columna += 4
                    texto = texto[1:]
                    self.estadoAnterior = 'A'
                    self.estadoActual = 'A'
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter,'invalido')
            # valida cuando hay comentarios de una Linea
            elif self.estadoActual == 'D':
                if caracter == '-':
                    self.almacenarToken(caracter,'guion')
                    self.estadoAnterior = 'D'
                    self.estadoActual = 'G'
                else:
                    validandoError = True
                    self.almacenarError(caracter,'invalido falta -')
            elif self.estadoActual == 'G':
                if caracter == '-':
                    self.almacenarToken(caracter,'guion')
                    self.estadoAnterior = 'G'
                    self.estadoActual = 'J'
                else:
                    validandoError = True
                    self.almacenarError(caracter,'invalido falta -') 
            elif self.estadoActual == 'J':
                if caracter.lower() in self.letrasComentarios:
                    tok += caracter
                    self.estadoAnterior = 'J'
                    self.estadoActual = 'J'
                elif caracter == ' ':
                    if tok != '':
                        self.almacenarToken(tok,'comentario')
                    tok = ''
                    self.estadoAnterior = 'J'
                    self.estadoActual = 'J'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                elif caracter == '\n':
                    if tok  != '':
                        self.almacenarToken(tok,'comentario')
                    tok = ''
                    self.estadoAnterior = 'J'
                    self.estadoActual = 'A'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                elif caracter == '\t':
                    if tok  != '':
                        self.almacenarToken(tok,'comentario')
                    tok = ''
                    self.estadoAnterior = 'J'
                    self.estadoActual = 'J'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter,'comentario invalido')
            # valida cuando hay comentarios de varias lineas
            elif self.estadoActual == 'C':
                if caracter == '*':
                    self.almacenarToken(caracter,'asterisco')
                    self.estadoAnterior = 'C'
                    self.estadoActual = 'F'
                else:
                    validandoError = True
                    self.almacenarError(caracter,'invalido falta *')
            elif self.estadoActual == 'F':
                if caracter.lower() in self.letrasComentarios:
                    tok += caracter
                    self.estadoAnterior = 'F'
                    self.estadoActual = 'F'
                elif caracter == '*':
                    self.almacenarToken(caracter,'asterisco')
                    self.estadoAnterior = 'F'
                    self.estadoActual = 'I'
                elif caracter == ' ':
                    if tok != '':
                        self.almacenarToken(tok,'comentario')
                    tok = ''
                    self.estadoAnterior = 'F'
                    self.estadoActual = 'F'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                elif caracter == '\n':
                    if tok  != '':
                        self.almacenarToken(tok,'comentario')
                    tok = ''
                    self.estadoAnterior = 'F'
                    self.estadoActual = 'F'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                elif caracter == '\t':
                    if tok  != '':
                        self.almacenarToken(tok, 'comentario')
                    tok = ''
                    self.estadoAnterior = 'F'
                    self.estadoActual = 'F'
                    self.columna += 4
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter,'caracter invalido ó falta *')
            elif self.estadoActual == 'I':
                if caracter == '/':
                    self.almacenarToken(caracter,'barra')
                    self.estadoAnterior = 'I'
                    self.estadoActual = 'L'
                else:
                    validandoError = True
                    self.almacenarError(caracter,'invalido falta /')
            elif self.estadoActual == 'L':
                if caracter == '\n':
                    if tok  != '':
                        self.almacenarToken(tok,'comentario')
                    tok = ''
                    self.estadoAnterior = 'L'
                    self.estadoActual = 'A'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter,'comentario invalido')
            # valida cuando hay funciones
            elif self.estadoActual == 'B':
                if caracter.lower() in self.tipoFuncion:
                    tok += caracter
                    self.estadoAnterior = 'B'
                    self.estadoActual = 'B'
                elif caracter == ' ':
                    if tok  != '':
                        self.almacenarToken(tok,'funcion')
                    tok = ''
                    self.estadoAnterior = 'B'
                    self.estadoActual = 'E'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter,'funcion invalida')
            elif self.estadoActual == 'E':
                if caracter.lower() in self.identificacion:
                    tok += caracter
                    self.estadoAnterior = 'E'
                    self.estadoActual = 'E'
                elif caracter == '=':
                    self.almacenarToken(caracter,'igual')
                    self.estadoAnterior = 'E'
                    self.estadoActual = 'H'
                elif caracter == ' ':
                    if tok  != '':
                        self.almacenarToken(tok,'variable')
                    tok = ''
                    self.estadoAnterior = 'E'
                    self.estadoActual = 'E'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter,'variable invalida ó falta =')
            elif self.estadoActual == 'H':
                if caracter.lower() in self.nueva:
                    tok += caracter
                    self.estadoAnterior = 'H'
                    self.estadoActual = 'H'
                elif caracter.lower() == 'a':
                    tok += caracter
                    self.almacenarToken(tok,'reservada')
                    tok = ''
                    self.estadoAnterior = 'H'
                    self.estadoActual = 'K'
                elif caracter == ' ':
                    self.estadoAnterior = 'H'
                    self.estadoActual = 'H'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter,'invalido reservada (nueva)')
            elif self.estadoActual == 'K':
                if caracter.lower() in self.tipoFuncion:
                    tok += caracter
                    self.estadoAnterior = 'K'
                    self.estadoActual = 'K'
                elif caracter == '(':
                    self.almacenarToken(tok,'funcion')
                    tok = ''
                    self.almacenarToken(caracter,'parentesis')
                    self.estadoAnterior = 'K'
                    self.estadoActual = 'M'
                elif caracter == ' ':
                    if tok  != '':
                        self.almacenarToken(tok,'funcion')
                    tok = ''
                    self.estadoAnterior = 'K'
                    self.estadoActual = 'K'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                elif caracter == '\n':
                    if tok  != '':
                        self.almacenarToken(tok,'funcion')
                    tok = ''
                    self.estadoAnterior = 'K'
                    self.estadoActual = 'K'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter,'funcion invalida o falta (')
            elif self.estadoActual == 'M':
                if caracter == ')':
                    self.almacenarToken(caracter,'parentesis')
                    self.estadoAnterior = 'M'
                    self.estadoActual = 'Ñ'
                elif caracter == '“':
                    self.almacenarToken(caracter,'comilla')
                    self.estadoAnterior = 'M'
                    self.estadoActual = 'N'
                else:
                    validandoError = True
                    self.almacenarError(caracter,'falta ) ó “')
            elif self.estadoActual == 'N':
                if caracter.lower() in self.identificacion:
                    tok += caracter
                    self.estadoAnterior = 'N'
                    self.estadoActual = 'N'
                elif caracter == '”':
                    self.almacenarToken(tok,'identificador')
                    tok = ''
                    self.almacenarToken(caracter,'comilla')
                    self.estadoAnterior = 'N'
                    self.estadoActual = 'O'
                elif caracter == ' ':
                    if tok  != '':
                        self.almacenarToken(tok,'identificador')
                    tok = ''
                    self.estadoAnterior = 'N'
                    self.estadoActual = 'N'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                elif caracter == '\n':
                    if tok  != '':
                        self.almacenarToken(tok,'identificador')
                    tok = ''
                    self.estadoAnterior = 'N'
                    self.estadoActual = 'N'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter,'falta ” ó identificador invalido')
            # ARREGLAR LOS ESTADOS DE LAS FUNCIONES YA QUE FALLA DESPUES DE LA PALABRA nueva 
            elif self.estadoActual == 'Ñ':
                if caracter == ';':
                    self.almacenarToken(caracter,'punto y coma')
                    self.estadoAnterior = 'Ñ'
                    self.estadoActual = 'L'
                elif caracter == ' ':
                    if tok  != '':
                        self.almacenarToken(tok,'valor')
                    tok = ''
                    self.estadoAnterior = 'Ñ'
                    self.estadoActual = 'Ñ'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                elif caracter == '\n':
                    if tok  != '':
                        self.almacenarToken(tok,'valor')
                    tok = ''
                    self.estadoAnterior = 'Ñ'
                    self.estadoActual = 'Ñ'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter,'falta ; ó caracter invalido')
            elif self.estadoActual == 'O':
                if caracter == ')':
                    self.almacenarToken(caracter,'parentesis')
                    self.estadoAnterior = 'O'
                    self.estadoActual = 'Ñ'
                elif caracter == ',':
                    self.almacenarToken(caracter,'coma')
                    self.estadoAnterior = 'O'
                    self.estadoActual = 'P'
                elif caracter == ' ':
                    if tok  != '':
                        self.almacenarToken(tok,'valor')
                    tok = ''
                    self.estadoAnterior = 'O'
                    self.estadoActual = 'O'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                elif caracter == '\n':
                    if tok  != '':
                        self.almacenarToken(tok,'valor')
                    tok = ''
                    self.estadoAnterior = 'O'
                    self.estadoActual = 'O'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter,'falta ) ó , ó caracter invalido')
            elif self.estadoActual == 'P':
                if caracter == '“':
                    self.almacenarToken(caracter,'comilla')
                    self.estadoAnterior = 'P'
                    self.estadoActual = 'Q'
                elif caracter == ' ':
                    if tok  != '':
                        self.almacenarToken(tok,'valor')
                    tok = ''
                    self.estadoAnterior = 'P'
                    self.estadoActual = 'P'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                elif caracter == '\n':
                    if tok  != '':
                        self.almacenarToken(tok,'valor')
                    tok = ''
                    self.estadoAnterior = 'P'
                    self.estadoActual = 'P'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter,'falta “ ó caracter invalido')
            elif self.estadoActual == 'Q':
                if caracter.lower() in self.letrasJson:
                    tok += caracter
                    self.estadoAnterior = 'Q'
                    self.estadoActual = 'Q'
                elif caracter == '”':
                    self.almacenarToken(tok,'json')
                    tok = ''
                    self.almacenarToken(caracter,'comilla')
                    self.estadoAnterior = 'Q'
                    self.estadoActual = 'O'
                elif caracter == ' ':
                    if tok  != '':
                        self.almacenarToken(tok,'json')
                    tok = ''
                    self.estadoAnterior = 'Q'
                    self.estadoActual = 'Q'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                elif caracter == '\n':
                    if tok  != '':
                        self.almacenarToken(tok,'json')
                    tok = ''
                    self.estadoAnterior = 'Q'
                    self.estadoActual = 'Q'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter,'falta ” ó caracter json invalido')
            
            self.columna += 1
            texto = texto[1:]
        return self.estadoActual in self.estadoFinal
    
    def analizadorSintactico(self):
        estadoAct = 'S'
        estadoAnt = ''
        for buscar in self.tabla:
            if estadoAct == 'S':
                if buscar.lexema in self.reservadasFunciones:
                    self.almacenarSintactico(buscar.fila, buscar.columna, buscar.lexema,'funcion')
                    estadoAnt = 'S'
                    estadoAct = 'A'
                else:
                    self.almacenarErrorSintactico(buscar.fila, buscar.columna, buscar.lexema,'invalido')
            elif estadoAct == 'A':
                if buscar.lexema != '':
                    self.almacenarSintactico(buscar.fila, buscar.columna, buscar.lexema,'variable')
                    estadoAnt = 'A'
                    estadoAct = 'B'
                else:
                    self.almacenarErrorSintactico(buscar.fila, buscar.columna, buscar.lexema,'invalido')
            elif estadoAct == 'B':
                if buscar.lexema == '=':
                    self.almacenarSintactico(buscar.fila, buscar.columna, buscar.lexema,'igual')
                    estadoAnt = 'B'
                    estadoAct = 'C'
                else:
                    self.almacenarErrorSintactico(buscar.fila, buscar.columna, buscar.lexema,'invalido')
            elif estadoAct == 'C':
                if buscar.lexema.lower() == 'nueva':
                    self.almacenarSintactico(buscar.fila, buscar.columna, buscar.lexema,'reservada')
                    estadoAnt = 'C'
                    estadoAct = 'D'
                else:
                    self.almacenarErrorSintactico(buscar.fila, buscar.columna, buscar.lexema,'invalido')
            elif estadoAct == 'D':
                if buscar.lexema in self.reservadasFunciones:
                    self.almacenarSintactico(buscar.fila, buscar.columna, buscar.lexema,'funcion')
                    estadoAnt = 'D'
                    estadoAct = 'E'
                else:
                    self.almacenarErrorSintactico(buscar.fila, buscar.columna, buscar.lexema,'invalido')
            elif estadoAct == 'E':
                if buscar.lexema == '(':
                    self.almacenarSintactico(buscar.fila, buscar.columna, buscar.lexema,'parentesis')
                    estadoAnt = 'E'
                    estadoAct = 'F'
                else:
                    self.almacenarErrorSintactico(buscar.fila, buscar.columna, buscar.lexema,'invalido')
            elif estadoAct == 'F':
                if buscar.lexema == ')':
                    self.almacenarSintactico(buscar.fila, buscar.columna, buscar.lexema,'parentesis')
                    estadoAnt = 'F'
                    estadoAct = 'W'
                elif buscar.lexema == '“':
                    self.almacenarSintactico(buscar.fila, buscar.columna, buscar.lexema,'comilla')
                    estadoAnt = 'F'
                    estadoAct = 'H'  
                elif buscar.lexema == '”':
                    self.almacenarSintactico(buscar.fila, buscar.columna, buscar.lexema,'comilla')
                    estadoAnt = 'F'
                    estadoAct = 'F'  
                elif buscar.lexema == ',':
                    self.almacenarSintactico(buscar.fila, buscar.columna, buscar.lexema,'coma')
                    estadoAnt = 'F'
                    estadoAct = 'F' 
                else:
                    self.almacenarErrorSintactico(buscar.fila, buscar.columna, buscar.lexema,'invalido')
            elif estadoAct == 'H':
                if buscar.lexema == '”':
                    self.almacenarSintactico(buscar.fila, buscar.columna, buscar.lexema,'comilla')
                    estadoAnt = 'H'
                    estadoAct = 'F'
                elif buscar.lexema != '”':
                    self.almacenarSintactico(buscar.fila, buscar.columna, buscar.lexema,'json')
                    estadoAnt = 'H'
                    estadoAct = 'H'
                else:
                    self.almacenarErrorSintactico(buscar.fila, buscar.columna, buscar.lexema,'invalido')
            elif estadoAct == 'W':
                if buscar.lexema == ';':
                    self.almacenarSintactico(buscar.fila, buscar.columna, buscar.lexema,'punto y coma')
                    estadoAnt = 'W'
                    estadoAct = 'S'
                else:
                    self.almacenarErrorSintactico(buscar.fila, buscar.columna, buscar.lexema,'invalido')
        
    def escribiendoArchivo(self):
        sentencias = ''
        it = 0
        while it < len(self.tablaSintactico):
            if self.tablaSintactico[it].lexema == 'CrearBD':
                sentencias += "use(‘nombreBaseDatos’);"
            if self.tablaSintactico[it].lexema== 'EliminarBD':
                sentencias += '\n'
                sentencias += 'db.dropDatabase();'
            if self.tablaSintactico[it].lexema == 'CrearColeccion':
                sentencias += '\n'
                sentencias += 'db.createCollection(‘nombreColeccion’);'
            it +=1

    #Metodos para almacenar Sintacticos
    def almacenarSintactico(self,fila, columna, dato, t):
        newSin = Token(fila, columna, dato, t)
        self.tablaSintactico.append(newSin)

    def almacenarErrorSintactico(self,fila, columna, dato, t):
        newESin = Token(fila, columna, dato, t)
        self.tablaErroresSintacticos.append(newESin)

    #Metodos para almacenar token lexicos
    def almacenarToken(self, lexema,t):
        newToken = Token(self.fila, self.columna, lexema,t)
        self.tabla.append(newToken)

    def almacenarError(self, lexemaError,t):
        newToken1 = Token(self.fila, self.columna, lexemaError,t)
        self.tablaErrores.append(newToken1)

    def obtenerTablaTokens(self):
        return self.tabla
    
    def obtenerTablaErrores(self):
        return self.tablaErrores
    
    #Metodos de impresion para sintactico
    def imprimir_tokensSintacticos(self):
        print('-'*31)
        print("| {:<12} | {:<4} | {:<7} | {:<20} |".format('Correlativo','Fila', 'Columna', 'Lexema'))
        print('-'*31)
        correlativo = 1
        for token in self.tablaSintactico:
            print("| {:<12} | {:<4} | {:<7} | {:<20} |".format(str(correlativo),token.fila, token.columna, token.lexema))
            correlativo +=1

    def imprimir_ErroresSintacticos(self):
        print('-'*31)
        print("| {:<12} | {:<4} | {:<7} | {:<20} |".format('Correlativo','Fila', 'Columna', 'Lexema'))
        print('-'*31)
        correlativo = 1
        for token in self.tablaErroresSintacticos:
            print("| {:<12} | {:<4} | {:<7} | {:<20} |".format(str(correlativo),token.fila, token.columna, token.lexema))
            correlativo +=1
    
    def limpiarDatos(self):
        self.fila = 1
        self.columna = 0
        self.estadoActual = 'A'
        self.estadoAnterior = ''
        self.tabla = []
        self.tablaErrores = []
        self.tablaSintactico = []
        self.tablaErroresSintacticos = []
    