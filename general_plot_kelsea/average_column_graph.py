import matplotlib.pyplot as plt
import numpy as np


def make_column_chart():
    number_of_data_sets = int(input("Enter number of data sets: "))
    averages = []
    labels = []
    title = str(input("Enter title: "))
    x_label = str(input("Enter x axis title: "))
    y_label = str(input("Enter y axis title: "))

    for i in range(0, number_of_data_sets):
        data = input("Enter data set: ")
        label = str(input("Enter data label: "))
        averages.append(_compute_average(data))
        labels.append(label)

    y_pos = np.arange(len(averages))
    plt.bar(y_pos, averages, align='center', alpha=0.5)
    plt.xticks(y_pos, labels)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def _compute_average(data):
    total = 0
    average = 0
    for i in range(0, len(data)):
        total += data[i]

    average = total / len(data)
    return average
