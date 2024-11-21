from pydantic import BaseModel

class Usuario(BaseModel):
    nome : str
    sexo : str
    idade : int
usuario = Usuario(nome = "Celso", idade = 17, sexo = "Masculino")
print(usuario.nome)
print(usuario.idade)
print(usuario.sexo)