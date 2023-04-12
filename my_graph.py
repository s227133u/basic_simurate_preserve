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


     for axg in ax_g:
        i = 0
        axg.cla() #本来はpltだった
        axg.plot(t_list_list[i], y_list_list[i]) 
        axg.set_xlabel(t_label_list[i])
        axg.set_ylabel(y_label_list[i])
        axg.grid()
        i = i+1