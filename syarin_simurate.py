import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#keyboad_debug
import keyboard

#animation
import matplotlib.patches as patches
import matplotlib.collections as collections  


#constant
WINDOW_SIZE = (8,4)
CIR_R = 0.3 #hankei
FHI = np.pi /6
X_P = 2 #x_plane
ROT_LENGTH = 2.5
X_MAX = ROT_LENGTH * np.cos(FHI) 
Y_MAX = ROT_LENGTH * np.sin(FHI) 
X_K = 0.0 #x0
Y_K = 0.3 #y0
DISK_OFFSET = 0.02


#buturi-prm
M = 2.00 #[kg]
A = 0.1 #[m]
GRAVITY = 9.80665  #重力加速度
J = M * A**2 / 2  


def getTorque(t): #時刻によるトルク指定
    if(t<1):
        tau = 0
    elif(t<4):
        tau = -0*t**2
    elif(t<6):
        tau = 0*t
    else:
        tau = 0

    return tau



#diffeq
def func_motion(t, y): #yは状態ベクトル
    dydt = np.zeros_like(y)

    dydt[0] = y[1]  #y[0] = x_w
    if(y[0] < -X_P):
        dydt[1] = (2 / (M * A + J / A))* getTorque(t) + (2*GRAVITY/(3*A)) *np.sin(FHI)
    elif(y[0] > X_P):
        dydt[1] = (2 / (M * A + J / A))* getTorque(t) - (2*GRAVITY/(3*A)) *np.sin(FHI)
    else:
        dydt[1] = (2 / (M * A + J / A))* getTorque(t)

    return dydt


#plot graph
def plot2dn(fig,ax_g,t_list_list, y_list_list, t_label_list, y_label_list):

     for axg in ax_g:
        i = 0
        axg.plot(t_list_list[0], y_list_list[0]) 
        axg.set_xlabel(t_label_list[i])
        axg.set_ylabel(y_label_list[i])
        axg.grid()
        i = i+1


         



def plotDisk(ax_a,x_d): #円盤プロット

    #config
    plt.cla()
    plt.ion()
    ax_a.set_xlim(-WINDOW_SIZE[0] * 1/2,WINDOW_SIZE[0] * 1/2)
    ax_a.set_ylim(0,WINDOW_SIZE[1])
    ax_a.set_title("disk simulate")

    #disk
    if(x_d < -X_P):
        y_d = -(x_d + X_P) * np.sin(FHI+0.13) + CIR_R + DISK_OFFSET
    elif(x_d > X_P):
         y_d = (x_d - X_P) * np.sin(FHI+0.13) + CIR_R + DISK_OFFSET
    else :
         y_d = CIR_R 
    disk = patches.Circle(xy=(x_d + X_K, CIR_R + y_d), radius=CIR_R,fc="w" ,ec='k')

    #diplay disk's rad
    disk_rad = (x_d % 2*np.pi*A) /A 
    disk_rot = [(x_d + X_K,CIR_R + y_d),(x_d + X_K + CIR_R*np.sin(disk_rad), CIR_R + y_d + CIR_R*np.cos(disk_rad))]


    #rot
    rot1 = [(-X_MAX -X_P + X_K,Y_K+Y_MAX),(-X_P + X_K, Y_K)]
    rot2 = [(-X_P + X_K,Y_K),(X_P + X_K,Y_K)]
    rot3 = [(X_MAX +X_P + X_K,Y_K+Y_MAX),(X_P + X_K, Y_K)]


   
    #plot
    ax_a.add_patch(disk)
    collection0=collections.LineCollection([disk_rot],color=["red"])
    collection1=collections.LineCollection([rot1,rot2,rot3],color=["black"])
    ax_a.add_collection(collection0)
    ax_a.add_collection(collection1)

    #plt.pause(0.00001)


def scanKeyBoard():
    match keyboard.read_key():
        case "right":
            return 1

        case "left":
            return -1

        case "up":
            return 2

        case "down":
            return -2
         
        case _:
            return 0
        








def main():
    #animation
    global xd_a
    xd_a=0
    fig_a = plt.figure(figsize=WINDOW_SIZE)
    ax_a = fig_a.add_subplot()
    
    while(True):
        
	#solve diffeq
        t_span = [0, 8]
        t = np.arange(0, t_span[1], 0.01)
        y0 = [3, -15]
        sol = solve_ivp(func_motion, t_span, y0, t_eval = t)     
        xd_a = sol.y[0,:] #list
        
        # #plot
        # fig_g,ax_g = plt.subplots(nrows=4,ncols=1,figsize=(5,5))
        # t_list = [t,t,t,t]
        # y_list = [xd_a,xd_a,xd_a,xd_a]
        # y_label = ["aaaa","bbbb","cccc","dddd"]
        # t_label = ["t","t","t","t"]
        # plot2dn(fig_g,ax_g,t_list_list=t_list,y_list_list=y_list,t_label_list=t_label,y_label_list=y_label)
        
	#loop
        for xd in xd_a:
            plotDisk(ax_a,xd)






        # for i in range(4):
        #     plot2dn(fig,ax_a[i],t,sol.y[0,:],"aaaa","bbbb")
            
        # fig.tight_layout()
        # fig.show()

        # pass
            


    #solve

    

if(__name__ == "__main__"):
    main()


#plot2d(t,sol.y[0,:],"aaaa","bbbbb")