from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.series import Series

df = pd.read_csv('Lista de Pasajeros del Titanic.csv', sep=';')

def query_ticket(ticket_id:str) -> DataFrame:
    filtered_data = df[df['Ticket']==ticket_id]
    print(filtered_data)
    return filtered_data

def get_survivors_data() -> Series:
    filtered_data = df.groupby(by='Sobrevivió')['Sobrevivió']
    survivors_summary = filtered_data.count()
    survivors_summary = survivors_summary.sort_values(ascending=True) # Lista primero los sobrevivientes
    survivors_summary.index = ['Sobrevivientes', 'Fallecidos']
    return survivors_summary

def plot_survivors_data() -> None:
    survivors_color = 'green'
    deceaseds_color = 'red'
    survivors_summary = get_survivors_data()
    print(survivors_summary)
    survivors = Patch(color=survivors_color, label=survivors_summary.index[0])
    deceaseds = Patch(color=deceaseds_color, label=survivors_summary.index[1])
    plt.pie(survivors_summary, colors=[survivors_color, deceaseds_color] ,autopct='%.2f')
    plt.legend(handles=[survivors, deceaseds], bbox_to_anchor=(0.05, 0.01))
    plt.title('Porcentaje de sobrevivientes y fallecidos')
    plt.show()

    
def menu():
    menu_options = defaultdict(lambda: menu() or 'La opción no está en la lista')
    menu_options['1']='Si'
    menu_options['2']='No'
    print('Elija una opción:', *menu_options.items(), sep='\n')
    x = input()
    print(menu_options[x])
    return



if __name__=='__main__':
    plot_survivors_data()