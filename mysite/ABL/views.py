from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from transformers import pipeline
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import numpy as np
from plotly.offline import plot

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


        #Grafico 1
        if ("mrovejaxd/FNST_b" in categorias):
            classifier = pipeline("text-classification",model= "mrovejaxd/FNST_b", return_all_scores=True)
            output = classifier(frase)

            dicFNST = {0: 'fatherlander', 1: 'nerd', 2: 'spiritualist', 3: 'treehugger'}

            categories = list(dicFNST.values())
            inner_list = output[0]

            values = [item['score'] for item in inner_list]

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
        if ("mrovejaxd/ABL_d" in categorias):
            classifier = pipeline("text-classification",model= "mrovejaxd/ABL_d", return_all_scores=True)
            output = classifier(frase)

            dicABL={0: 'leech', 1: 'bee', 2: 'ant'}

            categories = list(dicABL.values())
            inner_list = output[0]

            values = [item['score'] for item in inner_list]

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
        if ("mrovejaxd/goemotions_bertspanish_finetunig_d" in categorias):
            classifier = pipeline("text-classification",model= "mrovejaxd/goemotions_bertspanish_finetunig_d", return_all_scores=True)
            output = classifier(frase)

            midic={0: 'admiration', 1: 'amusement', 2: 'anger', 3: 'annoyance', 4: 'approval', 5: 'caring', 6: 'confusion', 7: 'curiosity', 8: 'desire', 9: 'disappointment', 10: 'disapproval', 11: 'disgust', 12: 'embarrassment', 13: 'excitement', 14: 'fear', 15: 'gratitude', 16: 'grief', 17: 'joy', 18: 'love', 19: 'nervousness', 20: 'optimism', 21: 'pride', 22: 'realization', 23: 'relief', 24: 'remorse', 25: 'sadness', 26: 'surprise', 27: 'neutral'}

            categories = list(midic.values())
            inner_list = output[0]

            values = [item['score'] for item in inner_list]

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



        return render(request, 'ABL/resultados.html', {'frase': frase, 'categorias': categorias,  'graficos': [grafico_html_1, grafico_html_2, grafico_html_3]})
    return redirect('mainpage')




