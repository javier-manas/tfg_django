import re
import numpy as np
from transformers import pipeline

dicFNST={0: 'fatherlander', 1: 'nerd', 2: 'spiritualist', 3: 'treehugger'}
frase = "fatherlander fatherlander"





FNSTclassifier = pipeline("text-classification",model= "mrovejaxd/FNST_b", return_all_scores=True)
FNSTanalizador = FNSTclassifier(frase)

inner_list = FNSTanalizador[0]

classifier = pipeline("text-classification",model= "mrovejaxd/goemotions_bertspanish_finetunig_d", return_all_scores=True)
output = classifier(frase)

midic={0: 'admiration', 1: 'amusement', 2: 'anger', 3: 'annoyance', 4: 'approval', 5: 'caring', 6: 'confusion', 7: 'curiosity', 8: 'desire', 9: 'disappointment', 10: 'disapproval', 11: 'disgust', 12: 'embarrassment', 13: 'excitement', 14: 'fear', 15: 'gratitude', 16: 'grief', 17: 'joy', 18: 'love', 19: 'nervousness', 20: 'optimism', 21: 'pride', 22: 'realization', 23: 'relief', 24: 'remorse', 25: 'sadness', 26: 'surprise', 27: 'neutral'}

categories = list(midic.values())
inner_list = output[0]

values = [item['score'] for item in inner_list]


# Imprimir los valores
print(values)
print("")
print(FNSTanalizador)