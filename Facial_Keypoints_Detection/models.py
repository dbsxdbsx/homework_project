## TODO: define the convolutional neural network architecture

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs

        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel

        # the input image size should be  224x224px
        self.conv1 = nn.Conv2d(1, 32, 4)
        self.conv2 = nn.Conv2d(32, 64, 3)
        self.conv3 = nn.Conv2d(64, 128, 2)
        self.conv4 = nn.Conv2d(128, 256, 1)

        self.maxpool1 = nn.MaxPool2d(2, 2)
        self.maxpool2 = nn.MaxPool2d(2, 2)
        self.maxpool3 = nn.MaxPool2d(2, 2)
        self.maxpool4 = nn.MaxPool2d(2, 2)

        self.dropout1 = nn.Dropout2d(p=0.1)
        self.dropout2 = nn.Dropout2d(p=0.2)
        self.dropout3 = nn.Dropout2d(p=0.3)
        self.dropout4 = nn.Dropout2d(p=0.4)
        self.dropout5 = nn.Dropout(p=0.5)
        self.dropout6 = nn.Dropout(p=0.6)

        self.dense1 = nn.Linear(43264, 1000)
        self.dense2 = nn.Linear(1000, 1000)
        self.dense3 = nn.Linear(1000, 136)
        #
        # for m in self.modules():
        #     # print(m)
        #     weight_init(m)
        #     # torch.nn.init.kaiming_uniform_(m.weight.data, a=0, mode='fan_in')
        #     # nn.init.xavier_normal_()

        # n_size = self._get_conv_output(input_shape)
        # self.fc1 = nn.Linear(320, 50)
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting

    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        x = self.dropout1(self.maxpool1(F.relu(self.conv1(x))))
        x = self.dropout2(self.maxpool2(F.relu(self.conv2(x))))
        x = self.dropout3(self.maxpool3(F.relu(self.conv3(x))))
        x = self.dropout4(self.maxpool4(F.relu(self.conv4(x))))
        x = x.view(x.size(0), -1)

        x = self.dropout5(F.relu(self.dense1(x)))
        x = self.dropout6(F.relu(self.dense2(x)))
        # x = F.relu(self.dense3(x))
        x = self.dense3(x)
        # a modified x, having gone through all the layers of your model, should be returned
        return x

# import math
#
#
# def weight_init(m):
#     if isinstance(m, nn.Conv2d):
#         n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
#         m.weight.data.normal_(0, math.sqrt(2. / n))
#     elif isinstance(m, nn.BatchNorm2d):
#         m.weight.data.fill_(1)
#         m.bias.data.zero_()
