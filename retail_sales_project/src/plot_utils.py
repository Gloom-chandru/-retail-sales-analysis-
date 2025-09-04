import matplotlib.pyplot as plt
import seaborn as sns

def save_and_show_plot(fig, filename):
    fig.savefig(f'assets/charts/{filename}', bbox_inches='tight')
    plt.show()