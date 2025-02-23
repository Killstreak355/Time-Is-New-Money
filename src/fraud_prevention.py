#!/usr/bin/env python3
"""
File: fraud_prevention.py
Description: Implements the FraudPrevention class that verifies user activities and enforces strict withdrawal rules.
"""

import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class FraudPrevention:
    def __init__(self):
        self.verification_logs = {}

    def verify_user_activity(self, user, ai_bot):
        # Verify that the user has an active task.
        if user not in ai_bot.users or not ai_bot.users[user]["current_task"]:
            logging.warning("Verification failed for user %s: No active task", user)
            return "User verification failed: No active task."
        self.verification_logs[user] = datetime.now().isoformat()
        logging.info("User %s verified successfully.", user)
        return "User verified successfully."

    def enforce_strict_withdrawal(self, user, ai_bot):
        # Enforce a minimum balance threshold for withdrawals.
        if ai_bot.users[user]["balance"] < 10:
            logging.warning("Withdrawal denied for user %s: Balance below minimum threshold", user)
            return "Withdrawal denied: Minimum balance required."
        logging.info("Withdrawal approved for user %s.", user)
        return "Withdrawal approved. Credits can be used."
