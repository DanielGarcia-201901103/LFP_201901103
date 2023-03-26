from token import Token
from operar import Operaciones

class AFD:
    def __init__(self):
        self.letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
        self.numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.fila = 0
        self.columna = 0
        self.estadoActual = ''
        self.estadoAnterior = ''
        self.estadoFinal = ['q10', 'q23']
        self.tabla = []
        self.tablaErrores = []
        self.auxiliarTexto = ""
        self.iterar = 1
        self.escribiendoGrafica = ""
        self.enlaceNodosSub = ""
    def analizando(self, texto1):
        tok = ''
        # Eliminando espacios y saltos de linea de la cadena
        # texto = texto.replace("\n","")
        # texto = texto.replace(" ","")
        validandoError = False
        texto = texto1
        # recorriendo el texto
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

            # validaciones de acuerdo al caracter que se está leyendo
            # valida cuando inicia leyendo el texto
            if self.estadoActual == '':
                if caracter == '{':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q0'
                    self.estadoActual = 'q1'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # valida cuando se encuentra en el estado q1
            if self.estadoActual == 'q1':
                if caracter == '{':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q1'
                    self.estadoActual = 'q2'
                elif caracter == '"':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q1'
                    self.estadoActual = 'q3'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # valida cuando se encuentra en q3 ***************************
            elif self.estadoActual == 'q3':
                if caracter.lower() in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'q3'
                    self.estadoActual = 'q4'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # valida cuando se encuentra en q4
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
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            elif self.estadoActual == 'q5':
                if caracter == ':':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q5'
                    self.estadoActual = 'q6'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            elif self.estadoActual == 'q6':
                if caracter == '"':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q6'
                    self.estadoActual = 'q7'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            elif self.estadoActual == 'q7':
                if caracter.lower() in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'q7'
                    self.estadoActual = 'q8'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # valida cuando se encuentra en q8
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
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # valida cuando se encuentra en q9
            elif self.estadoActual == 'q9':
                if caracter == ',':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q9'
                    self.estadoActual = 'q1'
                    validandoError = False
                elif caracter == '}':
                    # estado de aceptación
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q9'
                    self.estadoActual = 'q10'
                    validandoError = False
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # Aqui termina una parte  ***************************
            # Segunda parte
            # validar estado q2
            elif self.estadoActual == 'q2':
                if caracter == '"':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q2'
                    self.estadoActual = 'q11'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # validacion estado q11
            elif self.estadoActual == 'q11':
                if caracter.lower() in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'q11'
                    self.estadoActual = 'q12'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # validando estado q12
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
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # validando estado q13
            elif self.estadoActual == 'q13':
                if caracter == ':':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q13'
                    self.estadoActual = 'q14'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # validando estado q14
            elif self.estadoActual == 'q14':
                if caracter in self.numeros:
                    tok += caracter
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
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # validando estado q15
            elif self.estadoActual == 'q15':
                if caracter.lower() in self.letras:
                    tok += caracter
                    self.estadoAnterior = 'q15'
                    self.estadoActual = 'q16'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # validando estado q16
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
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # validando estado q17
            elif self.estadoActual == 'q17':
                if caracter == ',':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q17'
                    self.estadoActual = 'q2'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # validando estado q18
            elif self.estadoActual == 'q18':
                if caracter in self.numeros:
                    tok += caracter
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
                    self.estadoAnterior = 'q18'
                    self.estadoActual = 'q19'
                elif caracter == ']':
                    self.almacenarToken(tok)
                    tok = ''
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q18'
                    self.estadoActual = 'q24'
                elif caracter == '}':
                    self.almacenarToken(tok)
                    tok = ''
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q18'
                    self.estadoActual = 'q22'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # validando estado q19
            elif self.estadoActual == 'q19':
                if caracter in self.numeros:
                    tok += caracter
                    self.estadoAnterior = 'q19'
                    self.estadoActual = 'q20'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # validando estado q20
            elif self.estadoActual == 'q20':
                if caracter in self.numeros:
                    tok += caracter
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
                elif caracter == '}':
                    self.almacenarToken(tok)
                    tok = ''
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q20'
                    self.estadoActual = 'q22'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # validando estado q21
            elif self.estadoActual == 'q21':
                if caracter == ']':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q21'
                    self.estadoActual = 'q21'
                elif caracter == '}':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q21'
                    self.estadoActual = 'q22'
                elif caracter == ',':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q21'
                    self.estadoActual = 'q2'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # validando estado q22
            elif self.estadoActual == 'q22':
                if caracter == ',':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q22'
                    self.estadoActual = 'q1'
                    validandoError = False
                    # estado de acpetación
                elif caracter == '}':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q22'
                    self.estadoActual = 'q23'
                else:
                    validandoError = True
                    self.almacenarError(caracter)
            # validando estado q24
            elif self.estadoActual == 'q24':
                if caracter == ']':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q24'
                    self.estadoActual = 'q24'
                elif caracter == ',':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q24'
                    self.estadoActual = 'q2'
                elif caracter == '}':
                    self.almacenarToken(caracter)
                    self.estadoAnterior = 'q24'
                    self.estadoActual = 'q22'
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

    def erroresValidados(self):
        escribiendoEstructura = "{\n"
        iterador = 1
        for token in self.tablaErrores:
            escribiendoEstructura = escribiendoEstructura + "\t{\n"
            escribiendoEstructura = escribiendoEstructura + \
                '\t\t"No.":' + str(iterador) + "\n"
            escribiendoEstructura = escribiendoEstructura + \
                '\t\t"Descripcion-Token":{\n'
            escribiendoEstructura = escribiendoEstructura + \
                '\t\t\t"Lexema": ' + str(token.lexema) + '\n'
            escribiendoEstructura = escribiendoEstructura + '\t\t\t"Tipo": Error\n'
            escribiendoEstructura = escribiendoEstructura + \
                '\t\t\t"Columna": ' + str(token.columna) + '\n'
            escribiendoEstructura = escribiendoEstructura + \
                '\t\t\t"Fila": ' + str(token.row) + '\n'
            escribiendoEstructura = escribiendoEstructura + "\t\t}\n"
            escribiendoEstructura = escribiendoEstructura + "\t},\n"
            iterador += 1
            # print(token.row, token.columna, token.lexema)
        total = escribiendoEstructura[:-2] + "\n}"
        # escribiendoEstructura = total +"\n}"
        return total

    

    def analizandoSintacticamente(self):
        self.iniciandoEsGrafica = '''digraph G {
        rankdir=LR
        size= 8.5
        ranksep=1
        bgcolor = lightgoldenrodyellow
        margin = 0.1
        edge[arrowhead = vee];'''
        self.escribiendoGrafica = ""
        calculando = Operaciones()
        # recorrer la tabla y ir validando con ifs anidados para ver los datos que están como frases o como numeros
        self.iterar = 1
        # valida si viene un  corchete
        while self.iterar < len(self.tabla):
            if self.tabla[self.iterar].lexema == "{":
                print(self.tabla[self.iterar].lexema)
                self.iterar += 1
                # valida si el siguiente es una comilla
                if self.tabla[self.iterar].lexema == '"':
                    self.iterar += 1
                    if self.tabla[self.iterar].lexema.lower() == 'operacion':
                        asignacion_Operacion = ""
                        self.iterar += 1
                        # valida si el que finaliza es una comilla entonces se creó la variable operacion
                        if self.tabla[self.iterar].lexema == '"':
                            self.iterar += 1
                            if self.tabla[self.iterar].lexema == ':':
                                # aqui se valida si lo ve sigue son comillas para la asignacion de la variable
                                self.iterar += 1
                                if self.tabla[self.iterar].lexema == '"':
                                    self.iterar += 1
                                    asignacion_Operacion = self.tabla[self.iterar].lexema
                                    print(asignacion_Operacion)
                                    self.iterar += 1
                                    if self.tabla[self.iterar].lexema == '"':
                                        self.iterar += 1
                                        if self.tabla[self.iterar].lexema == ',':
                                            self.iterar += 1
                                            if self.tabla[self.iterar].lexema == '"':
                                                self.iterar += 1
                                                if self.tabla[self.iterar].lexema.lower() == 'valor1':
                                                    valor1 = ""
                                                    self.iterar += 1
                                                    if self.tabla[self.iterar].lexema == '"':
                                                        self.iterar += 1
                                                        if self.tabla[self.iterar].lexema == ':':
                                                            self.iterar += 1
                                                            if self.tabla[self.iterar].lexema == '[':
                                                                resultado_valor1 = self.operacionAnidada()
                                                                enlace1 = self.enlaceNodosSub
                                                                print(resultado_valor1)
                                                                if self.tabla[self.iterar].lexema == ']':
                                                                    self.iterar += 1
                                                                    if self.tabla[self.iterar].lexema == ',':
                                                                        self.iterar += 1
                                                                        if self.tabla[self.iterar].lexema == '"':
                                                                            self.iterar += 1
                                                                            if self.tabla[self.iterar].lexema.lower() == 'valor2':
                                                                                valor2 = ""
                                                                                self.iterar += 1
                                                                                if self.tabla[self.iterar].lexema == '"':
                                                                                    self.iterar += 1
                                                                                    if self.tabla[self.iterar].lexema == ':':
                                                                                        self.iterar += 1
                                                                                        if self.tabla[self.iterar].lexema == '[':
                                                                                            resultado_valor2 = self.operacionAnidada()
                                                                                            print(resultado_valor2)
                                                                                            resultadoCalculos = calculando.operando(resultado_valor1, resultado_valor2, asignacion_Operacion)
                                                                                            print("Resultado: " + str(resultadoCalculos))
                                                                                            enlace2 = self.enlaceNodosSub
                                                                                            self.escribiendoGrafica = self.escribiendoGrafica +'''
    a0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];
    a0 ->'''+ enlace1 +''';
    a0 ->'''+ enlace2 +''';'''
                                                                                            if self.tabla[self.iterar].lexema == ']':
                                                                                                self.iterar += 1
                                                                                                if self.tabla[self.iterar].lexema == ']':
                                                                                                    self.iterar += 1
                                                                                                elif self.tabla[self.iterar].lexema == '}':
                                                                                                    print(self.tabla[self.iterar].lexema)
                                                                                                    self.iterar += 1
                                                                                        else:
                                                                                            valor2 = self.tabla[self.iterar].lexema
                                                                                            print(valor2)
                                                                                            self.iterar += 1
                                                                                            resultadoCalculos = calculando.operando(resultado_valor1, valor2, asignacion_Operacion)

                                                                                            print("Resultado: " + str(resultadoCalculos))

                                                                                            self.escribiendoGrafica = self.escribiendoGrafica + '''
    b0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];
    b2  [label = "'''+str(valor2)+'''"];
    b0 ->'''+ enlace1 +''';
    b0 -> b2;'''
                                                                                            if self.tabla[self.iterar].lexema == '}':
                                                                                                print(self.tabla[self.iterar].lexema)
                                                                                                self.iterar += 1
                                                                    else :
                                                                        
                                                                        resultadoCalculos = calculando.operando(resultado_valor1, None,asignacion_Operacion)
                                                                        print("Resultado: " + str(resultadoCalculos))
                                                                        self.escribiendoGrafica = self.escribiendoGrafica +'''
    z0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];
    z0 ->'''+ enlace1 +''';'''
                                                                        print(self.tabla[self.iterar].lexema)
                                                                        self.iterar += 1
                                                            else:
                                                                valor1 = self.tabla[self.iterar].lexema
                                                                print(valor1)
                                                                self.iterar += 1
                                                                if self.tabla[self.iterar].lexema == ',':
                                                                    self.iterar += 1
                                                                    if self.tabla[self.iterar].lexema == '"':
                                                                        self.iterar += 1
                                                                        if self.tabla[self.iterar].lexema.lower() == 'valor2':
                                                                            valor2 = ""
                                                                            self.iterar += 1
                                                                            if self.tabla[self.iterar].lexema == '"':
                                                                                self.iterar += 1
                                                                                if self.tabla[self.iterar].lexema == ':':
                                                                                    self.iterar += 1
                                                                                    if self.tabla[self.iterar].lexema == '[':
                                                                                        resultado_valor2 = self.operacionAnidada()
                                                                                        print(resultado_valor2)
                                                                                        resultadoCalculos = calculando.operando(valor1, resultado_valor2, asignacion_Operacion)
                                                                                        print("Resultado: " + str(resultadoCalculos))
                                                                                        enlace2 = self.enlaceNodosSub
                                                                                        self.escribiendoGrafica = self.escribiendoGrafica + '''
    c0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];
    c1  [label = "'''+str(valor1)+'''"];
    c0 -> c1;
    c0 ->'''+ enlace2 +''';'''
                                                                                        if self.tabla[self.iterar].lexema == ']':
                                                                                            self.iterar += 1
                                                                                            if self.tabla[self.iterar].lexema == '}':
                                                                                                print(self.tabla[self.iterar].lexema)
                                                                                                self.iterar += 1
                                                                                    else:
                                                                                        valor2 = self.tabla[self.iterar].lexema
                                                                                        print(valor2)
                                                                                        resultadoCalculos = calculando.operando(valor1, valor2, asignacion_Operacion)
                                                                                        print("Resultado: " + str(resultadoCalculos))

                                                                                        self.escribiendoGrafica = self.escribiendoGrafica + '''
    d0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];
    d1  [label = "'''+str(valor1)+'''"];
    d2  [label = "'''+str(valor2)+'''"];
    d0 -> d1;
    d0 -> d2;'''
                                                                                        self.iterar += 1
                                                                                        if self.tabla[self.iterar].lexema == '}':
                                                                                            print(self.tabla[self.iterar].lexema)
                                                                                            self.iterar += 1
                                                                else:
                                                                    resultadoCalculos = calculando.operando(valor1, None,asignacion_Operacion)
                                                                    print("Resultado: " + str(resultadoCalculos))
                                                                    self.escribiendoGrafica = self.escribiendoGrafica +'''
    y0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];
    y1  [label = "'''+str(valor1)+'''"];
    y0 -> y1;'''
                                                                    print(self.tabla[self.iterar].lexema)
                                                                    self.iterar += 1                       
            elif self.tabla[self.iterar].lexema == '"':
                    self.iterar += 1
                    if self.tabla[self.iterar].lexema.lower() == 'texto':
                        asignacion_texto = ""
                        self.iterar += 1
                        # valida si el que finaliza es una comilla entonces se creó la variable operacion
                        if self.tabla[self.iterar].lexema == '"':
                            self.iterar += 1
                            if self.tabla[self.iterar].lexema == ':':
                                # aqui se valida si lo ve sigue son comillas para la asignacion de la variable
                                self.iterar += 1
                                if self.tabla[self.iterar].lexema == '"':
                                    self.iterar += 1
                                    asignacion_texto = self.tabla[self.iterar].lexema
                                    print(asignacion_texto)
                                    self.iterar += 1
                                    if self.tabla[self.iterar].lexema == '"':
                                        continue
                    elif self.tabla[self.iterar].lexema.lower() == 'color-fondo-nodo':
                        asignacion_ColorFondo = ""
                        self.iterar += 1
                        # valida si el que finaliza es una comilla entonces se creó la variable operacion
                        if self.tabla[self.iterar].lexema == '"':
                            self.iterar += 1
                            if self.tabla[self.iterar].lexema == ':':
                                # aqui se valida si lo ve sigue son comillas para la asignacion de la variable
                                self.iterar += 1
                                if self.tabla[self.iterar].lexema == '"':
                                    self.iterar += 1
                                    asignacion_ColorFondo = self.tabla[self.iterar].lexema
                                    print(asignacion_ColorFondo)
                                    self.iterar += 1
                                    if self.tabla[self.iterar].lexema == '"':
                                        continue
                    elif self.tabla[self.iterar].lexema.lower() == 'color-fuente-nodo':
                        asignacion_ColorFuente = ""
                        self.iterar += 1
                        # valida si el que finaliza es una comilla entonces se creó la variable operacion
                        if self.tabla[self.iterar].lexema == '"':
                            self.iterar += 1
                            if self.tabla[self.iterar].lexema == ':':
                                # aqui se valida si lo ve sigue son comillas para la asignacion de la variable
                                self.iterar += 1
                                if self.tabla[self.iterar].lexema == '"':
                                    self.iterar += 1
                                    asignacion_ColorFuente = self.tabla[self.iterar].lexema
                                    print(asignacion_ColorFuente)
                                    self.iterar += 1
                                    if self.tabla[self.iterar].lexema == '"':
                                        continue
                    elif self.tabla[self.iterar].lexema.lower() == 'forma-nodo':
                        asignacion_Forma = ""
                        self.iterar += 1
                        # valida si el que finaliza es una comilla entonces se creó la variable operacion
                        if self.tabla[self.iterar].lexema == '"':
                            self.iterar += 1
                            if self.tabla[self.iterar].lexema == ':':
                                # aqui se valida si lo ve sigue son comillas para la asignacion de la variable
                                self.iterar += 1
                                if self.tabla[self.iterar].lexema == '"':
                                    self.iterar += 1
                                    asignacion_Forma = self.tabla[self.iterar].lexema.lower() 
                                    print(asignacion_Forma)
                                    self.iterar += 1
                                    if self.tabla[self.iterar].lexema == '"':
                                        continue
            self.iterar += 1
        self.iniciandoEsGrafica = self.iniciandoEsGrafica + 'node [style=filled,color='+asignacion_ColorFondo+', shape = '+asignacion_Forma+',fontcolor= '+asignacion_ColorFuente+'];\n\t\tlabel = "'+asignacion_texto+'";'
        #self.escribiendoGrafica = self.escribiendoGrafica + "}"
        self.iniciandoEsGrafica = self.iniciandoEsGrafica+self.escribiendoGrafica + "}"

        return self.iniciandoEsGrafica
    def operacionAnidada(self):
        calculando = Operaciones()
        self.iterar +=1
        #valida si el siguiente es una comilla
        if self.tabla[self.iterar].lexema == '"':
            self.iterar +=1
            if self.tabla[self.iterar].lexema.lower() == 'operacion':
                asignacion_Operacion = ""
                self.iterar +=1
                #valida si el que finaliza es una comilla entonces se creó la variable operacion
                if self.tabla[self.iterar].lexema == '"':
                    self.iterar +=1
                    if self.tabla[self.iterar].lexema == ':':
                        #aqui se valida si lo ve sigue son comillas para la asignacion de la variable
                        self.iterar +=1
                        if self.tabla[self.iterar].lexema == '"':
                            self.iterar +=1
                            asignacion_Operacion = self.tabla[self.iterar].lexema
                            print(asignacion_Operacion)
                            self.iterar +=1
                            if self.tabla[self.iterar].lexema == '"':
                                self.iterar +=1
                                if self.tabla[self.iterar].lexema == ',':
                                    self.iterar +=1
                                    if self.tabla[self.iterar].lexema == '"':
                                        self.iterar +=1
                                        if self.tabla[self.iterar].lexema.lower() == 'valor1':
                                            valor1 = ""
                                            self.iterar += 1
                                            if self.tabla[self.iterar].lexema == '"':
                                                self.iterar +=1
                                                if self.tabla[self.iterar].lexema == ':':
                                                    self.iterar +=1
                                                    if self.tabla[self.iterar].lexema == '[':
                                                        resultado_valor1 = self.operacionAnidada()
                                                        enlace1 = self.enlaceNodosSub
                                                        print(resultado_valor1)
                                                        if self.tabla[self.iterar].lexema == ']':
                                                            self.iterar += 1
                                                            if self.tabla[self.iterar].lexema == ',':
                                                                self.iterar += 1
                                                                if self.tabla[self.iterar].lexema == '"':
                                                                    self.iterar += 1
                                                                    if self.tabla[self.iterar].lexema.lower() == 'valor2':
                                                                        valor2 = ""
                                                                        self.iterar += 1
                                                                        if self.tabla[self.iterar].lexema == '"':
                                                                            self.iterar += 1
                                                                            if self.tabla[self.iterar].lexema == ':':
                                                                                self.iterar += 1
                                                                                if self.tabla[self.iterar].lexema == '[':
                                                                                    resultado_valor2 = self.operacionAnidada()
                                                                                    print(resultado_valor2)
                                                                                    resultadoCalculos = calculando.operando(resultado_valor1, resultado_valor2, asignacion_Operacion)
                                                                                    print("Resultado: " + str(resultadoCalculos))
                                                                                    enlace2 = self.enlaceNodosSub
                                                                                    self.escribiendoGrafica = self.escribiendoGrafica + '''
    e0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];
    e0 ->'''+ enlace1 +''';
    e0 ->'''+ enlace2 +''';'''

                                                                                    self.enlaceNodosSub = "e0"
                                                                                    return resultadoCalculos
                                                                                else:
                                                                                    valor2 = self.tabla[self.iterar].lexema
                                                                                    print(valor2)
                                                                                    self.iterar += 1
                                                                                    resultadoCalculos = calculando.operando(resultado_valor1, valor2, asignacion_Operacion)
                                                                                    print("Resultado: " + str(resultadoCalculos))
                                                                                    
                                                                                    self.escribiendoGrafica = self.escribiendoGrafica + '''
    f0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"]
    f2  [label = "'''+str(valor2)+'''"];
    f0 ->'''+ enlace1 +''';
    f0 -> f2;'''
                                                                                    self.enlaceNodosSub = "f0"
                                                                                    return resultadoCalculos
                                                            else:
                                                                resultadoCalculos = calculando.operando(resultado_valor1, None, asignacion_Operacion)
                                                                print("Resultado: " + str(resultadoCalculos))
                                                                self.escribiendoGrafica = self.escribiendoGrafica + '''
    g0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];
    g0 ->'''+ enlace1 +''';'''
                                                                self.enlaceNodosSub = "g0"
                                                                return resultadoCalculos
                                                    else:
                                                        valor1 = self.tabla[self.iterar].lexema
                                                        print(valor1)
                                                        self.iterar +=1
                                                        if self.tabla[self.iterar].lexema == ',':
                                                            self.iterar +=1
                                                            if self.tabla[self.iterar].lexema == '"':
                                                                self.iterar +=1
                                                                if self.tabla[self.iterar].lexema.lower() == 'valor2':
                                                                    valor2 = ""
                                                                    self.iterar += 1
                                                                    if self.tabla[self.iterar].lexema == '"':
                                                                        self.iterar +=1
                                                                        if self.tabla[self.iterar].lexema == ':':
                                                                            self.iterar +=1
                                                                            if self.tabla[self.iterar].lexema == '[':
                                                                                resultado_valor2 = self.operacionAnidada() 
                                                                                print(resultado_valor2)
                                                                                resultadoCalculos = calculando.operando(valor1, resultado_valor2, asignacion_Operacion)
                                                                                print("Resultado: " + str(resultadoCalculos))
                                                                                enlace2 = self.enlaceNodosSub
                                                                                self.escribiendoGrafica = self.escribiendoGrafica + '''
    h0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];
    h1  [label = "'''+str(valor1)+'''"];
    h0 -> h1;
    h0 ->'''+ enlace2 +';'
                                                                                self.enlaceNodosSub = "h0"
                                                                                return resultadoCalculos
                                                                            else:
                                                                                valor2 = self.tabla[self.iterar].lexema
                                                                                print(valor2)
                                                                                resultadoCalculos = calculando.operando(valor1, valor2, asignacion_Operacion)
                                                                                print("Resultado: " + str(resultadoCalculos))
                                                                                self.escribiendoGrafica = self.escribiendoGrafica + '''
    i0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"]
    i1  [label = "'''+str(valor1)+'''"];
    i2  [label = "'''+str(valor2)+'''"];
    i0 -> i1;
    i0 -> i2;'''
                                                                                self.enlaceNodosSub = "i0"
                                                                                self.iterar +=1
                                                                                return resultadoCalculos
                                                        else:
                                                            resultadoCalculos = calculando.operando(valor1, None, asignacion_Operacion)
                                                            print("Resultado: " + str(resultadoCalculos))
                                                            self.escribiendoGrafica = self.escribiendoGrafica + '''
    j0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];
    j1  [label = "'''+str(valor1)+'''"];
    j0 -> j1;'''
                                                            self.enlaceNodosSub = "j0"
                                                            return resultadoCalculos
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

    def almacenarError(self, lexemaError):
        newToken1 = Token(self.fila, self.columna, lexemaError)
        self.tablaErrores.append(newToken1)
# https://www.ibidemgroup.com/edu/traduccion-automatica-python/    para traducir idiomas
