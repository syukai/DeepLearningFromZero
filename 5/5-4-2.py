"""
加算レイヤと乗算レイヤを使った逆伝播
"""
from MulLayer import MulLayer
from AddLayer import AddLayer

apple = 100
apple_num = 2
orange = 150
orange_num = 3
tax = 1.1

mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()
add_apple_orange_layer = AddLayer()
mul_tax_layer = MulLayer()

# forward
# りんご x  りんごの個数
apple_price = mul_apple_layer.forward(apple, apple_num)
# オレンジ x オレンジの個数
orange_price = mul_orange_layer.forward(orange, orange_num)
# りんご値段 + オレンジ値段
all_price = add_apple_orange_layer.forward(apple_price, orange_price)
# 消費税
price = mul_tax_layer.forward(all_price, tax)

# backward
dprice = 1
dall_price, dtax = mul_tax_layer.backward(dprice)
dapple_price, dorange_price = add_apple_orange_layer.backward(dall_price)
dorange, dorange_num = mul_orange_layer.backward(dorange_price)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print("price=" + str(price))
print("dapple_num="+str(dapple_num))
print("dorange=" + str(dorange))
print("dorange_num=" + str(dorange_num))
print("dtax=" + str(dtax))
