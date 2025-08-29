import matplotlib.pyplot as plt
from logerForDiagramma import logger
import pandas as pd


class Grafic:
    def __init__(self, cards):
        self.cards = cards 
        
    @logger
    def diagramma(self):
        df = pd.read_csv(self.cards)
        count = df.iloc[:, 5].value_counts()
        label = count.index
        size = count.values
        colors = ['lightgreen', 'blue', 'silver']
        plt.pie(size, labels = label, colors = colors, autopct = '%1.1f%%', startangle = 140)
        plt.axis('equal')
        plt.show()

    def __del__(self):
        print(" ")