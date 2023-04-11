import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

M = 2.00 #[kg]
A = 0.1 #[m/s]
GRAVITY = 9.80665  #重力加速度
J = M * A**2 / 2  


def getTorque(t): #時刻によるトルク指定
    if(t<1):
        tau = 0.2
    elif(t<4):
        tau = -0.02*t**2
    elif(t<6):
        tau = 0.04*t
    else:
        tau = 0


        
    return tau



#diffeq
def func_motion(t, y): #yは状態ベクトル
    dydt = np.zeros_like(y)

    dydt[0] = y[1]
    dydt[1] = (2 / (M * A + J / A))* getTorque(t)

    return dydt


#2d可視化
def plot2d(t_list, y_list, t_label, y_label):
    plt.xlabel(t_label)  #x軸の名前
    plt.ylabel(y_label)  #y軸の名前
    plt.grid()  #点線の目盛りを表示
    plt.plot(t_list, y_list)

    plt.show()


def plot2dn(fig,ax,t_list, y_list, t_label, y_label):
     ax.plot(t_list, y_list) 
     ax.set_xlabel(t_label)
     ax.set_ylabel(y_label)
     ax.grid()


     # for _ax in ax:







def main():
    
    #solve
    t_span = [0, 8]
    t = np.arange(0, t_span[1], 0.01)
    y0 = [0, 0]
    sol = solve_ivp(func_motion, t_span, y0, t_eval = t)



    #plot
    fig,ax = plt.subplots(nrows=4,ncols=1,figsize=(5,5))


    for i in range(4):
         plot2dn(fig,ax[i],t,sol.y[0,:],"aaaa","bbbb")
        
    fig.tight_layout()
    fig.show()

    pass
    

if(__name__ == "__main__"):
    main()


#plot2d(t,sol.y[0,:],"aaaa","bbbbb")