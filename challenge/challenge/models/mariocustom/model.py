import torch
import torch.nn as nn
import torch.nn.functional as f

from challenge.base import ModelBase
from challenge.utils import setup_logger


log = setup_logger(__name__)
class Mariocustom(ModelBase):
    def __init__(self, in_features: int):
        """ Simple baseline model for prediction secondary structure
        Args:
            in_features: size in features
        """
        super(Mariocustom, self).__init__()

        self.L0 = nn.Conv1d(in_channels=in_features, out_channels=32, kernel_size=9, padding=4, padding_mode='circular')
        self.N0 = nn.ReLU()
        #self.MP0 = nn.MaxPool1d(kernel_size=9, padding=4)
        self.L1 = nn.Conv1d(in_channels=32, out_channels=64, kernel_size=9, padding=4, padding_mode='circular')
        self.N1 = nn.ReLU()
        #self.MP1 = nn.MaxPool1d(kernel_size=9, padding=4)
        self.ss8 = nn.Linear(64,8)
        self.ss3 = nn.Linear(64,3)
        
        log.info(f'<init>: \n{self}')

    def forward(self, x: torch.tensor, mask: torch.tensor) -> torch.tensor:
        """ Forwarding logic """

        ss8 = self.L0(x.permute(0,2,1))
        #ss8 = self.N0(ss8)
        #ss8 = self.MP0(ss8)
        #print(ss8.size())
        ss8 = self.L1(ss8)
        #ss8 = self.N1(ss8)
        #ss8 = self.MP1(ss8)
        #print(ss8.size())
        # permute back to original dimensions
        ss3 = self.ss3(ss8.permute(0,2,1))
        ss8 = self.ss8(ss8.permute(0,2,1))

        return [ss8, ss3]
