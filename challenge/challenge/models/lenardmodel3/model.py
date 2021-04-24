import torch
import torch.nn as nn
import torch.nn.functional as f

from challenge.base import ModelBase
from challenge.utils import setup_logger

log = setup_logger(__name__)


class LenardModel3(ModelBase):
    def __init__(self, in_features: int):
        """ Simple baseline model for prediction secondary structure
        Args:
            in_features: size in features
        """
        super(LenardModel3, self).__init__()

        # Task block
        # Based on https://pytorch.org/tutorials/beginner/nlp/sequence_models_tutorial.html

        self.ss8_lstm = nn.LSTM(in_features, 64)
        self.ss8_out = nn.Linear(in_features=64, out_features=8)

        self.ss3_lstm = nn.LSTM(in_features, 64)
        self.ss3_out = nn.Linear(in_features=64, out_features=3)

        log.info(f'<init>: \n{self}')

    def forward(self, x: torch.tensor, mask: torch.tensor) -> torch.tensor:
        """ Forwarding logic """

        ss8 = self.ss8_lstm(x[:, :, 20:], (1,) )
        ss3 = self.ss3_lstm(x[:, :, 20:], (1,) )

        ss8 = self.ss8_out(ss8)
        ss3 = self.ss3_out(ss3)

        return [ss8, ss3]
