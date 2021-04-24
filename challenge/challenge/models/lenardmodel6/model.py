import torch
import torch.nn as nn
import torch.nn.functional as f

from challenge.base import ModelBase
from challenge.utils import setup_logger

log = setup_logger(__name__)


class LenardModel6(ModelBase):
    def __init__(self, in_features: int):
        """ Simple baseline model for prediction secondary structure
        Args:
            in_features: size in features
        """
        super(LenardModel6, self).__init__()

        # Task block

        # setup LSTM to match output from conv1d
        self.input_dim = 128
        
        # Conv1d 1280 -> 64 with kernel_size of 9, because literature says there are around 10 AA in a helix
        # padding 4 required so that we keep sequence length constant (1632)
        # padding mode circular because why not, maybe something else would be better?
        self.L0 = nn.Conv1d(in_channels=in_features, out_channels=self.input_dim, kernel_size=9, padding=4, padding_mode='circular')
        self.N0 = nn.ReLU()

        # maybe inserting a second conv1d layer in-between?
        #self.L1 = nn.Conv1d(in_channels=128, out_channels=self.input_dim, kernel_size=9, padding=4, padding_mode='circular')
        #self.N1 = nn.ReLU()


        # just a guess
        self.hidden_dim = 512
        # if bidirectional=True, this should be 2
        bidir = False
        if bidir:
            self.n_layers = 2
        else:
            self.n_layers = 1

        # batch_first, because we have (batch_size, seq, feature)
        # but because of conv1d we permuted it to (batch_size, seq, feature) --> don't forget to permute in forward() again
        self.L2 = nn.LSTM(input_size=self.input_dim, hidden_size=self.hidden_dim, num_layers=self.n_layers, batch_first=True, bidirectional=bidir)
        self.N2 = nn.ReLU()

        #self.L3 = nn.LSTM(input_size=self.hidden_dim, hidden_size=self.hidden_dim, num_layers=self.n_layers, batch_first=True, bidirectional=bidir)
        #self.N3 = nn.ReLU()

        # FC to Q8 and Q3
        self.ss8 = nn.Linear(self.hidden_dim * self.n_layers, 8)
        self.ss3 = nn.Linear(self.hidden_dim * self.n_layers, 3)
        
        log.info(f'<init>: \n{self}')

    def forward(self, x: torch.tensor, mask: torch.tensor) -> torch.tensor:
        """ Forwarding logic """

        # apply layer0 and permute input tensor to be compatible with conv1d
        ss8 = self.L0(x.permute(0,2,1))
        ss8 = self.N0(ss8)

        #ss8 = self.L1(ss8)
        #ss8 = self.N1(ss8)

        # batch_size may change dynamically, so always compute
        batch_size = ss8.size()[0]

        # create hidden states for the LSMT
        # if not on cuda, remove the ".to("cuda") part
        hidden_state = torch.randn(self.n_layers * self.n_layers, batch_size, self.hidden_dim)#.to("cuda")
        cell_state = torch.randn(self.n_layers * self.n_layers, batch_size, self.hidden_dim)#.to("cuda")
        hidden = (hidden_state, cell_state)
        
        # apply LSTM layer
        ss8, hidden = self.L2(ss8.permute(0,2,1), hidden)
        ss8 = self.N2(ss8)

        #hidden_state2 = torch.randn(self.n_layers * self.n_layers, batch_size, self.hidden_dim)#.to("cuda")
        #cell_state2 = torch.randn(self.n_layers * self.n_layers, batch_size, self.hidden_dim)#.to("cuda")
        #hidden2 = (hidden_state2, cell_state2)
        
        #ss8, hidden2 = self.L3(ss8, hidden2)
        #ss8 = self.N3(ss8)

        # now the ss8 has good dimensions, we don't need pemrute
        ss3 = self.ss3(ss8)
        ss8 = self.ss8(ss8)

        return [ss8, ss3]
