import matplotlib.pyplot as plt

salarios = (151.00, 180.00, 200.00, 240.00, 260.00,
            300.00, 380.00, 415.00, 465.00, 510.00,
            540.00, 545.00, 622.00, 678.00, 724.00,
            788.00, 880.00, 937.00, 954.00, 998.00, 
            1039.00, 1045.00, 1100.00, 1212.00, 1302.00, 
            1518.00)
anos = (2000, 2001, 2002, 2003, 2004, 2005,
        2006, 2007, 2008, 2009, 2010, 2011,
        2012, 2013, 2014, 2015, 2016, 2017,
        2018, 2019, 2020, 2021, 2022, 2023,
        2024, 2025)
cores = [
    "red", "blue", "green", "purple", "orange", "cyan", 
    "pink", "brown", "gray", "yellow", "magenta", "lime", 
    "teal", "navy", "gold", "coral", "violet", "indigo",
    "crimson", "olive", "maroon", "turquoise", "plum", "chocolate",
    "peru", "dodgerblue"
]

plt.bar(anos, salarios, color=cores)
plt.ylabel("Salario R$")
plt.xlabel("Ano (2000-2025)")
plt.grid(True)
plt.xticks(anos, rotation=45)
plt.show()