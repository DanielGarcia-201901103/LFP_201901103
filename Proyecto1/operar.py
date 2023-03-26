import math
class Operaciones:
    def __init__(self):
        pass
    
    def operando(self, valor_1, valor_2, tipoOpera):
        resultado = 0
        if valor_1 != None:
            valor_1 = float(valor_1)
        if valor_2 != None:
            valor_2 = float(valor_2)

        if tipoOpera.lower() == 'suma':
            resultado = valor_1 + valor_2
            return resultado
        elif tipoOpera.lower() == 'resta':
            resultado = valor_1 - valor_2
            return resultado
        elif tipoOpera.lower() == 'multiplicacion':
            resultado = valor_1 * valor_2
            return resultado
        elif tipoOpera.lower() == 'division':
            try:
                if valor_2 !=0:
                    resultado = valor_1 / valor_2
                else:
                    return "Error division entre 0"
            except ZeroDivisionError:
                return "Error Error division entre 0"
            else:
                return resultado
        elif tipoOpera.lower() == 'potencia':
            resultado = pow(valor_1,valor_2)
            return resultado
        elif tipoOpera.lower()== 'raiz':
            try:
                if valor_1 >= 0: 
                    resultado = math.sqrt(valor_1)
                    return resultado
                else:
                    return "No acepta negativos"
            except Exception as e:
                return e
        elif tipoOpera.lower() == 'inverso':
            try:
                if valor_1 !=0:
                    if valor_1 > 1:
                        resultado = "1" + "/" + str(valor_1)
                        return resultado
                    elif valor_1 < -1:
                        resultado = "-1" + "/" + str(valor_1 * -1)
                        return resultado
                    elif valor_1 < 0 and valor_1 > -1:
                        resultado = 1/valor_1
                        return resultado
                    elif valor_1 > 0 and valor_1 < 1:
                        resultado = 1/valor_1
                        return resultado
                    elif valor_1 == 1 or valor_1 == -1:
                        resultado = valor_1
                        return resultado
                else:
                    return "Error no existe el inverso entre 0"
            except ZeroDivisionError:
                return "Error"
        elif tipoOpera.lower() == 'seno':
            #convirtiendo el angulo a radianes
            convirtiendo = math.radians(valor_1)
            resultado = math.sin(convirtiendo)
            return resultado
        elif tipoOpera.lower() == 'coseno':
            #convirtiendo el angulo a radianes
            convirtiendo1 = math.radians(valor_1)
            resultado = math.cos(convirtiendo1)
            return resultado
        elif tipoOpera.lower()== 'tangente':
            #convirtiendo el angulo a radianes
            convirtiendo2 = math.radians(valor_1)
            resultado = math.tan(convirtiendo2)
            return resultado
        elif tipoOpera.lower() == 'mod':
            resultado = valor_1 % valor_2
            return resultado
        #MANEJAR LAS OPERACIONES EN BASE A LA TABLA DE TOKENS YA QUE SE DEBE VALIDAR LA JERARQUIA CON LA QUE INGRESAN LOS CALCULOS Y AL REALIZAR CADA CALCULO RETORNAR EL VALOR
        '''
        https://docs.python.org/3/library/math.html
        https://docs.python.org/3.11/library/math.html
        '''

#calculando = Operaciones()
#funcionan todos los calculos
#res = calculando.operando(90,0,"seno")
#print(calculando.operando(90,0,"seno"))
#print(calculando.operando(res,5.32,"suma"))
#print(calculando.operando(2,None,"inverso"))
            