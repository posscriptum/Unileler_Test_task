from app import app
import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from app import UnileverData as Ul
import numpy as np
import matplotlib.pyplot as plt

"""Вывод графиков на страничку"""
@app.route('/')
@app.route('/index')
def plot_png():

    x1 = np.arange(100, 200)
    temp_range = []
    for item in Ul.arrayUnilever:
        temp_range.append(item.randomValue)
    gistogram_array = []
    for item1 in range(100, 200):
        gistogram_array.append(temp_range.count(item1))
    y1 = np.array(gistogram_array)

    data_array = []
    for item2 in Ul.arrayUnilever:
        data_array.append(item2.date)
    x2 = np.array(data_array)
    y2 = np.array(temp_range)

    fig, axes = plt.subplots(2, 1)

    axes[1].bar(x1, y1)
    axes[0].plot(x2, y2)

    axes[1].set_facecolor('seashell')
    axes[0].set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)
    fig.set_figheight(12)

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
