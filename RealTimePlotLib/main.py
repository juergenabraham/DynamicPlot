# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def live():

    from queue import Queue
    import RealTimePlotLib
    import numpy as np
    import time

    queue = Queue()

    size = 100
    counter = 0
    x_vec = np.linspace(0, size, size+1)[0:-1]
    y_vec = np.random.randn(len(x_vec))
    line1 = list()
    images = list()

    # ploter = RealTimePlotLib.LivePlotter("Test me")
    # ploter.set_label("x Achse", "y Achse")
    # while True:


    # ploter.plot(0, 1)

    import numpy as np

    while True:
        rand_val = np.random.randn(1)
        y_vec[-1] = rand_val
        line1 = RealTimePlotLib.live_plotter(x_vec, y_vec, line1, title="Drehzahl", y_label="Umdrehungen", x_label="sec")
    #    images.append(line1.save_img("testFile"))
        y_vec = np.append(y_vec[1:], 0.0)
        x_vec = np.linspace(counter, size + counter, size + 1)[0:-1]
        counter += 1
### # See PyCharm help at https://www.jetbrains.com/help/pycharm/
from tkinter import *
from random import randint

# these two imports are important
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import threading

continuePlotting = False


def change_state():
    global continuePlotting
    if continuePlotting == True:
        continuePlotting = False
    else:
        continuePlotting = True


def data_points():
    f = open("data.txt", "w")
    for i in range(10):
        f.write(str(randint(0, 10)) + '\n')
    f.close()

    f = open("data.txt", "r")
    data = f.readlines()
    f.close()

    l = []
    for i in range(len(data)):
        l.append(int(data[i].rstrip("\n")))
    return l


def app():
    # initialise a window.
    root = Tk()
    root.config(background='white')
    root.geometry("1000x700")

    lab = Label(root, text="Live Plotting", bg='white').pack()

    fig = Figure()

    ax = fig.add_subplot(111)
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.grid()

    graph = FigureCanvasTkAgg(fig, master=root)
    graph.get_tk_widget().pack(side="top", fill='both', expand=True)

    def plotter():
        while continuePlotting:
            ax.cla()
            ax.grid()
            dpts = data_points()
            ax.plot(range(10), dpts, marker='o', color='orange')
            graph.draw()
            time.sleep(1)

    def gui_handler():
        change_state()
        threading.Thread(target=plotter).start()

    b = Button(root, text="Start/Stop", command=gui_handler, bg="red", fg="white")
    b.pack()

    root.mainloop()

if __name__ == '__main__':
    app()
#    live()
