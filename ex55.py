class Quadrado():
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado
    
    def mostrar_area(self):
        self.area = self.tamanho_lado**2
        print(f"A área é {self.area}")

    def mudar_valor_lado(self):
        self.tamanho_lado = float(input("Novo tamanho do lado: "))
        print(f"O novo tamanho do lado é {self.tamanho_lado}")
        print(f"A nova area é {self.tamanho_lado**2}")
        
quadrado1 = Quadrado(2)
quadrado1.mostrar_area()
quadrado1.mudar_valor_lado()