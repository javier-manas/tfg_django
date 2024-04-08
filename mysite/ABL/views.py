from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from transformers import pipeline
import matplotlib.pyplot as plt
import plotly.graph_objs as go



def mainpage(request):
   
    return render(request, 'ABL/mainpage.html')


def resultados(request):
    if request.method == 'POST':
        frase = request.POST.get('texto')
        categorias = request.POST.getlist('modelo')

        # Datos para el gráfico
        x = [0, 1, 2, 3, 4, 5]
        y = [0, 1, 4, 9, 16, 25]

        # Crear el gráfico
        fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers', marker=dict(color='blue')))
        fig.update_layout(title='Gráfico de ejemplo', xaxis_title='X', yaxis_title='Y')

        # Convertir el gráfico a formato HTML
        grafico_html = fig.to_html(full_html=False)

        if not frase:  
            messages.error(request, 'Escriba una frase.')
            return render(request, 'ABL/mainpage.html')
        if not categorias: 
            messages.error(request, 'Seleccione al menos una categoría.')
            return render(request, 'ABL/mainpage.html')
        
        #summarizer = pipeline("text-classification",model= "mrovejaxd/goemotions_bertspanish_finetunig_f", return_all_scores=True)
        #resultado = summarizer(frase)
        resultado = 'no consegui que funcione' 


        return render(request, 'ABL/resultados.html', {'frase': frase, 'categorias': categorias, 'resultado': resultado, 'grafico_html': grafico_html})
    return redirect('mainpage')




