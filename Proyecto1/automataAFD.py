class Token:
    def __init__(self, row, columna, lexema):
        self.row = row
        self.columna = columna
        self.lexema = lexema

class AFD:
    def __init__(self):
        self.letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','-']
        self.numeros = ['0','1','2','3','4','5','6','7','8','9']
        self.fila = 0
        self.columna = 0
        self.estadoInicial = 'q0'
        self.estadoActual = ''
        self.estadoAnterior = ''
        self.estadoFinal = ['q10','q23']
        self.tabla = []
        self.auxiliarTexto = ""

    def analizando(self, texto):
        tok = ''
        #Eliminando espacios y saltos de linea de la cadena
        #texto = texto.replace("\n","")
        #texto = texto.replace(" ","")
        
        #recorriendo el texto
        while len(texto) > 0:
            caracter = texto[0]
            if caracter == '\n':
                self.fila += 1
                self.columna = 0
                texto = texto[1:]
                continue
            elif caracter == ' ':
                self.columna += 1
                texto = texto[1:]
                continue
            
            #validaciones de acuerdo al caracter que se está leyendo
            #valida cuando inicia leyendo el texto
            if self.estadoActual == '':
                if caracter == '{':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q0'
                    self.estadoActual = 'q1'
            #valida cuando se encuentra en el estado q1
            if self.estadoActual == 'q1':
                if caracter == '{':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q1'
                    self.estadoActual = 'q2'
                elif caracter == '"':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q1'
                    self.estadoActual = 'q3'
            #valida cuando se encuentra en q3 ***************************
            elif self.estadoActual == 'q3':
                if caracter.lower() in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'q3'
                    self.estadoActual = 'q4'
            #valida cuando se encuentra en q4
            elif self.estadoActual == 'q4':
                if caracter.lower() in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'q4'
                    self.estadoActual = 'q4'
                elif caracter == '"':
                    self.almacenarToken(tok)
                    tok = ''
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q4'
                    self.estadoActual = 'q5'
            elif self.estadoActual == 'q5':
                if caracter == ':':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q5'
                    self.estadoActual = 'q6'
            elif self.estadoActual == 'q6':
                if caracter == '"':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q6'
                    self.estadoActual = 'q7'
            elif self.estadoActual == 'q7':
                if caracter.lower() in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'q7'
                    self.estadoActual = 'q8'
            #valida cuando se encuentra en q8
            elif self.estadoActual == 'q8':
                if caracter.lower() in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'q8'
                    self.estadoActual = 'q8'
                elif caracter == '"':
                    self.almacenarToken(tok)
                    tok = ''
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q8'
                    self.estadoActual = 'q9'
            #valida cuando se encuentra en q9
            elif self.estadoActual == 'q9':
                if caracter == ',':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q9'
                    self.estadoActual = 'q1'
                elif caracter == '}': 
                    # estado de aceptación
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q9'
                    self.estadoActual = 'q10'
            # Aqui termina una parte  ***************************
            # Segunda parte
            #validar estado q2
            elif self.estadoActual == 'q2':
                if caracter == '"':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q2'
                    self.estadoActual = 'q11'
            #validacion estado q11
            elif self.estadoActual == 'q11':
                if caracter.lower() in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'q11'
                    self.estadoActual = 'q12'
            #validando estado q12
            elif self.estadoActual == 'q12':
                if caracter.lower() in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'q12'
                    self.estadoActual = 'q12'
                elif caracter == '"':
                    self.almacenarToken(tok)
                    tok = ''
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q12'
                    self.estadoActual = 'q13'
            #validando estado q13
            elif self.estadoActual == 'q13':
                if caracter == ':':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q13'
                    self.estadoActual = 'q14'
            #validando estado q14
            elif self.estadoActual == 'q14':
                if caracter in self.numeros:
                    tok += caracter
                    print(tok)
                    self.estadoAnterior = 'q14'
                    self.estadoActual = 'q18'
                elif caracter == '"':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q14'
                    self.estadoActual = 'q15'
                elif caracter == '[':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q14'
                    self.estadoActual = 'q2'
            #validando estado q15
            elif self.estadoActual == 'q15':
                if caracter.lower() in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'q15'
                    self.estadoActual = 'q16'
            #validando estado q16
            elif self.estadoActual == 'q16':
                if caracter.lower() in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'q16'
                    self.estadoActual = 'q16'
                elif caracter == '"':
                    self.almacenarToken(tok)
                    tok = ''
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q16'
                    self.estadoActual = 'q17'
            #validando estado q17
            elif self.estadoActual == 'q17':
                if caracter == ',':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q17'
                    self.estadoActual = 'q2'
            #validando estado q18
            elif self.estadoActual == 'q18':
                if caracter in self.numeros:
                    tok += caracter
                    print(tok)
                    self.estadoAnterior = 'q18'
                    self.estadoActual = 'q18'
                elif caracter == ',':
                    self.almacenarToken(tok)
                    tok = ''
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q18'
                    self.estadoActual = 'q2'
                elif caracter == '.':
                    tok += caracter
                    print(tok)
                    self.estadoAnterior = 'q18'
                    self.estadoActual = 'q19'
                elif caracter == ']':
                    self.almacenarToken(tok)
                    tok = ''
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q18'
                    self.estadoActual = 'q21'
                elif caracter == '}':
                    self.almacenarToken(tok)
                    tok = ''
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q18'
                    self.estadoActual = 'q22'
            #validando estado q19
            elif self.estadoActual == 'q19':
                if caracter in self.numeros:
                    tok += caracter
                    print(tok)
                    self.estadoAnterior = 'q19'
                    self.estadoActual = 'q20'
            #validando estado q20
            elif self.estadoActual == 'q20':
                if caracter in self.numeros:
                    tok += caracter
                    print(tok)
                    self.estadoAnterior = 'q20'
                    self.estadoActual = 'q20'
                elif caracter == ',':
                    self.almacenarToken(tok)
                    tok = ''
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q20'
                    self.estadoActual = 'q2'
                elif caracter == ']':
                    self.almacenarToken(tok)
                    tok = ''
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q20'
                    self.estadoActual = 'q21'
                # estado de aceptación para las operaciones
                elif caracter == '}':
                    self.almacenarToken(tok)
                    tok = ''
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q20'
                    self.estadoActual = 'q22'
            #validando estado q21
            elif self.estadoActual == 'q21':
                if caracter == '}':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q21'
                    self.estadoActual = 'q22'
                elif caracter == ',':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q21'
                    self.estadoActual = 'q2'
            #validando estado q22
            elif self.estadoActual == 'q22':
                if caracter == ',':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q22'
                    self.estadoActual = 'q1'
                    #estado de acpetación
                elif caracter == '}':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q22'
                    self.estadoActual = 'q23'
                '''
                AGREGAR q23 como estado de aceptación }, q22 no es un estado de aceptación
                (q22, }) = q23
                AGREGAR 
                (q21, ,) = q2
                Hay que modificar el automata
                '''
            self.columna +=1
            texto = texto[1:]
        return self.estadoActual in self.estadoFinal

    def almacenarToken(self, lexema):
        newToken = Token(self.fila, self.columna, lexema)
        self.tabla.append(newToken)                

    def imprimir_tokens(self):
        print('-'*31)
        print ("| {:<4} | {:<7} | {:<10} |".format('Fila','Columna','Lexema'))
        print('-'*31)
        for token in self.tabla:
            print ("| {:<4} | {:<7} | {:<10} |".format(token.row, token.columna, token.lexema))