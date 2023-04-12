import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.collections as collections  

import keyboard

#constant
WINDOW_SIZE = (8,4)
X0Y0 = (0,0)
x0 = X0Y0[0] #WINDOW_SIZE[1] /2
y0 = X0Y0[1]
angle = np.pi * 1/6 #[rad]
CIR_X = 0.6
CIR_Y = 0.3 #hankei
REC_WIDTH = 2
REC_HEIGHT = 1
ROT_LENGTH = 1.8


def plotPemdulum(ax,x0,angle): #倒立振子プロット
    plt.cla()
    plt.ion()


    ax.set_xlim(-WINDOW_SIZE[0] * 1/2,WINDOW_SIZE[0] * 1/2)
    ax.set_ylim(0,WINDOW_SIZE[1])

    ax.set_title("zukei simulate")

    #zukei
    cir1 = patches.Circle(xy=(x0-CIR_X, y0+CIR_Y), radius=CIR_Y,fc="w" ,ec='k')
    cir2 = patches.Circle(xy=(x0+CIR_X, y0+CIR_Y), radius=CIR_Y,fc="w" ,ec='k')
    rect = patches.Rectangle(xy=(x0 - 1/2*REC_WIDTH,y0+2*CIR_Y),width=REC_WIDTH,height=REC_HEIGHT,fc="w" ,ec='k')

    #Cir3
    cir3X = x0+(CIR_Y + ROT_LENGTH)* np.sin(angle)
    cir3Y = y0 + 2*CIR_Y + REC_HEIGHT + (CIR_Y + ROT_LENGTH)*np.cos(angle)
    cir3 = patches.Circle(xy=(cir3X, cir3Y), radius=CIR_Y,fc="w" ,ec='k')


    #rot
    rotX0 = x0
    rotY0 = y0+2*CIR_Y+REC_HEIGHT
    rotX1 = x0+(CIR_Y + ROT_LENGTH)* np.sin(angle)                          #x0+ROT_LENGTH*np.sin(angle)
    rotY1 = y0 + 2*CIR_Y + REC_HEIGHT + (CIR_Y + ROT_LENGTH)*np.cos(angle)  #y0 + 2*CIR_Y + REC_HEIGHT + ROT_LENGTH*np.cos(angle)
    rot = [(rotX0,rotY0),(rotX1,rotY1)]
   
    #plot
    ax.add_patch(cir1)
    ax.add_patch(cir2)
    ax.add_patch(cir3)
    ax.add_patch(rect)
    collection=collections.LineCollection([rot],color=["black"])
    ax.add_collection(collection)


    plt.pause(0.01)



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
    global x0,angle
    x0=0
    angle=0
    fig = plt.figure(figsize=WINDOW_SIZE)
    ax = fig.add_subplot()
 

    while True:
        Key = scanKeyBoard()
        if Key == 1.0:
            x0 = x0 + 0.1
        if Key == -1.0:
            x0 = x0 - 0.1
        if Key == 2:
            angle = angle + np.pi * 1/24
        if Key == -2:
            angle = angle - np.pi * 1/24

        plotPemdulum(ax,x0,angle)



    

if __name__ == "__main__":
    main()


