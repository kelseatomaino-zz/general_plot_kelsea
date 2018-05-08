import matplotlib.pyplot as plt

def make_box_plot(data, label, title):
    #raw_data = [81.5823249817,75.4757449627,75.6831839085,75.5024600029,75.5057520866,75.6040329933,75.6440458298,75.4538609982]

    fig1, ax1 = plt.subplots()
    ax1.set_title(title)
    ax1.boxplot(data)
    ax1.set_xticklabels(label, rotation=45, fontsize=8)
    plt.show()