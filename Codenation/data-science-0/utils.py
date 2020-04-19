import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# <=========================================================================================================================>  
# <============================================ DATA EXPLORATION ==========================================================> 
# <==========================================================================================================================>



#================================================ trim_axs ==========================================================
def trim_axs(axs, N):
    '''   This function takes the an axes list, the number of plots and sets  the axes list with correct length
    
    ARG: 
    axs(array like): array with axes 
    N(integer): number of graphs to be plotted 
    
    RETURS:
    axs(array like): array with correct number of axes to be plotted
    '''

    axs = axs.flatten()
    for ax in axs[N:]:
        ax.remove()
    return axs[:N]



#================================================ individual_bar_plot ==========================================================

def individual_bar_plot(df, col,  ax = None):
    '''
    Bar plot for each column
    
    
    ARG:
    df(daraframe): dataframe to be parsed 
    col(string): name of the column
        
    
    '''

    obj = dataframe.loc[col,:]  # Select item

    obj.plot( kind = 'barh',
            color = color,
            edgecolor = 'black', 
            ax = ax,   
            legend = None,              
            ).set_title(f'{title} {col}')
    
    ax.set_xlabel('Purchase Mean [$]')
    
