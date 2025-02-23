# ===== File: src/api_server.py =====
#!/usr/bin/env python3
"""
File: api_server.py
Description: A Flask-based API server that exposes endpoints for the "Time is the New Money" application.
This server integrates the AI bot, merchant tap-to-pay, fraud prevention, and blockchain systems.
"""

from flask import Flask, request, jsonify
from ai_bot import AIBot
from merchant_integration import MerchantIntegration
from fraud_prevention import FraudPrevention
from blockchain_integration import BlockchainIntegration
from tap_to_pay import TapToPayIntegration
import time

# Initialize Flask app
app = Flask(__name__)

# Initialize core systems
ai_bot = AIBot()
merchant_system = MerchantIntegration()
fraud_system = FraudPrevention()
blockchain_system = BlockchainIntegration()
tap_to_pay = TapToPayIntegration(ai_bot, merchant_system, fraud_system, blockchain_system)

# ===== Endpoint: /authenticate =====
# Description: Authenticate or register a user.
@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    user = data.get('user')
    if not user:
        return jsonify({"error": "Missing user parameter"}), 400
    message = ai_bot.authenticate_user(user)
    return jsonify({"message": message, "balance": ai_bot.users[user]['balance']})

# ===== Endpoint: /start_task =====
# Description: Start an activity/task for the user.
@app.route('/start_task', methods=['POST'])
def start_task():
    data = request.get_json()
    user = data.get('user')
    category = data.get('category')
    task = data.get('task')
    if not all([user, category, task]):
        return jsonify({"error": "Missing parameters"}), 400
    message = ai_bot.start_task(user, category, task)
    return jsonify({"message": message})

# ===== Endpoint: /stop_task =====
# Description: Stop the current activity/task and compute earned credits.
@app.route('/stop_task', methods=['POST'])
def stop_task():
    data = request.get_json()
    user = data.get('user')
    if not user:
        return jsonify({"error": "Missing user parameter"}), 400
    message = ai_bot.stop_task(user)
    return jsonify({"message": message, "balance": ai_bot.users[user]['balance']})

# ===== Endpoint: /register_merchant =====
# Description: Register a new merchant for tap-to-pay.
@app.route('/register_merchant', methods=['POST'])
def register_merchant():
    data = request.get_json()
    merchant_name = data.get('merchant_name')
    if not merchant_name:
        return jsonify({"error": "Missing merchant_name parameter"}), 400
    message = merchant_system.register_merchant(merchant_name)
    return jsonify({"message": message})

# ===== Endpoint: /tap_payment =====
# Description: Process a tap-to-pay payment from a user to a merchant.
@app.route('/tap_payment', methods=['POST'])
def tap_payment():
    data = request.get_json()
    user = data.get('user')
    merchant_name = data.get('merchant_name')
    amount = data.get('amount')
    if not all([user, merchant_name, amount]):
        return jsonify({"error": "Missing parameters"}), 400
    try:
        amount = float(amount)
    except ValueError:
        return jsonify({"error": "Amount must be a number"}), 400
    message = tap_to_pay.initiate_tap_payment(user, merchant_name, amount)
    return jsonify({"message": message})

# ===== Endpoint: /blockchain =====
# Description: Retrieve the full blockchain ledger.
@app.route('/blockchain', methods=['GET'])
def blockchain():
    chain = blockchain_system.get_blockchain()
    return jsonify({"blockchain": chain})

# ===== Main entry point to run the API server =====
if __name__ == '__main__':
    # Run Flask app on port 5000 with debugging enabled
    app.run(debug=True, port=5000)
