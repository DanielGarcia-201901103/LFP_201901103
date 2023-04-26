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
        self.sentencias = ''

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
                elif caracter == '\t':
                    if tok  != '':
                        self.almacenarToken(tok,'funcion')
                    tok = ''
                    self.estadoAnterior = 'B'
                    self.estadoActual = 'E'
                    self.columna += 4
                    texto = texto[1:]
                    continue
                elif caracter == '\n':
                    if tok  != '':
                        self.almacenarToken(tok,'funcion')
                    tok = ''
                    self.estadoAnterior = 'B'
                    self.estadoActual = 'E'
                    self.fila += 1
                    self.columna = 0
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
                elif caracter == '\n':
                    if tok  != '':
                        self.almacenarToken(tok,'variable')
                    tok = ''
                    self.estadoAnterior = 'E'
                    self.estadoActual = 'E'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                elif caracter == '\t':
                    if tok  != '':
                        self.almacenarToken(tok,'variable')
                    tok = ''
                    self.estadoAnterior = 'E'
                    self.estadoActual = 'E'
                    self.columna += 4
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
                elif caracter == '\t':
                    self.estadoAnterior = 'H'
                    self.estadoActual = 'H'
                    self.columna += 4
                    texto = texto[1:]
                    continue
                elif caracter == '\n':
                    self.estadoAnterior = 'H'
                    self.estadoActual = 'H'
                    self.fila += 1
                    self.columna = 0
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
                elif caracter == ' ':
                    if tok  != '':
                        self.almacenarToken(tok,'valor')
                    tok = ''
                    self.estadoAnterior = 'M'
                    self.estadoActual = 'M'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                elif caracter == '\n':
                    if tok  != '':
                        self.almacenarToken(tok,'valor')
                    tok = ''
                    self.estadoAnterior = 'M'
                    self.estadoActual = 'M'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                elif caracter == '\t':
                    if tok  != '':
                        self.almacenarToken(tok,'valor')
                    tok = ''
                    self.estadoAnterior = 'M'
                    self.estadoActual = 'M'
                    
                    self.columna += 4
                    texto = texto[1:]
                    continue
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
                elif caracter == '\t':
                    if tok  != '':
                        self.almacenarToken(tok,'identificador')
                    tok = ''
                    self.estadoAnterior = 'N'
                    self.estadoActual = 'N'
                    
                    self.columna += 4
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
                elif caracter == '\t':
                    if tok  != '':
                        self.almacenarToken(tok,'valor')
                    tok = ''
                    self.estadoAnterior = 'Ñ'
                    self.estadoActual = 'Ñ'
                    
                    self.columna += 4
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
                elif caracter == '\t':
                    if tok  != '':
                        self.almacenarToken(tok,'valor')
                    tok = ''
                    self.estadoAnterior = 'O'
                    self.estadoActual = 'O'
                    
                    self.columna += 4
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
                elif caracter == '\t':
                    if tok  != '':
                        self.almacenarToken(tok,'valor')
                    tok = ''
                    self.estadoAnterior = 'P'
                    self.estadoActual = 'P'
                    
                    self.columna += 4
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
                elif caracter == '\t':
                    if tok  != '':
                        self.almacenarToken(tok,'json')
                    tok = ''
                    self.estadoAnterior = 'Q'
                    self.estadoActual = 'Q'
                    self.columna += 4
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
        it = 0
        while it < len(self.tabla):
            if estadoAct == 'S':
                if self.tabla[it].lexema in self.reservadasFunciones:
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'funcion')
                    estadoAnt = 'S'
                    estadoAct = 'A'
                elif self.tabla[it].lexema == '/':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'comentario')
                    estadoAnt = 'A'
                    estadoAct = 'M'
                elif self.tabla[it].lexema == '-':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'comentario')
                    estadoAnt = 'A'
                    estadoAct = 'P'
                elif self.tabla[it].lexema == '\n' or self.tabla[it].lexema == ' ':
                    estadoAnt = 'S'
                    estadoAct = 'S'
                else:
                    self.almacenarErrorSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'invalido')
            elif estadoAct == 'A':
                if self.tabla[it].lexema != '':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'variable')
                    estadoAnt = 'A'
                    estadoAct = 'B'
                elif self.tabla[it].lexema == '\n' or self.tabla[it].lexema == ' ':
                    estadoAnt = 'A'
                    estadoAct = 'A'
                else:
                    self.almacenarErrorSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'invalido')
            elif estadoAct == 'B':
                if self.tabla[it].lexema == '=':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'igual')
                    estadoAnt = 'B'
                    estadoAct = 'C'
                elif self.tabla[it].lexema == '\n' or self.tabla[it].lexema == ' ':
                    estadoAnt = 'B'
                    estadoAct = 'B'
                else:
                    self.almacenarErrorSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'invalido')
            elif estadoAct == 'C':
                if self.tabla[it].lexema.lower() == 'nueva':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'reservada')
                    estadoAnt = 'C'
                    estadoAct = 'D'
                elif self.tabla[it].lexema == '\n' or self.tabla[it].lexema == ' ':
                    estadoAnt = 'C'
                    estadoAct = 'C'
                else:
                    self.almacenarErrorSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'invalido')
            elif estadoAct == 'D':
                if self.tabla[it].lexema in self.reservadasFunciones:
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'funcion')
                    estadoAnt = 'D'
                    estadoAct = 'E'
                elif self.tabla[it].lexema == '\n' or self.tabla[it].lexema == ' ':
                    estadoAnt = 'D'
                    estadoAct = 'D'
                else:
                    self.almacenarErrorSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'invalido')
            elif estadoAct == 'E':
                if self.tabla[it].lexema == '(':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'parentesis')
                    estadoAnt = 'E'
                    estadoAct = 'F'
                elif self.tabla[it].lexema == '\n' or self.tabla[it].lexema == ' ':
                    estadoAnt = 'E'
                    estadoAct = 'E'
                else:
                    self.almacenarErrorSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'invalido')
            elif estadoAct == 'F':
                if self.tabla[it].lexema == ')':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'parentesis')
                    estadoAnt = 'F'
                    estadoAct = 'W'
                elif self.tabla[it].lexema == '“':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'comilla')
                    estadoAnt = 'F'
                    estadoAct = 'H'  
                elif self.tabla[it].lexema == '”':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'comilla')
                    estadoAnt = 'F'
                    estadoAct = 'F'  
                elif self.tabla[it].lexema == ',':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'coma')
                    estadoAnt = 'F'
                    estadoAct = 'F' 
                elif self.tabla[it].lexema == '\n' or self.tabla[it].lexema == ' ':
                    estadoAnt = 'F'
                    estadoAct = 'F'
                else:
                    self.almacenarErrorSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'invalido')
            elif estadoAct == 'H':
                if self.tabla[it].lexema == '”':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'comilla')
                    estadoAnt = 'H'
                    estadoAct = 'F'
                elif self.tabla[it].lexema != '”':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'json')
                    estadoAnt = 'H'
                    estadoAct = 'H'
                elif self.tabla[it].lexema == '\n' or self.tabla[it].lexema == ' ':
                    estadoAnt = 'H'
                    estadoAct = 'H'
                else:
                    self.almacenarErrorSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'comilla o json invalido')
            elif estadoAct == 'W':
                if self.tabla[it].lexema == ';':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'punto y coma')
                    estadoAnt = 'W'
                    estadoAct = 'S'
                elif self.tabla[it].lexema == '\n' or self.tabla[it].lexema == ' ':
                    estadoAnt = 'W'
                    estadoAct = 'W'
                else:
                    self.almacenarErrorSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'invalido')
            elif estadoAct == 'M':
                if self.tabla[it].lexema == '*':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'asterisco')
                    estadoAnt = 'M'
                    estadoAct = 'N'
                elif self.tabla[it].lexema == '\n' or self.tabla[it].lexema == ' ':
                    estadoAnt = 'M'
                    estadoAct = 'M'
                else:
                    self.almacenarErrorSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'* invalido')
            elif estadoAct == 'N':
                if self.tabla[it].lexema != '':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'comentario')
                    estadoAnt = 'N'
                    estadoAct = 'N'
                elif self.tabla[it].lexema == '*':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'asterisco')
                    estadoAnt = 'N'
                    estadoAct = 'U'
                elif self.tabla[it].lexema == '\n' or self.tabla[it].lexema == ' ':
                    estadoAnt = 'N'
                    estadoAct = 'N'
                else:
                    self.almacenarErrorSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'* ó caracter invalido')
            elif estadoAct == 'U':
                if self.tabla[it].lexema == '/':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'barra /')
                    estadoAnt = 'U'
                    estadoAct = 'S'
                elif self.tabla[it].lexema == '\n' or self.tabla[it].lexema == ' ':
                    estadoAnt = 'U'
                    estadoAct = 'U'
                else:
                    self.almacenarErrorSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'/ invalido')
            elif estadoAct == 'P':
                if self.tabla[it].lexema == '-':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'guion -')
                    estadoAnt = 'P'
                    estadoAct = 'P'
                elif self.tabla[it].lexema != '':
                    self.almacenarSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'caracter')
                    estadoAnt = 'P'
                    estadoAct = 'A'
                elif self.tabla[it].lexema == '\n' or self.tabla[it].lexema == ' ':
                    estadoAnt = 'P'
                    estadoAct = 'P'
                else:
                    self.almacenarErrorSintactico(self.tabla[it].fila, self.tabla[it].columna, self.tabla[it].lexema,'- ó caracter invalido')
            it +=1
        
    def escribiendoArchivo(self):
        estadoAct = 'S'
        estadoAnt = ''
        self.sentencias = ''
        compararFuncion = ''
        nameColeccion = ''
        archivoJson = ''
        it = 0
        while it < len(self.tablaSintactico):
            if estadoAct == 'S':
                if self.tablaSintactico[it].lexema in self.reservadasFunciones:
                    compararFuncion = self.tablaSintactico[it].lexema
                    estadoAnt = 'S'
                    estadoAct = 'A'
            elif estadoAct == 'A':
                if self.tablaSintactico[it].lexema != '':
                    estadoAnt = 'A'
                    estadoAct = 'B'
                elif self.tablaSintactico[it].lexema == '\n' or self.tablaSintactico[it].lexema == ' ':
                    estadoAnt = 'A'
                    estadoAct = 'A'
            elif estadoAct == 'B':
                if self.tablaSintactico[it].lexema == '=':
                    estadoAnt = 'B'
                    estadoAct = 'C'
                elif self.tablaSintactico[it].lexema == '\n' or self.tablaSintactico[it].lexema == ' ':
                    estadoAnt = 'B'
                    estadoAct = 'B'
            elif estadoAct == 'C':
                if self.tablaSintactico[it].lexema.lower() == 'nueva':
                    estadoAnt = 'C'
                    estadoAct = 'D'
                elif self.tablaSintactico[it].lexema == '\n' or self.tablaSintactico[it].lexema == ' ':
                    estadoAnt = 'C'
                    estadoAct = 'C'
            elif estadoAct == 'D':
                if self.tablaSintactico[it].lexema in self.reservadasFunciones:
                    compararFuncion = self.tablaSintactico[it].lexema
                    estadoAnt = 'D'
                    estadoAct = 'E'
                elif self.tablaSintactico[it].lexema == '\n' or self.tablaSintactico[it].lexema == ' ':
                    estadoAnt = 'D'
                    estadoAct = 'D'
            elif estadoAct == 'E':
                if self.tablaSintactico[it].lexema == '(':
                    estadoAnt = 'E'
                    estadoAct = 'F'
                elif self.tablaSintactico[it].lexema == '\n' or self.tablaSintactico[it].lexema == ' ':
                    estadoAnt = 'E'
                    estadoAct = 'E'
            elif estadoAct == 'F':
                if self.tablaSintactico[it].lexema == ')':
                    estadoAnt = 'F'
                    estadoAct = 'W'
                elif self.tablaSintactico[it].lexema == '“':
                    estadoAnt = 'F'
                    estadoAct = 'H'  
                elif self.tablaSintactico[it].lexema == '”':
                    #self.sentencias += '’'
                    estadoAnt = 'F'
                    estadoAct = 'F'  
                elif self.tablaSintactico[it].lexema == ',':
                    estadoAnt = 'F'
                    estadoAct = 'I' 
                elif self.tablaSintactico[it].lexema == '\n' or self.tablaSintactico[it].lexema == ' ':
                    estadoAnt = 'F'
                    estadoAct = 'F'
            elif estadoAct == 'H':
                if self.tablaSintactico[it].lexema == '”':
                    #self.sentencias += '’'
                    estadoAnt = 'H'
                    estadoAct = 'F'
                elif self.tablaSintactico[it].lexema != '”':
                    nameColeccion = str(self.tablaSintactico[it].lexema)
                    estadoAnt = 'H'
                    estadoAct = 'H'
                elif self.tablaSintactico[it].lexema == '\n' or self.tablaSintactico[it].lexema == ' ':
                    estadoAnt = 'H'
                    estadoAct = 'H'
            elif estadoAct == 'I':
                if self.tablaSintactico[it].lexema == ')':
                    estadoAnt = 'I'
                    estadoAct = 'W'
                elif self.tablaSintactico[it].lexema == '“':
                    estadoAnt = 'I'
                    estadoAct = 'J'  
                elif self.tablaSintactico[it].lexema == '”':
                    #self.sentencias += '’'
                    estadoAnt = 'I'
                    estadoAct = 'I'
                elif self.tablaSintactico[it].lexema == '\n' or self.tablaSintactico[it].lexema == ' ':
                    estadoAnt = 'I'
                    estadoAct = 'I'  
            elif estadoAct == 'J':
                if self.tablaSintactico[it].lexema == '”':
                    #self.sentencias += '’'
                    estadoAnt = 'J'
                    estadoAct = 'I'
                elif self.tablaSintactico[it].lexema != '”':
                    archivoJson += str(self.tablaSintactico[it].lexema)
                    estadoAnt = 'J'
                    estadoAct = 'J'
                elif self.tablaSintactico[it].lexema == '\n' or self.tablaSintactico[it].lexema == ' ':
                    estadoAnt = 'J'
                    estadoAct = 'J'


            elif estadoAct == 'W':
                if self.tablaSintactico[it].lexema == ';':
                    estadoAnt = 'W'
                    estadoAct = 'S'
                    if compararFuncion.strip() == 'CrearBD':
                        self.sentencias += 'use(‘nombreBaseDatos’);'
                    elif compararFuncion.strip() == 'EliminarBD':
                        self.sentencias += 'db.dropDatabase();'
                    elif compararFuncion.strip() == 'CrearColeccion':
                        self.sentencias += 'db.createCollection(‘'+nameColeccion+'’);'
                    elif compararFuncion.strip() == 'EliminarColeccion':
                        self.sentencias += 'db.'+ nameColeccion+ '.drop();'
                    elif compararFuncion.strip() == 'InsertarUnico':
                        self.sentencias += 'db.'+ nameColeccion+ '.insertOne(“'+archivoJson+'”);'
                    elif compararFuncion.strip() == 'ActualizarUnico':
                        self.sentencias += 'db.'+ nameColeccion+ '.updateOne(“'+archivoJson+'”);'
                    elif compararFuncion.strip() == 'EliminarUnico':
                        self.sentencias += 'db.'+ nameColeccion+ '.deleteOne(“'+archivoJson+'”);'
                    elif compararFuncion.strip() == 'BuscarTodo':
                        self.sentencias += 'db.'+ nameColeccion+ '.find();'
                    elif compararFuncion.strip() == 'BuscarUnico':
                        self.sentencias += 'db.'+ nameColeccion+ '.findOne();'
                    self.sentencias += '\n\n'
                    archivoJson = ''
                    nameColeccion = ''
            
            it +=1
        print(self.sentencias)

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

    def imprimir_tokensSintacticosC(self):
        print('-'*31)
        print("| {:<12} | {:<4} | {:<7} | {:<20} |".format('Correlativo','Fila', 'Columna', 'Lexema'))
        print('-'*31)
        correlativo = 1
        for token in self.tablaSintacticoComentario:
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
    