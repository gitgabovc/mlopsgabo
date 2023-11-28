import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ast
sns.set()

import pandas as pd


def cantidadNulos(df, columnas_adicionales=None):    
    # Calcular porcentaje de nulos y no nulos para cada columna
    porcentaje_nulos = df.isnull().mean() * 100
    porcentaje_no_nulos = 100 - porcentaje_nulos

    # Filtrar por las columnas adicionales si se proporcionan
    if columnas_adicionales:
        porcentaje_nulos = porcentaje_nulos[columnas_adicionales]
        porcentaje_no_nulos = porcentaje_no_nulos[columnas_adicionales]

    # Crear un gráfico de barras agrupadas
    fig, ax = plt.subplots(figsize=(10, 6))

    bar_width = 0.35
    index = np.arange(len(porcentaje_nulos))

    # Gráfico de barras
    bar1 = ax.bar(index, porcentaje_nulos, bar_width, label='Nulos', color='red', alpha=0.7)
    bar2 = ax.bar(index + bar_width, porcentaje_no_nulos, bar_width, label='No Nulos', color='green', alpha=0.7)

    # Etiquetas y título para el gráfico de barras
    ax.set_xlabel('Columnas')
    ax.set_ylabel('Porcentaje')
    ax.set_title('Porcentaje de Nulos y No Nulos por Columna')

    # Rotar las etiquetas del eje x diagonalmente
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(porcentaje_nulos.index, rotation=45, ha='right')

    # Agregar etiquetas con los porcentajes en cada barra
    for bar, label in zip(bar1, porcentaje_nulos):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 1,
                f'{label:.2f}%', ha='center', va='bottom', color='red')

    for bar, label in zip(bar2, porcentaje_no_nulos):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 1,
                f'{label:.2f}%', ha='center', va='bottom', color='green')

    ax.legend()

    # Mostrar el gráfico
    plt.show()
    
def contar_nans_en_columna(df, nombre_columna):
    # Contar la cantidad de valores NaN en la columna específica
    cantidad_nans = df[nombre_columna].isna().sum()

    return cantidad_nans
