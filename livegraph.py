import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
class liveGraphMaker: 
    def __init__(self, data):
        self.data = data
        
    def init_graph(self):
        ax = plt.axes()
        ax.set_facecolor("black")
        plt.subplot(2,3,1)
        hl, = plt.plot([], [])

        plt.subplot(2,3,2)
        hl, = plt.plot([], [])
        plt.subplot(2,3,3)

        plt.subplot(2,3,4)

        plt.subplot(2,3,5)

        plt.subplot(2,3,6)

    def _realtime_graph(data_x, data_y)
    def update_line(hl, new_data):
        hl.set_xdata(np.append(hl.get_xdata(), new_data))
        hl.set_ydata(np.append(hl.get_ydata(), new_data))
        plt.draw()