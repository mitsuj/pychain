"""
This module contains the Block class, which represents a block in the blockchain.
"""

import datetime
import hashlib
from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Block:
    """
    Represents a block in the blockchain.
    """

    index: int
    timestamp: datetime.datetime
    transactions: List
    previous_hash: str
    hash: Optional[str]
    nonce: int

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block.
        """
        block_string = (
            f"{self.index}"
            f"{self.timestamp.isoformat()}"
            f"{str(self.transactions)}"
            f"{self.previous_hash}"
            f"{self.nonce}"
        )
        return hashlib.sha256(block_string.encode()).hexdigest()
