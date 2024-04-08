import re
import numpy as np
from transformers import pipeline

a = "mrovejaxd/goemotions_bertspanish_finetunig_a"
lista_frases1 = ["frase numero uno"]

#classifier = pipeline("text-classification",model= a, return_all_scores=True)

#analizador = classifier(lista_frases1[0])

# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("mrovejaxd/FNST_b")
model = AutoModelForSequenceClassification.from_pretrained("mrovejaxd/FNST_b")
analizador = model("frase numero uno")
cadena = str(analizador)
print (cadena)
