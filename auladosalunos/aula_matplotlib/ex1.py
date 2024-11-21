import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 9, 25]

plt.plot(x, y)

plt.title("Gráfico Simples")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.legend()
plt.show()