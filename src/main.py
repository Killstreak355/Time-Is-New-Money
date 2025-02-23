# User authentication and task management demonstration.
print(ai_bot.authenticate_user("Alice"))
print(ai_bot.start_task("Alice", "Community Service", "Food Drive"))
time.sleep(5)  # Simulate task duration
print(ai_bot.stop_task("Alice"))

# Merchant registration and tap-to-pay demonstration.
print(merchant_system.register_merchant("EcoStore"))
tap_payment_result = tap_to_pay.initiate_tap_payment("Alice", "EcoStore", 10)
print(tap_payment_result)

# Display the blockchain ledger for transparency.
print("Blockchain Ledger:")
for block in blockchain_system.get_blockchain():
    print(block)
