import torch
import torch.nn as nn
import torch.nn.functional as F

from challenge.base import ModelBase
from challenge.utils import setup_logger

log = setup_logger(__name__)


class Chris(ModelBase):
    def __init__(self, in_features: int):
        """ Simple baseline model for prediction secondary structure
        Args:
            in_features: size in features
        """
        super(Chris, self).__init__()

        # Task block
        self.conv1 = nn.Conv1d(in_features, 100, 24)
        self.conv2 = nn.Conv1d(100, 200, 24)
        self.lstm_1 = nn.LSTM(200, 1024, num_layers=2, bidirectional=True)
        self.lstm_2 = nn.LSTM(1024, 1024, num_layers=2, bidirectional=True)
        self.ss8_fc = nn.Linear(2048, 8)

        self.ss3_conv1 = nn.Conv1d(in_features, 100, 24)
        self.ss3_conv2 = nn.Conv1d(100, 200, 24)
        self.ss3_lstm_1 = nn.LSTM(200, 1024, num_layers=2, bidirectional=True)
        self.ss3_lstm_2 = nn.LSTM(1024, 1024, num_layers=2, bidirectional=True)
        self.ss3_fc = nn.Linear(2048, 3)

        log.info(f'<init>: \n{self}')

    def forward(self, x: torch.tensor, mask: torch.tensor) -> torch.tensor:
        """ Forwarding logic """

        ss8_x = F.relu(self.conv1(x))
        ss8_x = F.max_pool2d(ss8_x, kernel_size=2, stride=2)

        ss8_x = F.relu(self.conv2(ss8_x))
        ss8_x = F.max_pool2d(ss8_x, kernel_size=2, stride=2)

        ss8_x = F.relu(self.lstm_1(ss8_x))
        ss8_x = F.relu(self.lstm_2(ss8_x))

        ss8 = self.ss8_fc(ss8_x)

        ss3_x = F.relu(self.ss3_conv1(x))
        ss3_x = F.max_pool2d(ss3_x, kernel_size=2, stride=2)

        ss3_x = F.relu(self.ss3_conv2(ss3_x))
        ss3_x = F.max_pool2d(ss3_x, kernel_size=2, stride=2)

        ss3_x = F.relu(self.lstm_1(ss3_x))
        ss3_x = F.relu(self.lstm_2(ss3_x))
        ss3 = self.ss3_fc(ss3_x)

        return [ss8, ss3]
