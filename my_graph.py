#moderu
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#keyboad_debug
import keyboard




#unko
fig_g,ax_g = plt.subplots(nrows=4,ncols=1,figsize=(5,5))


#plot graph
def plot2dn(t_list_list, y_list_list, t_label_list, y_label_list):

     i=0
     for axg in ax_g:
        #ax_g[i].cla() #本来はpltだった
        ax_g[i].plot(t_list_list[i], y_list_list[i]) 
        aaa=t_list_list[i]
        ax_g[i].set_xlabel(t_label_list[i])
        ax_g[i].set_ylabel(y_label_list[i])
        ax_g[i].grid()
        i = i+1