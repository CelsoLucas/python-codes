class TV():
    def __init__(self):
        self.btn_volume = 0
        self.btn_canal = 0

    def aumentar_diminuir(self, btn1):
        if btn1 == "+":
            if self.btn_volume >= 10:
                print(f"Volume Maximo! {self.btn_volume}")
            else:
                self.btn_volume += 1
                print(f"Volume: {self.btn_volume}")
        elif btn1 == "-":
            if self.btn_volume <= 0:
                print(f"Volume Minimo! {self.btn_volume}")
            else:
                self.btn_volume -= 1
                print(f"Volume: {self.btn_volume}")
        else:
            print("Opção invalida!")

    def mudar_canal(self, btn2):
        if btn2 == ">":
            if self.btn_canal >= 10:
                print(f"Ultimo canal disponivel {self.btn_canal}")
            else:
                self.btn_canal += 1
                print(f"Canal:  {self.btn_canal}")
        elif btn2 == "<":
            if self.btn_canal <= 0:
                print(f"Primeiro Canal disponivel  {self.btn_canal}")
            else:
                self.btn_canal -= 1
                print(f"Canal:  {self.btn_canal}")
        else:
            print("Opção invalida")

tv1 = TV()

while True:
    print("1 - Aumentar Volume")
    print("2 - Mudar Canal")
    print("3 - Desligar TV")
    qual = int(input("Opção que deseja: "))
    if qual == 1:
        while True:
            btn1 = str(input("+ or - or +- para parar: "))
            if btn1 == "+-":
                break
            else:
                tv1.aumentar_diminuir(btn1)
    elif qual == 2:
        while True:
            btn2 = str(input("< para anterior / > para proximo / <> para para: "))
            if btn2 == "<>":
                break
            else:
                tv1.mudar_canal(btn2)
    elif qual == 3:
        print("Saindo...")
        break

    else:
        print("Opção invalida")
