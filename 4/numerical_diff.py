# 数値微分
# 微小値を加算・減産して数式を実行し、差分の傾きを取る
def numerical_diff(f, x):
    h = 1e-4 #0.0001
    return(f(x+h) - f(x-h)) / (2*h)
