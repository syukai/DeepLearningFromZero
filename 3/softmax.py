# ソフトマックス関数
# ・inputの大小関係とoutputの大小関係は必ず同じになる
# ・配列でない値を渡すと戻り値は必ず1.0になる
# →分類に使用する際は最大のものを選ぶだけなので省略される
# ・合計は必ず1.0になるので、確率として扱うことができる
import numpy as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c) #オーバーフロー対策
    sum_exp_a = np.sum(exp_a)
    return exp_a / sum_exp_a

