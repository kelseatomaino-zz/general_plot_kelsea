import matplotlib.pyplot as plt

def make_multiple_box_plot():
    number_of_data_sets = input("Enter number_of_data_sets: ")
    data = []
    data_labels = []
    title = input("Enter title: ")
    logs = input("Enter 1 for log scale and 0 for not log scale: ")
    for i in range(0, number_of_data_sets):
        data_set = input("Enter data: ")
        data_label = input("Enter data label: ")
        data_labels.append(data_label)
        data.append(data_set)

    fig2, ax2 = plt.subplots()
    ax2.set_title('Multiple Sample Box Plot')
    ax2.boxplot(data)
    ax2.set_title(title)
    ax2.set_xticklabels(data_labels, rotation=45, fontsize=8)
    if(logs == 1):
        plt.yscale('logit')
    plt.show()
