class AFD:
    def __init__(self):
        self.letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','-']
        self.numeros = ['0','1','2','3','4','5','6','7','8','9']
        self.simbolos = [':','{','}',',','[',']"','"',']}','"}']
        self.estadoInicial = 'q0'
        self.estadoFinal = 'por definirse'
        self.transiciones = 'por definirse'
        self.alfabeto = {self.letras,self.numeros,self.simbolos}

    def analizando(self, texto):
        estadoActual = self.estadoInicial