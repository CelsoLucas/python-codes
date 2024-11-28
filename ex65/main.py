from config import PessoaFisica, PessoaJuridica

print("1 - Pessoa Fisica")
print("2 - Pessoa Juridica")
opc = int(input("Digite a opção: "))
if opc == 1:
    p1 = PessoaFisica()
elif opc == 2:
    p1 = PessoaJuridica()
else:
    print("Opção invalida")