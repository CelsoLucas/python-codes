import matplotlib.pyplot as plt

#Gráfico de Linha
# a = (1, 2, 3, 4, 5)
# b = (10, 4, 6, 3, 7)

# plt.plot(a, b, "mD:") # Depois do segundo parametro pode colocar outro sendo como vai ser a aparencia da linha, x - y
# plt.title("Meu Gráfico")
# plt.ylabel(u"Alguns números y")
# plt.xlabel(u"Alguns números x")
# plt.axis((1, 5, 1, 15)) #  Onde começa e termina os eixos, x depois y
# plt.grid(True) # Grade do Gráfico

# ===================================================================================

#Gráfico de Dispersão
# a = (1, 2, 3, 4, 5, 6)
# b = (2, 4, 6, 8, 10, 12)
# plt.scatter(a, b)

#====================================================================================

#Gráfico de Barras
# a = (1, 2, 3, 4, 5, 6)
# b = (2, 4, 6, 8, 10, 12)
# plt.bar(a, b)

#====================================================================================

#Gráfico Histograma
# a = (1, 2, 3, 4, 5, 6)
# b = (2, 4, 6, 8, 10, 12)
# plt.hist(a, b)

#====================================================================================

#Gráfico de Pizza
a = (10, 20, 30)
explode = (0.1, 0, 0)
labels = ["HB20", "GOL", "FUSCA"]
plt.pie(a, explode=explode, labels=labels, autopct="%.2f%%", shadow=True)
plt.title("Meu Gráfico")
plt.grid(True)
plt.show()