from token import Token

class AFD:
    def __init__(self):
        self.letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-','?','"','{','}','[',']',',','.',':',';']
        self.tipoFuncion = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.fila = 0
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
                if caracter in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'J'
                    self.estadoActual = 'J'
                elif caracter == ' ':
                    self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'J'
                    self.estadoActual = 'J'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                elif caracter == '\n':
                    self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'J'
                    self.estadoActual = 'A'
                    self.fila += 1
                    self.columna = 0
                    texto = texto[1:]
                    continue
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # valida cuando hay comentarios de una Linea
            elif self.estadoActual == 'C':
                if caracter == '*':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'C'
                    self.estadoActual = 'F'
            elif self.estadoActual == 'F':
                if caracter in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'F'
                    self.estadoActual = 'F'
                elif caracter == '*':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'F'
                    self.estadoActual = 'I'
                elif caracter == ' ':
                    self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'F'
                    self.estadoActual = 'F'
                    self.columna += 1
                    texto = texto[1:]
                    continue
                elif caracter == '\n':
                    self.almacenarToken(tok)
                    tok = ''
                    self.estadoAnterior = 'F'
                    self.estadoActual = 'F'
                    self.fila += 1
                    self.columna = 0
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






            # valida cuando hay funciones
            elif self.estadoActual == 'B':
                if caracter in self.tipoFuncion:
                    tok += caracter
                    self.estadoAnterior = 'B'
                    self.estadoActual = 'B'
                elif caracter == '"':
                    self.almacenarToken(tok)
                    tok = ''
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q4'
                    self.estadoActual = 'q5'
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
        print("| {:<4} | {:<7} | {:<20} |".format('Fila', 'Columna', 'Lexema'))
        print('-'*31)
        for token in self.tabla:
            print("| {:<4} | {:<7} | {:<20} |".format(
                token.row, token.columna, token.lexema))
            
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