import sys, os
sys.path.append(os.pardir) #親ディレクトリを参照先に追加
from dataset.mnist import load_mnist
import numpy as np
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


(x_train, t_train), (x_test, t_test) =load_mnist(flatten=True, normalize=False)

img = x_train[0]
label=t_train[0]
print(label)        # 5

print(img.shape)    # 28*28をflattenしているので(784, )
img = img.reshape(28, 28)   #1次元配列にflattenしていたものを28*28の2次元配列に戻す
print(img.shape)    # (28, 28)
img_show(img)   #画像表示

