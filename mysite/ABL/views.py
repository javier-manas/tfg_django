from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from transformers import pipeline
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import numpy as np
from plotly.offline import plot
import re

def mainpage(request):
    
    return render(request, 'ABL/mainpage.html')


def resultados(request):
    if request.method == 'POST':
        frase = request.POST.get('texto')
        categorias = request.POST.getlist('modelo')

        if not frase:  
            messages.error(request, 'Escriba una frase.')
            return render(request, 'ABL/mainpage.html')
        if not categorias: 
            messages.error(request, 'Seleccione al menos una categoría.')
            return render(request, 'ABL/mainpage.html')

        grafico_html_1 = None
        grafico_html_2 = None
        grafico_html_3 = None
        grafico_html_4 = None
        grafico_html_5 = None

        midic={0: 'admiration', 1: 'amusement', 2: 'anger', 3: 'annoyance', 4: 'approval', 5: 'caring', 6: 'confusion', 7: 'curiosity', 8: 'desire', 9: 'disappointment', 10: 'disapproval', 11: 'disgust', 12: 'embarrassment', 13: 'excitement', 14: 'fear', 15: 'gratitude', 16: 'grief', 17: 'joy', 18: 'love', 19: 'nervousness', 20: 'optimism', 21: 'pride', 22: 'realization', 23: 'relief', 24: 'remorse', 25: 'sadness', 26: 'surprise', 27: 'neutral'}
        dicFNST = {0: 'fatherlander', 1: 'nerd', 2: 'spiritualist', 3: 'treehugger'}
        dicABL={0: 'leech', 1: 'bee', 2: 'ant'}
        dicJonathan={0: 'care', 1: 'fairness', 2: 'loyalty', 3: 'authority', 4: 'sanctity',5: 'liberty'}
        dicSchwartz={0: 'selfDirection', 1: 'stimulation', 2: 'power', 3: 'hedonism', 4: 'achievement', 5: 'security', 6: 'conformity', 7: 'tradition', 8: 'benevolence', 9: 'universalism'}

        acumulado_emociones = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        acumulado_abl = [0.0,0.0,0.0]
        acumulado_fnst = [0.0,0.0,0.0,0.0]
        acumulado_Schawrtz = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        acumulado_Jonathan = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]


        frases = re.split(r'[.!?]', frase)
        frases = [frase.strip() for frase in frases if frase.strip()]

        #Grafico 1
        if ("mrovejaxd/FNST_trad_2j" in categorias):
            classifier = pipeline("text-classification",model= "mrovejaxd/FNST_trad_2j", return_all_scores=True)
            for h in range(len(frases)):

                output = classifier(frases[h])

                analizador_ordenado = sorted(output[0], key=lambda x: int(x['label'].split('_')[-1]))

                salida = [item['score'] for item in analizador_ordenado]

                acumulado_fnst = [x + y for x, y in zip(acumulado_fnst, salida)]

            acumulado_fnst =  [x / len(frases) for x in acumulado_fnst]


            categories = list(dicFNST.values())

            values = acumulado_fnst

            fig = go.Figure(data=go.Scatterpolar(r=values, theta=categories, fill='toself'))

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        ticks='',  
                        tickvals=[] 
                    )
                ),
                title='Modelo FNST'
            )

            grafico_html_1 = plot(fig, output_type='div')

        #Grafico 2
        if ("mrovejaxd/ABL_trad_2h" in categorias):
            classifier = pipeline("text-classification",model= "mrovejaxd/ABL_trad_2h", return_all_scores=True)
            for h in range(len(frases)):

                output = classifier(frases[h])

                analizador_ordenado = sorted(output[0], key=lambda x: int(x['label'].split('_')[-1]))

                salida = [item['score'] for item in analizador_ordenado]

                acumulado_abl = [x + y for x, y in zip(acumulado_abl, salida)]

            acumulado_abl =  [x / len(frases) for x in acumulado_abl]


            categories = list(dicABL.values())

            values = acumulado_abl
            

            fig = go.Figure(data=go.Scatterpolar(r=values, theta=categories, fill='toself'))

            fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            ticks='',  
                            tickvals=[]  
                        )
                    ),
                    title='Modelo ABL'
                )
            grafico_html_2 = plot(fig, output_type='div')

        #Grafico 3
        if ("mrovejaxd/goemotions_bertspanish_finetunig_h" in categorias):
            classifier = pipeline("text-classification",model= "mrovejaxd/goemotions_bertspanish_finetunig_h", return_all_scores=True)
            for h in range(len(frases)):

                output = classifier(frases[h])

                analizador_ordenado = sorted(output[0], key=lambda x: int(x['label'].split('_')[-1]))

                salida = [item['score'] for item in analizador_ordenado]

                acumulado_emociones = [x + y for x, y in zip(acumulado_emociones, salida)]

            acumulado_emociones =  [x / len(frases) for x in acumulado_emociones]


            categories = list(midic.values())

            values = acumulado_emociones


            fig = go.Figure(data=go.Scatterpolar(r=values, theta=categories, fill='toself'))

            fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            ticks='',  
                            tickvals=[]  
                        )
                    ),
                    title='Modelo emociones'
                )
            grafico_html_3 = plot(fig, output_type='div')

        #Grafico 3
        if ("mrovejaxd/valores_eticos_Schwartz" in categorias):
            classifier = pipeline("text-classification",model= "mrovejaxd/goemotions_bertspanish_finetunig_d", return_all_scores=True)
            for h in range(len(frases)):

                output = classifier(frases[h])

                analizador_ordenado = sorted(output[0], key=lambda x: int(x['label'].split('_')[-1]))

                salida = [item['score'] for item in analizador_ordenado]

                acumulado_Schawrtz = [x + y for x, y in zip(acumulado_Schawrtz, salida)]

            acumulado_Schawrtz =  [x / len(frases) for x in acumulado_Schawrtz]


            categories = list(dicSchwartz.values())

            Nmedia = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
            media = acumulado_Schawrtz

            Nmedia[0] = (media[6] + media[7] + media[22] + media[0]) / 4
            Nmedia[1] = (media[1] + media[13] + media[7] + media[26]) / 4
            Nmedia[2] = (media[2] + media[11]) / 2
            Nmedia[3] = (media[8] + media[1] + media[13]) / 3
            Nmedia[4] = (media[9] + media[8] + media[2] + media[16] + media[17] + media[21] + media[25] + media[0]) / 8
            Nmedia[5] = (media[14] + media[3] + media[19] + media[23] + media[25]) / 5
            Nmedia[6] = (media[3] + media[4] + media[12] + media[10] + media[24]) / 5
            Nmedia[7] = (media[4] + media[10] + media[9] + media[18] + media[14] + media[21] + media[12]) / 7
            Nmedia[8] = (media[5] + media[15] + media[18] + media[0]) / 4
            Nmedia[9] = (media[0] + media[15] + media[5] + media[20] + media[22]) / 5

            values = Nmedia


            fig = go.Figure(data=go.Scatterpolar(r=values, theta=categories, fill='toself'))

            fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            ticks='',  
                            tickvals=[]  
                        )
                    ),
                    title='Modelo Schwartz'
                )
            grafico_html_4 = plot(fig, output_type='div')

        #Grafico 3
        if ("mrovejaxd/valores_eticos_Jonathan" in categorias):
            classifier = pipeline("text-classification",model= "mrovejaxd/goemotions_bertspanish_finetunig_d", return_all_scores=True)
            for h in range(len(frases)):

                output = classifier(frases[h])

                analizador_ordenado = sorted(output[0], key=lambda x: int(x['label'].split('_')[-1]))

                salida = [item['score'] for item in analizador_ordenado]

                acumulado_Jonathan = [x + y for x, y in zip(acumulado_Jonathan, salida)]

            acumulado_Jonathan =  [x / len(frases) for x in acumulado_Jonathan]


            categories = list(dicJonathan.values())

            Nmedia = [0.0,0.0,0.0,0.0,0.0,0.0]
            media = acumulado_Jonathan

            Nmedia[0] = (media[0] + media[4] + media[8] + media[5] + media[15] + media[17] + media[18] + media[23] + media[20] + media[25]) / 10
            Nmedia[1] = (media[3] + media[4] + media[10] + media[6]) / 4
            Nmedia[2] = (media[0] + media[5] + media[15] + media[17] + media[18] + media[21] + media[24] ) / 7
            Nmedia[3] = (media[2] + media[10] + media[11] + media[21] + media[26]) / 5
            Nmedia[4] = (media[17] + media[18] + media[21] + media[23] + media[24] + media[9]) / 6
            Nmedia[5] = (media[2] + media[8] + media[17] + media[23] + media[20] + media[10] ) / 6
            

            values = Nmedia

            fig = go.Figure(data=go.Scatterpolar(r=values, theta=categories, fill='toself'))

            fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            ticks='',  
                            tickvals=[]  
                        )
                    ),
                    title='Modelo Jonathan'
                )
            grafico_html_5 = plot(fig, output_type='div')


        if 'mrovejaxd/FNST_trad_2j' in categorias:
            aux = categorias.index('mrovejaxd/FNST_trad_2j')
            categorias[aux] = 'FNST'
        if 'mrovejaxd/ABL_trad_2h' in categorias:
            aux = categorias.index('mrovejaxd/ABL_trad_2h')
            categorias[aux] = 'ABL'
        if 'mrovejaxd/goemotions_bertspanish_finetunig_d' in categorias:
            aux = categorias.index('mrovejaxd/goemotions_bertspanish_finetunig_d')
            categorias[aux] = 'Emociones'
        if 'mrovejaxd/valores_eticos_Schwartz' in categorias:
            aux = categorias.index('mrovejaxd/valores_eticos_Schwartz')
            categorias[aux] = 'Schwartz'
        if 'mrovejaxd/valores_eticos_Jonathan' in categorias:
            aux = categorias.index('mrovejaxd/valores_eticos_Jonathan')
            categorias[aux] = 'Jonathan'

        return render(request, 'ABL/resultados.html', {'frase': frase, 'categorias': categorias,  'graficos': [grafico_html_1, grafico_html_2, grafico_html_3, grafico_html_4, grafico_html_5]})
    return redirect('mainpage')




