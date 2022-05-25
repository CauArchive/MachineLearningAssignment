import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pandas.core.indexes import interval


def show_graph():
    def animate(i):
        data = pd.read_csv('./data4.csv')
        x = data['x_value']
        y1 = data['total_1']
        y2 = data['total_2']

        plt.cla()
        plt.plot(x, y1, label='blog')
        plt.plot(x, y2, label='youtube')

        plt.legend(loc='upper left')

    anim = FuncAnimation(plt.gcf(), animate, interval=1000)
    plt.show()
    return anim


anim = show_graph()
