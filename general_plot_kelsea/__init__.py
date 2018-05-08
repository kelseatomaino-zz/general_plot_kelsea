import matplotlib.pyplot as plt
import numpy as np


def make_box_plot():
    #raw_data = [81.5823249817,75.4757449627,75.6831839085,75.5024600029,75.5057520866,75.6040329933,75.6440458298,75.4538609982]

    file = input("Enter file name: ")
    with open(file, 'r') as f:
        content = f.readlines()

    for line in content:
        raw_data.append(float(line.strip()))
    fig1, ax1 = plt.subplots()
    ax1.set_title('Basic Plot')
    ax1.boxplot(raw_data)
    plt.show()
