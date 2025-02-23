#!/usr/bin/env python3
"""
File: merchant_integration.py
Description: Implements the MerchantIntegration class that handles merchant registration and tap-to-pay processing.
"""

import time
import json
import logging
import hashlib
from datetime import datetime

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class MerchantIntegration:
    def __init__(self):
        self.registered_merchants = {}

    def register_merchant(self, merchant_name):
        # Register a merchant if not already registered.
        if merchant_name not in self.registered_merchants:
            self.registered_merchants[merchant_name] = {"balance": 0, "transactions": []}
            logging.info("Merchant registered: %s", merchant_name)
        return f"Merchant '{merchant_name}' registered for tap-to-pay system."

    def process_payment(self, user, merchant_name, amount, ai_bot):
        # Process payment if the user exists and has sufficient credits.
        if user not in ai_bot.users:
            logging.error("Payment failed: User %s not found", user)
            return "User not found."
        if ai_bot.users[user]["balance"] < amount:
            logging.error("Payment failed: Insufficient balance for user %s", user)
            return "Insufficient balance."
        ai_bot.users[user]["balance"] -= amount
        self.registered_merchants[merchant_name]["balance"] += amount
        transaction_record = {
            "user": user,
            "amount": amount,
            "timestamp": datetime.now().isoformat(),
            "transaction_id": hashlib.sha256(f"{user}{merchant_name}{time.time()}".encode()).hexdigest()
        }
        self.registered_merchants[merchant_name]["transactions"].append(transaction_record)
        logging.info("Processed payment of %.2f credits from %s to merchant %s", amount, user, merchant_name)
        return f"Payment of {amount:.2f} credits processed to '{merchant_name}'. Remaining balance: {ai_bot.users[user]['balance']:.2f} credits."
