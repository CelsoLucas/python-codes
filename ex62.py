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


while True:
    print("1 - Criar retangulo")
    print("2 - Sair")
    opc = int(input("Opção: "))
    if opc == 1:
        lar = float(input("Largura: "))
        alt = float(input("Altura: "))
        ret = Retangulo(lar, alt)
        ret.encontrar_centro()
    elif opc == 2:
        break
    else:
        print("Opção invalida!")
