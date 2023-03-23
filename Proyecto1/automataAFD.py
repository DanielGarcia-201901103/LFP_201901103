from token import Token
from operar import Operaciones
#import graphviz

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
        for token in self.tablaErrores:
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

    '''
    {"Operacion":"Resta",
    "Valor1":4.5,
    "Valor2":[
    "Operacion":"Potencia",
    "Valor1":10,
    "Valor2":[
        "Operacion":"Suma",
        "Valor1":10,
        "Valor2":3
        ]
    ]},

    {"Operacion":"Suma",
    "Valor1":[
    "Operacion":"Seno",
    "Valor1":90
    ],
    "Valor2":5.32},
    "Texto":"Realizacion de Operaciones",
    "Color-Fondo-Nodo":"Yellow",
    "Color-Fuente-Nodo":"Red",
    "Forma-Nodo":"Circulo"
            '''

    def analizandoSintacticamente(self):
        self.escribiendoGrafica = '''digraph G {
            rankdir=LR
            size= 8.5
            ranksep=1
            bgcolor = lightgoldenrodyellow
            margin = 0.1'''

        #grafo = graphviz.Digraph('graficaOperaciones',filename ='graficaOperaciones.dot')
        #grafo.attr(rankdir = 'LR',size='8,5', ranksep="2", bgcolor = "lightgoldenrodyellow", margin = "0.1")
        #grafo.attr('node', shape= 'circle',style="filled", color="black",fillcolor="lightsalmon")
        #grafo.node(asignacion_Operacion,"lo que se muestra en el nodo")
        #grafo.attr('node', shape= 'circle', style="filled", color="black",fillcolor="lightsalmon")
        #grafo.edge(""+':e', "", arrowhead = 'vee')
        #grafo.attr('node',style='', color='')
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


                                                                                            self.escribiendoGrafica = self.escribiendoGrafica + '''
                                                                                            node [style=filled,color=white, shape = circle];
                                                                                            edge[arrowhead = vee];'''+'''
                                                                                            a0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];a1  [label = "'''+str(resultado_valor1)+'''"];
                                                                                            a2  [label = "'''+str(resultado_valor2)+'''"];
                                                                                            a0 -> a1;
                                                                                            a0 -> a2;
                                                                                            '''
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
                                                                                            node [style=filled,color=white, shape = circle];
                                                                                            edge[arrowhead = vee];'''+'''
                                                                                            b0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];b1  [label = "'''+str(resultado_valor1)+'''"];
                                                                                            b2  [label = "'''+str(valor2)+'''"];
                                                                                            b0 -> b1;
                                                                                            b0 -> b2;
                                                                                            '''
                                                                                            if self.tabla[self.iterar].lexema == '}':
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

                                                                                        self.escribiendoGrafica = self.escribiendoGrafica + '''
                                                                                            node [style=filled,color=white, shape = circle];
                                                                                            edge[arrowhead = vee];'''+'''
                                                                                            c0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];c1  [label = "'''+str(valor1)+'''"];
                                                                                            c2  [label = "'''+str(resultado_valor2)+'''"];
                                                                                            c0 -> c1;
                                                                                            c0 -> c2;
                                                                                            '''
                                                                                        if self.tabla[self.iterar].lexema == ']':
                                                                                            self.iterar += 1
                                                                                            if self.tabla[self.iterar].lexema == '}':
                                                                                                print(
                                                                                                    self.tabla[self.iterar].lexema)
                                                                                                self.iterar += 1
                                                                                    else:
                                                                                        valor2 = self.tabla[self.iterar].lexema
                                                                                        print(valor2)
                                                                                        resultadoCalculos = calculando.operando(valor1, valor2, asignacion_Operacion)
                                                                                        print("Resultado: " + str(resultadoCalculos))

                                                                                        self.escribiendoGrafica = self.escribiendoGrafica + '''
                                                                                            node [style=filled,color=white, shape = circle];
                                                                                            edge[arrowhead = vee];'''+'''
                                                                                            d0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];d1  [label = "'''+str(valor1)+'''"];
                                                                                            d2  [label = "'''+str(valor2)+'''"];
                                                                                            d0 -> d1;
                                                                                            d0 -> d2;
                                                                                            '''
                                                                                        self.iterar += 1
                                                                                        if self.tabla[self.iterar].lexema == '}':
                                                                                            print(self.tabla[self.iterar].lexema)
                                                                                            self.iterar += 1
            
            self.iterar += 1
        #grafo.view(filename ="graficaOperaciones.dot" ,directory="./Proyecto1")
        # print(asignacion_Operacion)
        self.escribiendoGrafica = self.escribiendoGrafica + "}"
        return self.escribiendoGrafica
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

                                                                                    self.escribiendoGrafica = self.escribiendoGrafica + '''
                                                                                            node [style=filled,color=white, shape = circle];
                                                                                            edge[arrowhead = vee];'''+'''
                                                                                            e0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];e1  [label = "'''+str(resultado_valor1)+'''"];
                                                                                            e2  [label = "'''+str(resultado_valor2)+'''"];
                                                                                            e0 -> e1;
                                                                                            e0 -> e2;
                                                                                            '''


                                                                                    return resultadoCalculos
                                                                                else:
                                                                                    valor2 = self.tabla[self.iterar].lexema
                                                                                    print(valor2)
                                                                                    self.iterar += 1
                                                                                    resultadoCalculos = calculando.operando(resultado_valor1, valor2, asignacion_Operacion)
                                                                                    print("Resultado: " + str(resultadoCalculos))

                                                                                    self.escribiendoGrafica = self.escribiendoGrafica + '''
                                                                                            node [style=filled,color=white, shape = circle];
                                                                                            edge[arrowhead = vee];'''+'''
                                                                                            f0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];f1  [label = "'''+str(resultado_valor1)+'''"];
                                                                                            f2  [label = "'''+str(valor2)+'''"];
                                                                                            f0 -> f1;
                                                                                            f0 -> f2;
                                                                                            '''
                                                                                    
                                                                                    return resultadoCalculos
                                                            else:
                                                                resultadoCalculos = calculando.operando(resultado_valor1, None, asignacion_Operacion)
                                                                print("Resultado: " + str(resultadoCalculos))
                                                                self.escribiendoGrafica = self.escribiendoGrafica + '''
                                                                                            node [style=filled,color=white, shape = circle];
                                                                                            edge[arrowhead = vee];'''+'''
                                                                                            g0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];g1  [label = "'''+str(resultado_valor1)+'''"];
                                                                                            g0 -> g1;
                                                                                            '''
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
                                                                                self.escribiendoGrafica = self.escribiendoGrafica + '''
                                                                                            node [style=filled,color=white, shape = circle];
                                                                                            edge[arrowhead = vee];'''+'''
                                                                                            h0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];h1  [label = "'''+str(valor1)+'''"];
                                                                                            h2  [label = "'''+str(resultado_valor2)+'''"];
                                                                                            h0 -> h1;
                                                                                            h0 -> h2;
                                                                                            '''
                                                                                return resultadoCalculos
                                                                            else:
                                                                                valor2 = self.tabla[self.iterar].lexema
                                                                                print(valor2)
                                                                                resultadoCalculos = calculando.operando(valor1, valor2, asignacion_Operacion)
                                                                                print("Resultado: " + str(resultadoCalculos))
                                                                                self.escribiendoGrafica = self.escribiendoGrafica + '''
                                                                                            node [style=filled,color=white, shape = circle];
                                                                                            edge[arrowhead = vee];'''+'''
                                                                                            i0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];i1  [label = "'''+str(valor1)+'''"];
                                                                                            i2  [label = "'''+str(valor2)+'''"];
                                                                                            i0 -> i1;
                                                                                            i0 -> i2;
                                                                                            '''
                                                                                self.iterar +=1
                                                                                return resultadoCalculos
                                                        else:
                                                            resultadoCalculos = calculando.operando(valor1, None, asignacion_Operacion)
                                                            print("Resultado: " + str(resultadoCalculos))
                                                            self.escribiendoGrafica = self.escribiendoGrafica + '''
                                                                                            node [style=filled,color=white, shape = circle];
                                                                                            edge[arrowhead = vee];'''+'''
                                                                                            j0  [label = "'''+asignacion_Operacion+'''\n'''+str(resultadoCalculos)+'''"];j1  [label = "'''+str(valor1)+'''"];
                                                                                            j0 -> j1;
                                                                                            '''
                                                            return resultadoCalculos

    def almacenarError(self, lexemaError):
        newToken1 = Token(self.fila, self.columna, lexemaError)
        self.tablaErrores.append(newToken1)
# https://www.ibidemgroup.com/edu/traduccion-automatica-python/    para traducir idiomas
