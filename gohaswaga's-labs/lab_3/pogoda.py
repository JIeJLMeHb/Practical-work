import pandas as pd
import matplotlib.pyplot as plt

#добавляеться файл с названием pogoda вида: 1 столбик с названием "Месяц", второй столбец с названием "Солнечные дни"
df = pd.read_csv('pogoda.csv')

def create_sunny_days_chart(df):
    fig, ax = plt.subplots(figsize=(12, 8))
    
    bars = ax.barh(df['Месяц'], df['Солнечные дни'], color="#26F1FF", edgecolor='black', linewidth=0.5)

    for i, (month, days) in enumerate(zip(df['Месяц'], df['Солнечные дни'])):
        ax.text(days + 0.3, i, f'{days}', va='center', fontsize=14, fontweight='bold')
    
    ax.set_xlim(0, 35)
    ax.set_xlabel('Количество солнечных дней', fontsize=12, fontweight='bold')
    ax.set_title('КОЛИЧЕСТВО СОЛНЕЧНЫХ ДНЕЙ В ГОДУ', fontsize=16, fontweight='bold', pad=20)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    ax.grid(axis='x', alpha=0.2, linestyle='--')
    ax.set_axisbelow(True)
    
    
    plt.tight_layout()
    return fig, ax

fig, ax = create_sunny_days_chart(df)
plt.show()

print("Статистика по солнечным дням:")
print(f"Всего солнечных дней в году: {df['Солнечные дни'].sum()}")
print(f"Среднее количество дней в месяц: {df['Солнечные дни'].mean():.1f}")
print(f"Максимальное количество: {df['Солнечные дни'].max()} (в {df.loc[df['Солнечные дни'].idxmax(), 'Месяц']})")
print(f"Минимальное количество: {df['Солнечные дни'].min()} (в {df.loc[df['Солнечные дни'].idxmin(), 'Месяц']})")