class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def escreve(self):
        print(f"X: {self.x} | Y: {self.y}")
    
class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        self.x_centro = self.largura / 2
        self.y_centro = self.altura / 2
        
        centro = Ponto(self.x_centro, self.y_centro)
        centro.escreve()

ret = Retangulo(20, 15)
ret.encontrar_centro()