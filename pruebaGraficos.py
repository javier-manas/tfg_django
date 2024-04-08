import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo (características del personaje)
categorias = ['Daño', 'Versatilidad', 'Defensa', 'Agilidad', 'Magia']
valores = [8, 7, 6, 9, 5]  # Valores de 1 a 10 para cada característica

# Crear el gráfico de radar
angulos = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False).tolist()

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angulos, valores, color='red', alpha=0.25)
ax.plot(angulos, valores, color='red', linewidth=2)


# Establecer los nombres de las características
ax.set_xticks(angulos)
ax.set_xticklabels(categorias)

plt.show()


# Datos de ejemplo (porcentajes de cada categoría)
categorias = ['A', 'B', 'C', 'D', 'E']
porcentajes = [20, 30, 15, 10, 25]

# Crear el gráfico de queso
plt.figure(figsize=(6, 6))
plt.pie(porcentajes, labels=categorias, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Aspecto igual para que el gráfico sea un círculo

plt.show()