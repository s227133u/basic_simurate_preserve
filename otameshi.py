import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


#2階常微分方程式（運動方程式、自由落下）
def func_motion(var, t):
    gravity = 9.80665  #重力加速度
    dxdt = var[1]
    dvdt = -gravity

    return [dxdt, dvdt]


#2d可視化
def plot2d(t_list, y_list, t_label, y_label):
    plt.xlabel(t_label)  #x軸の名前
    plt.ylabel(y_label)  #y軸の名前
    plt.grid()  #点線の目盛りを表示
    plt.plot(t_list, y_list)

    plt.show()


#メイン実行部
if (__name__ == '__main__'):
    t_list = np.linspace(0.0, 10.0, 1000)

    m_init = [100.0, 0.0]  #高さと速度の初期値
    m_list = odeint(func_motion, m_init, t_list)


    #可視化
    plot2d(t_list, m_list[:, 0], "$t$", "$x(t)$")
    plot2d(t_list, m_list[:, 1], "$t$", "$v(t)$")