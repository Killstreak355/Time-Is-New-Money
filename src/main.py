#!/usr/bin/env python3
import time

# --- Feature 1: Authentication and Task Management with Task History ---
class AIBot:
    def __init__(self):
        # Store a history of tasks for each user.
        self.task_history = {}  # {username: [task_record, ...]}
        self.current_tasks = {}  # {username: task_record}
    
    def authenticate_user(self, username):
        # Simulate authentication logic.
        return f"User {username} authenticated successfully via AIBot."
    
    def start_task(self, username, task_category, task_name):
        start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        task_record = {
            "task_category": task_category,
            "task_name": task_name,
            "start_time": start_time,
            "end_time": None,
            "status": "In Progress"
        }
        # Save current task and append to history.
        self.current_tasks[username] = task_record
        if username not in self.task_history:
            self.task_history[username] = []
        self.task_history[username].append(task_record)
        return f"Task '{task_name}' in category '{task_category}' started for {username} at {start_time}."
    
    def stop_task(self, username):
        if username in self.current_tasks:
            end_time = time.strftime("%Y-%m-%d %H:%M:%S")
            self.current_tasks[username]["end_time"] = end_time
            self.current_tasks[username]["status"] = "Completed"
            task_name = self.current_tasks[username]["task_name"]
            del self.current_tasks[username]
            return f"Task '{task_name}' stopped for {username} at {end_time}."
        else:
            return f"No active task found for {username}."
    
    def view_task_history(self, username):
        if username in self.task_history and self.task_history[username]:
            history = f"Task History for {username}:\n"
            for idx, task in enumerate(self.task_history[username], start=1):
                history += (f"{idx}. {task['task_name']} ({task['task_category']}) - "
                            f"Started: {task['start_time']}, Ended: {task['end_time'] or 'Ongoing'}, "
                            f"Status: {task['status']}\n")
            return history
        else:
            return f"No task history found for {username}."

# --- Feature 2: Merchant Registration ---
class MerchantSystem:
    def __init__(self):
        self.registered_merchants = []
    
    def register_merchant(self, merchant_name):
        if merchant_name in self.registered_merchants:
            return f"Merchant '{merchant_name}' is already registered."
        self.registered_merchants.append(merchant_name)
        return f"Merchant '{merchant_name}' registered successfully."

# --- Feature 3: Tap-to-Pay with Payment History ---
class TapToPay:
    def __init__(self):
        self.payment_history = []  # List of payment records
    
    def initiate_tap_payment(self, user, merchant, amount):
        payment_time = time.strftime("%Y-%m-%d %H:%M:%S")
        payment_record = {
            "user": user,
            "merchant": merchant,
            "amount": amount,
            "time": payment_time,
            "status": "Success"
        }
        self.payment_history.append(payment_record)
        return f"Tap payment of ${amount} initiated from {user} to {merchant} at {payment_time}."
    
    def view_payment_history(self, user):
        history = f"Payment History for {user}:\n"
        found = False
        for record in self.payment_history:
            if record["user"] == user:
                history += (f"- ${record['amount']} to {record['merchant']} on {record['time']} "
                            f"(Status: {record['status']})\n")
                found = True
        if not found:
            history += "No payments found."
        return history

# --- Feature 4: Blockchain Ledger for Transparency ---
class BlockchainSystem:
    def __init__(self):
        self.chain = ["Block 1: Genesis Block"]
    
    def get_blockchain(self):
        return self.chain
    
    def add_block(self, data):
        block_number = len(self.chain) + 1
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        block = f"Block {block_number}: {data} at {timestamp}"
        self.chain.append(block)
        return block

# --- Feature 5: Notification System ---
class NotificationSystem:
    def __init__(self):
        self.notifications = []
    
    def add_notification(self, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        notification = f"{timestamp} - {message}"
        self.notifications.append(notification)
    
    def view_notifications(self):
        if self.notifications:
            return "\n".join(self.notifications)
        else:
            return "No notifications at this time."

# --- Feature 6: Report Generator ---
class ReportGenerator:
    def generate_report(self, ai_bot, tap_to_pay):
        report = "=== System Report ===\n"
        # Report for tasks.
        total_tasks = sum(len(tasks) for tasks in ai_bot.task_history.values())
        report += f"Total tasks performed: {total_tasks}\n"
        # Report for payments.
        total_payments = len(tap_to_pay.payment_history)
        total_amount = sum(record["amount"] for record in tap_to_pay.payment_history)
        report += f"Total payments made: {total_payments} | Total amount: ${total_amount}\n"
        return report

# --- Feature 7: User Account Management ---
class UserAccountManager:
    def __init__(self):
        self.accounts = {}
        self.logged_in_user = None
        # Create a default admin account.
        self.accounts["admin"] = {"password": "admin123", "email": "admin@example.com", "balance": 0.0}
    
    def register_user(self, username, password, email):
        if username in self.accounts:
            return f"Username '{username}' is already registered."
        self.accounts[username] = {"password": password, "email": email, "balance": 0.0}
        return f"User '{username}' registered successfully."
    
    def login(self, username, password):
        if username not in self.accounts:
            return "Username not found."
        if self.accounts[username]["password"] != password:
            return "Incorrect password."
        self.logged_in_user = username
        return f"User '{username}' logged in successfully."
    
    def logout(self):
        if self.logged_in_user is None:
            return "No user is currently logged in."
        user = self.logged_in_user
        self.logged_in_user = None
        return f"User '{user}' logged out successfully."
    
    def view_balance(self):
        if self.logged_in_user is None:
            return "No user is logged in."
        balance = self.accounts[self.logged_in_user]["balance"]
        return f"User '{self.logged_in_user}' balance: ${balance:.2f}"
    
    def update_email(self, new_email):
        if self.logged_in_user is None:
            return "No user is logged in."
        old_email = self.accounts[self.logged_in_user]["email"]
        self.accounts[self.logged_in_user]["email"] = new_email
        return f"Email updated for '{self.logged_in_user}': from {old_email} to {new_email}."
    
    def admin_credit(self, target_username, amount):
        if self.logged_in_user != "admin":
            return "Only admin can credit user accounts."
        if target_username not in self.accounts:
            return f"User '{target_username}' not found."
        self.accounts[target_username]["balance"] += amount
        return f"Credited ${amount:.2f} to '{target_username}'. New balance: ${self.accounts[target_username]['balance']:.2f}"

# --- Main Application with Interactive Menu ---
def main():
    # Instantiate all systems.
    account_manager = UserAccountManager()
    ai_bot = AIBot()
    merchant_system = MerchantSystem()
    tap_to_pay = TapToPay()
    blockchain_system = BlockchainSystem()
    notifications = NotificationSystem()
    report_generator = ReportGenerator()
    
    while True:
        print("\n=== Main Menu ===")
        print("1. Register New User")
        print("2. Login")
        print("3. Logout")
        print("4. View Balance")
        print("5. Update Email")
        print("6. AIBot: Authenticate User")
        print("7. Start Task")
        print("8. Stop Task")
        print("9. View Task History")
        print("10. Register Merchant")
        print("11. Initiate Tap Payment")
        print("12. View Payment History")
        print("13. View Blockchain Ledger")
        print("14. View Notifications")
        print("15. Generate Reports")
        print("16. Admin Credit (Admin Only)")
        print("17. Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            username = input("Enter new username: ").strip()
            password = input("Enter new password: ").strip()
            email = input("Enter email: ").strip()
            result = account_manager.register_user(username, password, email)
            print(result)
            notifications.add_notification(result)
        
        elif choice == "2":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            result = account_manager.login(username, password)
            print(result)
            notifications.add_notification(result)
        
        elif choice == "3":
            result = account_manager.logout()
            print(result)
            notifications.add_notification(result)
        
        elif choice == "4":
            result = account_manager.view_balance()
            print(result)
        
        elif choice == "5":
            new_email = input("Enter new email: ").strip()
            result = account_manager.update_email(new_email)
            print(result)
            notifications.add_notification(result)
        
        elif choice == "6":
            username = input("Enter username for AIBot authentication: ").strip()
            result = ai_bot.authenticate_user(username)
            print(result)
            notifications.add_notification(result)
        
        elif choice == "7":
            username = input("Enter your username for task start: ").strip()
            task_category = input("Enter task category: ").strip()
            task_name = input("Enter task name: ").strip()
            result = ai_bot.start_task(username, task_category, task_name)
            print(result)
            blockchain_system.add_block(f"Task '{task_name}' started by {username}")
            notifications.add_notification(result)
        
        elif choice == "8":
            username = input("Enter your username for task stop: ").strip()
            result = ai_bot.stop_task(username)
            print(result)
            blockchain_system.add_block(f"Task stopped by {username}")
            notifications.add_notification(result)
        
        elif choice == "9":
            username = input("Enter username to view task history: ").strip()
            print(ai_bot.view_task_history(username))
        
        elif choice == "10":
            merchant_name = input("Enter merchant name to register: ").strip()
            result = merchant_system.register_merchant(merchant_name)
            print(result)
            blockchain_system.add_block(f"Merchant '{merchant_name}' registered")
            notifications.add_notification(result)
        
        elif choice == "11":
            user = input("Enter username for tap payment: ").strip()
            merchant = input("Enter merchant name: ").strip()
            try:
                amount = float(input("Enter payment amount: ").strip())
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            result = tap_to_pay.initiate_tap_payment(user, merchant, amount)
            print(result)
            blockchain_system.add_block(f"Payment of ${amount} from {user} to {merchant}")
            notifications.add_notification(result)
        
        elif choice == "12":
            user = input("Enter username to view payment history: ").strip()
            print(tap_to_pay.view_payment_history(user))
        
        elif choice == "13":
            print("Blockchain Ledger:")
            for block in blockchain_system.get_blockchain():
                print(block)
        
        elif choice == "14":
            print("Notifications:")
            print(notifications.view_notifications())
        
        elif choice == "15":
            print(report_generator.generate_report(ai_bot, tap_to_pay))
        
        elif choice == "16":
            target_username = input("Enter username to credit: ").strip()
            try:
                amount = float(input("Enter credit amount: ").strip())
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            result = account_manager.admin_credit(target_username, amount)
            print(result)
            blockchain_system.add_block(f"Admin credited ${amount} to {target_username}")
            notifications.add_notification(result)
        
        elif choice == "17":
            print("Exiting application. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")
        
        time.sleep(1)

if __name__ == '__main__':
    main()
