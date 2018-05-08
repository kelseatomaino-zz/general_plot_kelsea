import matplotlib.pyplot as plt

def make_multiple_box_plot():
    number_of_data_sets = input("Enter number_of_data_sets: ")
    data = []
    for i in range(0, number_of_data_sets):
        data_set = input("Enter data: ")
        data.append(data_set)

    fig2, ax2 = plt.subplots()
    ax2.set_title('Multiple Sample Box Plot')
    ax2.boxplot(data)
    plt.show()
