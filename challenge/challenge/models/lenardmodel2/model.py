import torch
import torch.nn as nn
import torch.nn.functional as f

from challenge.base import ModelBase
from challenge.utils import setup_logger

log = setup_logger(__name__)


class LenardModel2(ModelBase):
    def __init__(self, in1_features: int, in2_features: int):
        """ Simple baseline model for prediction secondary structure
        Args:
            in_features: size in features
        """
        super(LenardModel2, self).__init__()

        # Task block
        self.ss8_in = nn.Bilinear(in1_features=in1_features, in2_features=in2_features, out_features=512)
        self.ss8_1 = nn.Linear(in_features=512, out_features=256)
        self.ss8_2 = nn.Linear(in_features=256, out_features=128)
        self.ss8_3 = nn.Linear(in_features=128, out_features=64)
        self.ss8_out = nn.Linear(in_features=64, out_features=8)

        self.ss3_in = nn.Bilinear(in1_features=in1_features, in2_features=in2_features, out_features=256)
        self.ss3_1 = nn.Linear(in_features=256, out_features=128)
        self.ss3_2 = nn.Linear(in_features=128, out_features=64)
        self.ss3_out = nn.Linear(in_features=64, out_features=3)

        log.info(f'<init>: \n{self}')

    def forward(self, x: torch.tensor, mask: torch.tensor) -> torch.tensor:
        """ Forwarding logic """

        ss8 = f.relu(self.ss8_in(x[:, :, :20], x[:, :, 20:]))
        ss3 = f.relu(self.ss3_in(x[:, :, :20], x[:, :, 20:]))

        ss8 = f.relu(self.ss8_1(ss8))
        ss8 = f.relu(self.ss8_2(ss8))
        ss8 = f.relu(self.ss8_3(ss8))
        ss8 = self.ss8_out(ss8)

        ss3 = f.relu(self.ss3_1(ss3))
        ss3 = f.relu(self.ss3_2(ss3))
        ss3 = self.ss3_out(ss3)

        return [ss8, ss3]
