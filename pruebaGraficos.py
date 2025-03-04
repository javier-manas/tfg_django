import numpy as np
import matplotlib.pyplot as plt

'''
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

#plt.show()


# Datos de ejemplo (porcentajes de cada categoría)
categorias = ['A', 'B', 'C', 'D', 'E']
porcentajes = [20, 30, 15, 10, 25]

# Crear el gráfico de queso
plt.figure(figsize=(6, 6))
plt.pie(porcentajes, labels=categorias, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Aspecto igual para que el gráfico sea un círculo

#plt.show()


#-------------------------------------------------------------------------------------------


output = [{'label': 'LABEL_0', 'score': 0.87593626528978348},
          {'label': 'LABEL_1', 'score': 0.04073619842529297},
          {'label': 'LABEL_2', 'score': 0.0009410174679942429},
          {'label': 'LABEL_3', 'score': 0.1823865652084351}]

dicFNST = {0: 'fatherlander', 1: 'nerd', 2: 'spiritualist', 3: 'treehugger'}

categories = list(dicFNST.values())
values = [item['score'] for item in output]

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()

fig, ax = plt.subplots(figsize=(5,5), subplot_kw=dict(polar=True))

ax.fill(angles, values, color='blue', alpha=0.25)
ax.plot(angles, values, color='blue', linewidth=2)

ax.set_xticks(angles)
ax.set_yticklabels([])
ax.set_xticklabels(categories)
for i, label in enumerate(ax.get_xticklabels()):
    angle_rad = angles[i]  
    angle_deg = np.degrees(angle_rad) 
    label.set_text(categories[i])  
    label.set_fontsize(10)  
    if angle_deg < 90 :
        label.set_horizontalalignment('left')  
    elif angle_deg == 180:
        label.set_horizontalalignment('right')  
    else:
        label.set_horizontalalignment('center') 

plt.show()

'''