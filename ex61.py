class Macaco():
    def __init__(self, nome):
        self.nome = nome
        self.bucho = "Vazio"
    
    def comer(self):
        self.alimento = str(input(f"Oque o {self.nome} vai comer: "))
        self.bucho = self.alimento
    def verBucho(self):
        print(f"{self.bucho}")

    def digerir(self):
        self.bucho = "Vazio"

macaco1 = Macaco("Yuri")
macaco2 = Macaco("Dona")
macaco1.comer()
macaco2.comer()
macaco1.verBucho()
macaco2.verBucho()
macaco1.digerir()
macaco2.digerir()
macaco1.verBucho()
macaco2.verBucho()
macaco1.comer()
macaco2.comer()
macaco1.verBucho()
macaco2.verBucho()
macaco1.digerir()
macaco2.digerir()
macaco1.verBucho()
macaco2.verBucho()
macaco1.comer()
macaco2.comer()
macaco1.verBucho()
macaco2.verBucho()
macaco1.digerir()
macaco2.digerir()
macaco1.verBucho()
macaco2.verBucho()