import numpy as np
import matplotlib.patches as patches
import matplotlib.collections as collections  
import matplotlib.pyplot as plt



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




#animation
global xd_a
xd_a=0
fig_a = plt.figure(figsize=WINDOW_SIZE)
ax_a = fig_a.add_subplot()





def plotDisk(x_d): #円盤プロット

    #config
    ax_a.cla() #本来はpltだった
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

    plt.pause(0.00001)
