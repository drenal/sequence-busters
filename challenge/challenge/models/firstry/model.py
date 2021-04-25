import torch
import torch.nn as nn
import torch.nn.functional as f

from challenge.base import ModelBase
from challenge.utils import setup_logger


log = setup_logger(__name__)


class firstry(ModelBase):
    def __init__(self, in_features: int):
        """ Simple baseline model for prediction secondary structure
        Args:
               in_features: size in features
         """
        super(firstry, self).__init__()
        
         # Task block

        self.first=nn.Conv1d(in_features,640,kernel_size=2)
        self.second=nn.Conv1d(640,200, kernel_size=2)
        self.third=nn.Conv1d(200,50,kernel_size=2)
        self.fourd=nn.Conv1d(50,20,kernel_size=2)
        self.ss8 = nn.Linear(in_features=20, out_features=8)
        self.ss3 = nn.Linear(in_features=20, out_features=3)

        log.info(f'<init>: \n{self}')

    def forward(self, x: torch.tensor, mask: torch.tensor) -> torch.tensor:
        """ Forwarding logic """
        x=self.first(x)
        x=f.relu(x)
        x=self.second(x)
        x=f.relu(x)
        x=self.third(x)
        x=f.relu(x)
        x=self.fourd(x)
        x=f.relu(x)
        ss8 = self.ss8(x)
        ss3 = self.ss3(x)

        return [ss8, ss3]
