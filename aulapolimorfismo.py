class Super():
    def hello(self):
        print("Olá, sou a superclasse!!")
    def printar(self):
        print('Teste')
class Sub(Super):
    def hello(self):
        print("Hello, sou a sub clase")
class Subsub(Sub):
    def hello(self):
        print("Olá, sou a subsubclasse!")

teste = Subsub()
teste.hello()
teste.printar()