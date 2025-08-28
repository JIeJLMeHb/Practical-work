import matplotlib.pyplot as plt
import pandas as pd
import capsule as caps


class Sonyboys():
    @caps.logging
    def __init__(self, df):
        self.df = pd.DataFrame()
        self.df = df

    @caps.logging
    def diagramm(self):
        country_counts = self.df['country'].value_counts()
        country_counts = country_counts.to_dict()
        dflen = len(self.df)
        countries = country_counts.keys()
        counts = country_counts.values()
        print(counts)
        print(countries)
        sizes = []
        for i in counts:
            x = i / dflen * 100
            sizes.append(x)
        plt.pie(sizes, labels=countries)
        plt.show()

def main():
    df = pd.DataFrame()
    df = pd.read_csv("JIeJLMeHb's/lab3/playstation_players.csv")
    my_df = Sonyboys(df)
    my_df.diagramm()
