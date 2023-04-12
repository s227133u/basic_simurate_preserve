import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#keyboad_debug
import keyboard


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
        dydt[1] = (2 / (M * A + J / A))* getTorque(t) + (2*GRAVITY/(3*A)) *np.sin(FHI) #坂による力
    elif(y[0] > X_P):
        dydt[1] = (2 / (M * A + J / A))* getTorque(t) - (2*GRAVITY/(3*A)) *np.sin(FHI)
    else:
        dydt[1] = (2 / (M * A + J / A))* getTorque(t)

    return dydt