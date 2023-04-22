from token import Token

class AFD:
    def __init__(self):
        self.letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-','?','"','{','}','[',']','.',':',';','$']
        self.identificacion = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','_','A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.tipoFuncion = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.fila = 1
        self.columna = 0
        self.estadoActual = 'A'
        self.estadoAnterior = ''
        self.estadoFinal = ['L', 'J']
        self.tabla = []
        self.tablaErrores = []
        self.auxiliarTexto = ""
        self.iterar = 1

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
                if caracter in self.tipoFuncion:
                    tok += caracter
                    self.estadoAnterior = 'A'
                    self.estadoActual = 'B'
                elif caracter == '/':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'A'
                    self.estadoActual = 'C'
                elif caracter == '-':
                    self.almacenarToken(caracter)
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
                    self.almacenarError(caracter)
            # valida cuando hay comentarios de una Linea
            elif self.estadoActual == 'D':
                if caracter == '-':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'D'
                    self.estadoActual = 'G'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            elif self.estadoActual == 'G':
                if caracter == '-':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'G'
                    self.estadoActual = 'J'
                else:
                    validandoError = True
                    self.almacenarError(caracter) 
            elif self.estadoActual == 'J':
                if caracter.lower() in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'J'
                    self.estadoActual = 'J'
                elif caracter == ' ':
                    if tok != '':
                        self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'J'
                    self.estadoActual = 'J'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                elif caracter == '\n':
                    if tok  != '':
                        self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'J'
                    self.estadoActual = 'A'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                elif caracter == '\t':
                    if tok  != '':
                        self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'J'
                    self.estadoActual = 'J'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # valida cuando hay comentarios de varias lineas
            elif self.estadoActual == 'C':
                if caracter == '*':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'C'
                    self.estadoActual = 'F'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            elif self.estadoActual == 'F':
                if caracter.lower() in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'F'
                    self.estadoActual = 'F'
                elif caracter == '*':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'F'
                    self.estadoActual = 'I'
                elif caracter == ' ':
                    if tok != '':
                        self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'F'
                    self.estadoActual = 'F'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                elif caracter == '\n':
                    if tok  != '':
                        self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'F'
                    self.estadoActual = 'F'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                elif caracter == '\t':
                    if tok  != '':
                        self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'F'
                    self.estadoActual = 'F'
                    self.columna += 4
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            elif self.estadoActual == 'I':
                if caracter == '/':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'I'
                    self.estadoActual = 'L'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            elif self.estadoActual == 'L':
                if caracter == '\n':
                    if tok  != '':
                        self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'F'
                    self.estadoActual = 'A'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # valida cuando hay funciones
            elif self.estadoActual == 'B':
                if caracter in self.tipoFuncion:
                    tok += caracter
                    self.estadoAnterior = 'B'
                    self.estadoActual = 'B'
                elif caracter == ' ':
                    if tok  != '':
                        self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'B'
                    self.estadoActual = 'E'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            elif self.estadoActual == 'E':
                if caracter.lower() in self.identificacion:
                    tok += caracter
                    self.estadoAnterior = 'E'
                    self.estadoActual = 'E'
                elif caracter == '=':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'E'
                    self.estadoActual = 'H'
                elif caracter == ' ':
                    if tok  != '':
                        self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'E'
                    self.estadoActual = 'E'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            elif self.estadoActual == 'H':
                if caracter.lower() in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'H'
                    self.estadoActual = 'H'
                elif caracter == ' ':
                    if tok  != '':
                        self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'H'
                    self.estadoActual = 'K'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            elif self.estadoActual == 'K':
                if caracter in self.tipoFuncion:
                    tok += caracter
                    self.estadoAnterior = 'K'
                    self.estadoActual = 'K'
                elif caracter == ' ':
                    if tok  != '':
                        self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'K'
                    self.estadoActual = 'M'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            elif self.estadoActual == 'M':
                if caracter in self.tipoFuncion:
                    tok += caracter
                    self.estadoAnterior = 'M'
                    self.estadoActual = 'M'
                elif caracter == '(':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'E'
                    self.estadoActual = 'N'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            elif self.estadoActual == 'N':
                if caracter in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'N'
                    self.estadoActual = 'N'
                elif caracter == ')':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'N'
                    self.estadoActual = 'Ñ'
                elif caracter == ',':
                    self.almacenarToken(tok)
                    tok = ''
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'N'
                    self.estadoActual = 'N'
                elif caracter == ' ':
                    if tok  != '':
                        self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'N'
                    self.estadoActual = 'N'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                elif caracter == '\n':
                    if tok  != '':
                        self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'N'
                    self.estadoActual = 'N'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # ARREGLAR LOS ESTADOS DE LAS FUNCIONES YA QUE FALLA DESPUES DE LA PALABRA nueva 
            elif self.estadoActual == 'Ñ':
                if caracter == ';':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'Ñ'
                    self.estadoActual = 'L'
                else:
                    validandoError = True
                    self.almacenarError(caracter)

            self.columna += 1
            texto = texto[1:]
        return self.estadoActual in self.estadoFinal
    
    def almacenarToken(self, lexema):
        newToken = Token(self.fila, self.columna, lexema)
        self.tabla.append(newToken)

    def imprimir_tokens(self):
        print('-'*31)
        print("| {:<12} | {:<4} | {:<7} | {:<20} |".format('Correlativo','Fila', 'Columna', 'Lexema'))
        print('-'*31)
        correlativo = 1
        for token in self.tabla:
            print("| {:<12} | {:<4} | {:<7} | {:<20} |".format(str(correlativo),token.fila, token.columna, token.lexema))
            correlativo +=1
            
    def limpiarDatos(self):
        self.fila = 0
        self.columna = 0
        self.estadoActual = ''
        self.estadoAnterior = ''
        self.tabla = []
        self.tablaErrores = []
        self.auxiliarTexto = ""
        self.iterar = 1
        self.escribiendoGrafica = ""
        self.enlaceNodosSub = ""
        self.aleatorios = []
    
    def almacenarError(self, lexemaError):
        newToken1 = Token(self.fila, self.columna, lexemaError)
        self.tablaErrores.append(newToken1)