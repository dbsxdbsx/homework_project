# Image Caption

This is a homework project aiming to do "Image Caption" with encoder-decoder mechanism. Deep learning module `Pytorch` is used. For the idea behind the strucure, please refer to paper: [Show and Tell: A Neural Image Caption Generator](https://arxiv.org/pdf/1411.4555.pdf)



## Download Dataset

1. Download some specific data from here:  [Microsoft COCO Dataset](http://cocodataset.org/#download)

- Under **Annotations**, download:
  - **2014 Train/Val annotations [241MB]** (extract captions_train2014.json and captions_val2014.json, and place at locations cocoapi/annotations/captions_train2014.json and cocoapi/annotations/captions_val2014.json, respectively)  
  - **2014 Testing Image info [1MB]** (extract image_info_test2014.json and place at location cocoapi/annotations/image_info_test2014.json)
- Under **Images**, download:
  - **2014 Train images [83K/13GB]** (extract the train2014 folder and place at location cocoapi/images/train2014/)
  - **2014 Val images [41K/6GB]** (extract the val2014 folder and place at location cocoapi/images/val2014/)
  - **2014 Test images [41K/6GB]** (extract the test2014 folder and place at location cocoapi/images/test2014/)



## Documents 

There are 4 notebooks here, they are:

- 0_Dataset.ipynb --- This is used to be familiar with [Microsoft COCO Dataset](http://cocodataset.org/#download). As the Dataset is required here but too big, around 27GB. Please download it manually according to the Download Section. 
- 1_Preliminaries.ipynb --- This is used to be familiar with data structure taken in  this project with pytorch. And the model used in this book is defined in `model.py` I wrote.
- 2_Training.ipynb --- If everything is fine with the 1st 2 books,  the model could be trained with this book.
- 2_Training.ipynb --- With a trained model, this book is used to do inference finally.



## Some Thought

In this project, I struggled with the shape of every input and output of the model at first. And I did refer to some open source code. And I found there is a more easy way to implement with `Pytorch`, but for the aim of understanding LSTM, also the aim of this project, I choose the difficult one to implement.

One thing I found interesting is that when I have not trained the model enough, the prediction of every image are all the same, is that a common issue for RNN?

In addition, I notice  that `crossentropy` is taken as a loss function here like that using in classical CNN classification problem. And I know there is another loss function called "warpctc". I wonder when  I do need warpctc instead of crossentropy. 