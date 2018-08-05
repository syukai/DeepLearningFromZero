import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from TwoLayerNet import TwoLayerNet
import matplotlib.pylab as plt

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True,one_hot_label=True)

#ハイパーパラメータ
iters_num = 3
train_size = x_train.shape[0]
batch_size = 10
learning_rate = 0.1

train_loss_list=[]
train_acc_list=[]
test_acc_list=[]
# 1エポックあたりの繰り返し数
iter_per_epoch = max(t_train.shape[0] / batch_size, 1)
epoch_num = 0

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

for i in range(iters_num):
    print("i="+str(i))
    #ミニバッチ
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    print("numerical_gradient start")
    grad = network.numerical_gradient(x_batch, t_batch)
    print("numerical_gradient end")

    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]
    
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        epoch_num += 1
        print("train acc, test acc | " + str(train_acc) + ", " + str(test_acc))

#plt.plot(np.arange(0,iters_num), train_loss_list)
plt.plot(np.arange(0, epoch_num), train_acc, label="train_acc")
plt.plot(np.arange(0, epoch_num), test_acc, linestyle = "--", label="test_acc")
plt.show()
