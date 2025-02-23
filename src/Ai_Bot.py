#!/usr/bin/env python3
"""

File: Ai_Bot.py
Description: Implements the AIBot class that manages user authentication,
activity tracking, and credit calculation.
"""

import time
import json
import random
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S') 


class AIBot:
  def __init__(self):
    self.users = {} # Store user data
    self.activities = self.generate_activities() # Load activity catalog

  def generate_activities(self):
    # Four categories with 18 activities each for a rich user experience.
    categories = (
      "Community Service": [
    "Food Drive", "Elderly Assistance", "Public Cleaning", "Animal Shelter Help",
                "Disaster Relief", "Street Beautification", "Teaching Underprivileged Kids",
                "Library Organization", "Public Park Maintenance", "Homeless Outreach",
                "Blood Donation", "Beach Cleanup", "Hospital Assistance", "Mental Health Support",
                "Community Gardening", "Recycling Drives", "Public Mural Painting", "School Volunteer"
            ],
            "Education & Mentorship": [
                "Tutoring Math", "Teaching Languages", "Coding Mentorship", "Financial Literacy Coaching",
                "Music Lessons", "Public Speaking Training", "History Lectures", "Writing Workshops",
                "Debate Coaching", "STEM Education", "Scholarship Assistance", "Resume Writing Help",
                "Internship Placement", "Book Club Leadership", "After School Programs", "Virtual Classroom Assistance",
                "Adult Education", "Career Counseling"
            ],
            "Environmental Work": [
                "Tree Planting", "Water Conservation", "Wildlife Protection", "Sustainable Farming",
                "River Cleanup", "Renewable Energy Advocacy", "Urban Gardening", "Recycling Management",
                "Air Pollution Research", "Carbon Footprint Reduction", "Organic Farming Education",
                "Zero-Waste Lifestyle Coaching", "Plastic Free Campaigns", "Energy Efficiency Workshops",
                "Composting Training", "Solar Panel Installation Assistance", "Eco-Tourism Development", "Wildfire Prevention"
            ],
            "Self-Improvement": [
                "Meditation Practice", "Daily Exercise", "Yoga Coaching", "Journaling Habits",
                "Reading Challenge", "Mindfulness Training", "Nutritional Guidance", "Skill Development",
                "Language Learning", "Public Speaking Practice", "Leadership Training", "Time Management Mastery",
                "Productivity Coaching", "Confidence Building", "Personal Finance Training", "Networking Skills",
                "Healthy Cooking", "Mental Resilience Training"
            ]
        }
        logging.debug("Activities generated: %s", json.dumps(categories, indent=2))
        return categories

    def authenticate_user(self, user):
        # Register new users or authenticate existing ones.
        if user not in self.users:
            self.users[user] = {"balance": 0, "current_task": None, "start_time": None, "activity_log": []}
            logging.info("New user registered: %s", user)
        else:
            logging.info("User authenticated: %s", user)
        return f"Welcome, {user}! You have {self.users[user]['balance']:.2f} credits."

    def start_task(self, user, category, task):
        # Start a task if valid.
        if category not in self.activities or task not in self.activities[category]:
            logging.warning("Invalid task selection for user %s: %s in %s", user, task, category)
            return "Invalid task selection. Choose from available activities."
        self.users[user]["current_task"] = {"category": category, "task": task}
        self.users[user]["start_time"] = time.time()
        logging.info("%s started task '%s' in category '%s'", user, task, category)
        return f"{user} started '{task}' in '{category}' at {time.ctime(self.users[user]['start_time'])}"

    def stop_task(self, user):
        # Stop the current task and calculate earned credits.
        if not self.users[user]["current_task"]:
            logging.error("Stop task requested by %s without an active task", user)
            return "No active task found."
        elapsed_time = time.time() - self.users[user]["start_time"]
        rate = random.randint(5, 20)  # Dynamic rate per minute
        earned_credits = elapsed_time / 60 * rate
        self.users[user]["balance"] += earned_credits
        completed_task = self.users[user]["current_task"]
        log_entry = {
            "task": completed_task["task"],
            "category": completed_task["category"],
            "duration_seconds": elapsed_time,
            "earned_credits": earned_credits,
            "timestamp": datetime.now().isoformat()
        }
        self.users[user]["activity_log"].append(log_entry)
        self.users[user]["current_task"] = None
        self.users[user]["start_time"] = None
        logging.info("%s completed task '%s' and earned %.2f credits", user, completed_task["task"], earned_credits)
        return f"{user} earned {earned_credits:.2f} credits for '{completed_task['task']}'. Total balance: {self.users[user]['balance']:.2f} credits."
