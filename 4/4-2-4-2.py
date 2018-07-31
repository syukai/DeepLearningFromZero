import numpy as np

# y,tは2次元配列を受け取りまとめて計算。(4-2-2では1次元配列)
# tがone_hot表現ではなく正解ラベルの場合の実装
def cross_entropy_error(y, t):
    if y.ndim == 1:
        #1次元配列が来たら2次元配列に変換
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    
    batch_size = y.shape[0]

    #yから正解ラベルの位置だけ取り出して計算する
    return -np.sum(t * np.log(y[np.arange(batch_size), t])) / batch_size

