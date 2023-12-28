from dataclasses import dataclass, field
from typing import Dict

@dataclass
class CoinNode:
    name : str
    visited : bool = False
    #exchangeVal : float = 0 # increase in value
    pathsTo : set = None # set of lists to describe each path to node
    exchangeRates : Dict[str, float] = field(default_factory=dict)