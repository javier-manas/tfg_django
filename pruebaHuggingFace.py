import re
import numpy as np
from transformers import pipeline

dicFNST={0: 'fatherlander', 1: 'nerd', 2: 'spiritualist', 3: 'treehugger'}
frase = "fatherlander fatherlander"





FNSTclassifier = pipeline("text-classification",model= "mrovejaxd/FNST_b", return_all_scores=True)
FNSTanalizador = FNSTclassifier(frase)

inner_list = FNSTanalizador[0]

# Obtener los valores de 'score' de los diccionarios en la lista interna
values = [item['score'] for item in inner_list]

# Imprimir los valores
print(values)
print("")
print(FNSTanalizador)