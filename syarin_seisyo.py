#jisaku
import my_animation as animation
import my_moderu as moderu
import my_graph as graph

#moderu
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#keyboad_debug
import keyboard

#animation
import matplotlib.patches as patches
import matplotlib.collections as collections  


def main():
    while(True):
        
	#solve diffeq
        t_span = [0, 2]
        t = np.arange(0, t_span[1], 0.01)
        y0 = [3, -5]
        sol = solve_ivp(moderu.func_motion, t_span, y0, t_eval = t)     
        xd_a = sol.y[0,:] #list
        wd_a = sol.y[1,:]
        
        #plot
        t_list = [t,t,t,t]
        y_list = [xd_a,wd_a,xd_a,xd_a]
        y_label = ["Xw","Vw","cccc","dddd"]
        t_label = ["t","t","t","t"]
        graph.plot2dn(t_list_list=t_list,y_list_list=y_list,t_label_list=t_label,y_label_list=y_label)
        
    #loop
        for xd in xd_a:
            pass
            animation.plotDisk(xd)


if(__name__ == "__main__"):
    main()