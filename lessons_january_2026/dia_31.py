"""
PROJECT: Python Learning Journey
AUTHOR: Jefferson
DESCRIPTION: A collection of scripts demonstrating basic Python concepts 
(OOP, Loops, Lists, Conditionals) applied to real-world logic.
"""

import time # Imported for the countdown effect

# ==========================================
# 1. OOP (Object Oriented Programming)
# ==========================================
class Hustler:
    """
    Represents a disciplined worker building their future.
    """
    def __init__(self, name):
        self.name = name
        self.energy = 100
    
    def work(self):
        print(f"🚀 {self.name} is building the future...")
        self.energy -= 10
        print(f"   Energy left: {self.energy}")

# Simulation
hustlers_count = 0

if hustlers_count == 0:
    print("\n--- 1. OOP Simulation ---")
    print("No Hustler found. Creating one now...")
    new_hustler = Hustler("Jefferson")
    new_hustler.work()


# ==========================================
# 2. LISTS & MATH (Earnings Calculator)
# ==========================================
print("\n--- 2. Earnings Calculator ---")

deliveries = [10, 15, 5, 20] # List of values
target = 100

total_earnings = sum(deliveries)
print(f"Total earnings so far: €{total_earnings}")

if total_earnings >= target:
    print("✅ Target hit! Go rest.")
else:
    remaining = target - total_earnings
    print(f"❌ Not yet. €{remaining} left to hit the target.")


# ==========================================
# 3. CONDITIONALS (Speed Limit)
# ==========================================
print("\n--- 3. Speed Check ---")

# Using a fixed value for demonstration (instead of input)
speed = 85 

if speed > 80:
    print(f"Speed: {speed}km/h -> 🚓 TICKETED!")
else:
    print(f"Speed: {speed}km/h -> Safe travels.")


# ==========================================
# 4. WHILE LOOPS (Countdown)
# ==========================================
print("\n--- 4. Countdown ---")

countdown = 5
while countdown > 0:
    print(countdown)
    time.sleep(0.5) # Adds a small delay for realism
    countdown -= 1    

print("🚀 LIFTOFF!")


# ==========================================
# 5. ACCUMULATORS (Savings Logic)
# ==========================================
print("\n--- 5. Savings Accumulator ---")

safe = 0
deposit = 100
month = 0

while month < 3:
    safe += deposit
    month += 1
    print(f"Month {month}: Safe balance is now €{safe}")


# ==========================================
# 6. LOGIC GATES (Elevator Weight Limit)
# ==========================================
print("\n--- 6. Elevator Logic ---")

current_weight = 0
box_weight = 50
limit = 500

while current_weight < limit:
    current_weight += box_weight
    # Only print every 100kg to keep log clean
    if current_weight % 100 == 0: 
        print(f"Loading... Current weight: {current_weight}kg")

print(f"⚠️ Limit reached: {current_weight}kg")


# ==========================================
# 7. BUDGET CONTROL (Spending Limit)
# ==========================================
print("\n--- 7. Budget Control ---")

total_spent = 0
budget_limit = 100
# Simulating inputs for the script
prices_to_add = [30, 50, 40] 

for price in prices_to_add:
    if total_spent + price > budget_limit:
        print(f"❌ Purchase of €{price} denied! Insufficient funds.")
    else:
        total_spent += price
        print(f"✅ Added €{price}. Total: €{total_spent}")

print("End of transaction.")


# ==========================================
# 8. INTERACTIVE LISTS (Task Manager)
# ==========================================
print("\n--- 8. Task Manager (Simulation) ---")

tasks = []
# Simulating user input
user_inputs = ["Study Python", "Deliver Orders", "Fix CV", "end"]

for action in user_inputs:
    if action == "end":
        break
    else:
        tasks.append(action)
        print(f"➕ Added: {action}")

print("\n📝 --- Daily Tasks ---")
for task in tasks:
    print(f"- {task}")