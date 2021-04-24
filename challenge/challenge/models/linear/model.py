import torch
import torch.nn as nn
import torch.nn.functional as F

from challenge.base import ModelBase
from challenge.utils import setup_logger

log = setup_logger(__name__)


class Linear(ModelBase):
    def __init__(self, in_features: int):
        """ Simple baseline model for prediction secondary structure
        Args:
            in_features: size in features
        """
        super(Linear, self).__init__()

        # Task block
        self.ss8_in = nn.Linear(in_features=in_features, out_features=64)
        self.ss8_1 = nn.Linear(in_features=64, out_features=64)
        self.ss8_2 = nn.Linear(in_features=64, out_features=64)
        # self.ss8_3 = nn.Linear(in_features=64, out_features=64)
        self.ss8_out = nn.Linear(in_features=64, out_features=8)
        self.ss3_in = nn.Linear(in_features=in_features, out_features=64)
        self.ss3_1 = nn.Linear(in_features=64, out_features=64)
        self.ss3_2 = nn.Linear(in_features=64, out_features=64)
        self.ss3_out = nn.Linear(in_features=64, out_features=3)

        log.info(f'<init>: \n{self}')

    def forward(self, x: torch.tensor, mask: torch.tensor) -> torch.tensor:
        """ Forwarding logic """

        ss8 = F.relu(self.ss8_in(x))
        ss3 = F.relu(self.ss3_in(x))

        ss8 = F.relu(self.ss8_1(ss8))
        ss8 = F.relu(self.ss8_2(ss8))
        # ss8 = F.relu(self.ss8_3(ss8))
        ss8 = self.ss8_out(ss8)

        ss3 = F.relu(self.ss3_1(ss3))
        ss3 = F.relu(self.ss3_2(ss3))
        ss3 = self.ss3_out(ss3)

        return [ss8, ss3]
