import matplotlib.pyplot as plt

candidatos = ("Adriane Lopes (31,67%)", "Rose Modesto (29,56%)", "Beto Pereira(25,96%)", "Camila Jara (9,43%)", "Outros (3,69%)")
votos = (140913, 131525, 115516, 41966, 15060)

cores = [
    "red", "blue", "green", "purple", "orange"
]
plt.bar(candidatos, votos, color=cores)
plt.ylabel("Votos")
plt.xlabel("Candidatos")
plt.grid(True)
plt.show()