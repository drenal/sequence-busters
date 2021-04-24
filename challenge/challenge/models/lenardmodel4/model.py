import torch
import torch.nn as nn
import torch.nn.functional as f

from challenge.base import ModelBase
from challenge.utils import setup_logger

log = setup_logger(__name__)


class LenardModel4(ModelBase):
    def __init__(self, in_features: int):
        """ Simple baseline model for prediction secondary structure
        Args:
            in_features: size in features
        """
        super(LenardModel4, self).__init__()

        # Task block
        self.L0 = nn.Linear(in_features, 512)
        self.N0 = nn.ReLU()
        self.L1 = nn.Linear(512, 256)
        self.N1 = nn.ReLU()
        self.L2 = nn.Linear(256, 128)
        self.N2 = nn.ReLU()
        self.ss8 = nn.Linear(128,8)
        self.ss3 = nn.Linear(128,3)
        
        log.info(f'<init>: \n{self}')

    def forward(self, x: torch.tensor, mask: torch.tensor) -> torch.tensor:
        """ Forwarding logic """

        ss8 = self.L0(x)
        ss8 = self.N0(ss8)
        ss8 = self.L1(ss8)
        #ss8 = self.N1(ss8)
        ss8 = self.L2(ss8)
        #ss8 = self.N2(ss8)

        ss3 = self.ss3(ss8)
        ss8 = self.ss8(ss8)

        return [ss8, ss3]
