#!/usr/bin/env python3
"""
File: blockchain_integration.py
Description: Implements a simple blockchain ledger for recording transactions securely.
"""

import time
import json
import hashlib
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class BlockchainIntegration:
    def __init__(self):
        self.blockchain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = {
            "index": 0,
            "timestamp": time.time(),
            "transactions": [],
            "previous_hash": "0",
            "hash": ""
        }
        genesis_block["hash"] = self.hash_block(genesis_block)
        self.blockchain.append(genesis_block)
        logging.info("Genesis block created.")

    def hash_block(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_transaction(self, transaction):
        new_block = {
            "index": len(self.blockchain),
            "timestamp": time.time(),
            "transactions": [transaction],
            "previous_hash": self.blockchain[-1]["hash"],
            "hash": ""
        }
