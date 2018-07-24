import torch
import torch.nn as nn
import torchvision.models as models
import torch.nn.functional as F


class EncoderCNN(nn.Module):
    def __init__(self, embed_size):
        super(EncoderCNN, self).__init__()
        resnet = models.resnet50(pretrained=True)
        for param in resnet.parameters():
            param.requires_grad_(False)

        modules = list(resnet.children())[:-1]
        self.resnet = nn.Sequential(*modules)
        self.embed = nn.Linear(resnet.fc.in_features, embed_size)

    def forward(self, images):
        features = self.resnet(images)
        features = features.view(features.size(0), -1)
        features = self.embed(features)
        return features


class DecoderRNN(nn.Module):
    def __init__(self, embed_size, hidden_size, vocab_size, num_layers=3):
        super(DecoderRNN, self).__init__()
        self.embed_size = embed_size
        self.hidden_size = hidden_size
        self.n_layers = num_layers
        self.vocab_size = vocab_size

        self.embed = nn.Embedding(vocab_size, embed_size)
        self.lstm = nn.LSTM(embed_size, hidden_size, num_layers, dropout=0.4, batch_first=True)
        self.linear = nn.Linear(hidden_size, vocab_size)

    # def init_hidden(self, batch_size):
    #     ''' At the start of training, we need to initialize a hidden state;
    #        there will be none because the hidden state is formed based on perviously seen data.
    #        So, this function defines a hidden state with all zeroes and of a specified size.'''
    #     # The axes dimensions are (n_layers, batch_size, hidden_dim)
    #     from torch.autograd import Variable
    #     # return (Variable(torch.zeros(self.n_layers, batch_size, self.hidden_size)),
    #     #         Variable(torch.zeros(self.n_layers, batch_size, self.hidden_size)))
    #     return (Variable(torch.zeros(self.n_layers, batch_size, self.hidden_size)).cuda(),
    #             Variable(torch.zeros(self.n_layers, batch_size, self.hidden_size)).cuda())

    def forward(self, features, captions):
        """Decode image feature vectors and generates captions."""
        # print('caption :', captions.shape)
        embed_caption = self.embed(captions[:, :-1])
        embeddings = torch.cat((features.unsqueeze(1), embed_caption), 1)

        batch_size = features.shape[0]  # the input feature shape is (batch_size,embed_size)
        # print('batch_size:' + str(batch_size))

        outputs, hidden_output = self.lstm(embeddings)
        # print('lstm out shape', outputs.shape)

        # outputs = outputs.contiguous()
        # linear_input = outputs.view(outputs.shape[0] * outputs.shape[1], -1)
        # outputs = self.linear(linear_input)
        # n_steps = embeddings.shape[1]
        # outputs = outputs.view(batch_size, n_steps, -1)
        print('lstm output shape:', outputs.shape)
        outputs = self.linear(outputs)
        # print('revised outputs shape', outputs.shape)
        # outputs = outputs.narrow(1, 1, embeddings.shape[0] - 1)
        # print('narrowed outputs shape', outputs.shape)
        # outputs = F.log_softmax(outputs, dim=1)
        # print('softmax outputs shape', outputs.shape)

        return outputs

    def sample(self, inputs, states=None, max_len=20):
        " accepts pre-processed image tensor (inputs) and returns predicted sentence (list of tensor ids of length max_len) "
        """Generate captions for given image features using greedy search."""
        sampled_ids = []

        for i in range(max_len):
            print('hidden st:', states)
            outputs, states = self.lstm(inputs, states)  # hiddens: (batch_size, 1, hidden_size)
            outputs = self.linear(outputs.squeeze(1))  # outputs:  (batch_size, vocab_size)
            _, predicted = outputs.max(1)  # predicted: (batch_size)
            sampled_ids.append(predicted)
            print('predicted is :', predicted)
            inputs = self.embed(predicted)  # inputs: (batch_size, embed_size)
            # print('after emb:', inputs)
            inputs = inputs.unsqueeze(1)  # inputs: (batch_size, 1, embed_size)

        # sampled_ids = torch.stack(sampled_ids, 1)  # sampled_ids:
        new_list = []
        for each in sampled_ids:
            new_list.append(each.item())
        return new_list
