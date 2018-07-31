import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape)
print(t_train.shape)

train_size = x_train.shape[0]   # 60,000
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)   # 60,000からランダムに10個抽出
print("batch_mask")
print(batch_mask)

