import matplotlib.pyplot as plt
import numpy as np


# step1 データの作成
xs = []
y1 = []
y2 = []
# step2 グラフフレームの作成
fig, ax = plt.subplots()



while(True):
    # step3 リアルタイムでグラフを更新
    for x in np.linspace(0, 10, 10):
        # 値を更新
        xs.append(x)
        y1.append(4 + 2 * np.sin(2 * x))
        y2.append(4 + 2 * np.cos(2 * x))
        # グラフ描画
        ax.plot(xs, y1, color='C0', linestyle='-')
        ax.plot(xs, y2, color='C1', linestyle='--')

        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        ax.set_xlabel('Time [$sec$]')
        ax.set_ylabel('Frequency [$Hz$]')
        #ax.legend()
        # 0.001秒停止
        plt.pause(0.001)

    ax.remove()