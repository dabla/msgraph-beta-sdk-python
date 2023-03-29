from enum import Enum

class VpnTrafficDirection(Enum):
    # The rule applies to all outbound traffic.
    Outbound = "outbound",
    # The rule applies to all inbound traffic.
    Inbound = "inbound",
    # Evolvable enum member
    UnknownFutureValue = "unknownFutureValue",

