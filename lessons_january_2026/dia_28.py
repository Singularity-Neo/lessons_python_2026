# ==============================================================================
# 📅 DAY 28: FROM LOGIC TO OOP (FULL PORTFOLIO)
# ==============================================================================

# ==============================================================================
# LEVEL 1: BASIC INPUTS & MATH (The Wood Shop)
# ==============================================================================
print("\n--- LEVEL 1: SHOPPING CALCULATOR ---")

# Commented out to avoid blocking execution, uncomment to test
"""
item_name = input("What is the item name? ")
price = float(input("What is the price? "))
quantity = int(input("How many? "))

total_cost = price * quantity
print(f"User bought {quantity} units of {item_name} for ${total_cost:.2f}")
"""

# ==============================================================================
# LEVEL 2: LOOPS & CONDITIONALS (Spy Filter)
# ==============================================================================
print("\n--- LEVEL 2: SECURITY SYSTEM ---")

agent_ids = [102, 33, 45, 88, 12, 99]
spies_captured = 0

for agent_id in agent_ids:
    if agent_id % 2 == 0:
        print(f"ID: {agent_id} -> Access Permitted ✅")
    else:
        print(f"ID: {agent_id} -> Access Denied ❌ (Spy Detected!)")
        spies_captured += 1

print(f"🚨 Total spies captured: {spies_captured}")

# ==============================================================================
# LEVEL 3: LISTS OF DICTIONARIES (Inventory & Wallet)
# ==============================================================================
print("\n--- LEVEL 3: INVENTORY MANAGEMENT ---")

backpack = [
    {"item": "Sword", "weight": 5},
    {"item": "Shield", "weight": 8},
    {"item": "Potion", "weight": 2}
]

total_weight = 0 
for slot in backpack:
    print(f"Carrying: {slot['item']} ({slot['weight']}kg)")  
    total_weight += slot["weight"]

print("-" * 20)
print(f"🏋️ Total Backpack Weight: {total_weight}kg")


print("\n--- WALLET CALCULATOR ---")
wallet = [
    {"bill": 10},
    {"bill": 20},
    {"bill": 50}
]

total_cash = 0
for money in wallet:
    print(f"Counting bill: ${money['bill']}")
    total_cash += money["bill"]
  
print("-" * 20)
print(f"💰 Total Cash: ${total_cash}")

# ==============================================================================
# LEVEL 4: FUNCTIONS (Damage & Elite Filter)
# ==============================================================================
print("\n--- LEVEL 4: GAME LOGIC FUNCTIONS ---")

life = 100
sword_power = 10
has_weapon = True

def calculate_damage(base_life, weapon_bonus):
    base_life -= 15 # Base penalty
    if has_weapon:
        weapon_bonus *= 3
        base_life += weapon_bonus
        print("⚔️ Critical Hit! Damage multiplied by 3.")
    else:
        print("👊 No weapon equipped.")
    return base_life

final_damage = calculate_damage(life, sword_power)
print(f"💥 Final Damage Deal: {final_damage}")


# Elite Soldiers Filter
candidates_scores = [45, 80, 90, 20, 55, 70]

def filter_elite(scores):
    approved = []
    for score in scores:
        if score >= 70:
            approved.append(score)
    return approved

elite_squad = filter_elite(candidates_scores)
print(f"🎖️ Elite Soldiers: {elite_squad}")

# ==============================================================================
# LEVEL 5: WHILE LOOPS & MODULES (Random Battle)
# ==============================================================================
print("\n--- LEVEL 5: RANDOM ENCOUNTER ---")
import random

def attack_enemy(min_dmg, max_dmg):
    return random.randint(min_dmg, max_dmg) 

enemy_hp = 50 # Reduced for quicker testing

print("🔥 COMBAT STARTED! 🔥")

while enemy_hp > 0:
    damage_dealt = attack_enemy(5, 15)
    enemy_hp -= damage_dealt  
    
    if enemy_hp < 0:
        enemy_hp = 0
        
    print(f"⚔️ Hit for {damage_dealt}! Enemy HP: {enemy_hp}")

print("🏆 Enemy Defeated!")

# ==============================================================================
# LEVEL 6: OOP - BASIC CLASSES (Dog & Car)
# ==============================================================================
print("\n--- LEVEL 6: OBJECT ORIENTED BASICS ---")

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"🐶 {self.name} ({self.breed}) says: Woof Woof!")

dog1 = Dog("Rex", "Shepherd")
dog1.bark()


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
  
    def drive(self):
        print(f"🚗 The {self.brand} {self.model} ({self.year}) is driving!")
    
tesla = Car("Tesla", "Model 3", 2023)
fiat = Car("Fiat", "Uno", 1998)

tesla.drive()
fiat.drive()

# ==============================================================================
# LEVEL 7: OOP - INTERMEDIATE (Soldier & Vehicle)
# ==============================================================================
print("\n--- LEVEL 7: INTERMEDIATE OOP ---")

class Soldier:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def battle_cry(self):
        print(f"🗣️ {self.name} screams: FOR PYTHON!!!")

    def attack(self, target):
        damage = 10
        target.hp -= damage
        print(f"⚔️ {self.name} attacks {target.name} dealing {damage} damage!")

hero = Soldier("Jefferson", 100)
villain = Soldier("Bug", 100)

hero.battle_cry()
print(f"Enemy HP Before: {villain.hp}")
hero.attack(villain)
print(f"Enemy HP After: {villain.hp}")


class Vehicle:
    def __init__(self, brand, top_speed, color):
        self.brand = brand
        self.top_speed = top_speed
        self.color = color
        self.current_speed = 0 
        
    def show_info(self):
        print(f"Vehicle: {self.brand} | Color: {self.color} | Speed: {self.current_speed}/{self.top_speed} km/h")

    def accelerate(self, amount):
        self.current_speed += amount
        if self.current_speed > self.top_speed:
            self.current_speed = self.top_speed
            print("⚠️ Speed limit reached!")
    
    def brake(self):
        self.current_speed = 0
        print("🛑 Brakes applied!")

moto = Vehicle("Harley", 150, "Black")
moto.accelerate(50)
moto.show_info()
moto.brake()

# ==============================================================================
# LEVEL 8: OOP - ADVANCED (Bank & Study Tracker)
# ==============================================================================
print("\n--- LEVEL 8: ADVANCED OOP (FINAL BOSS) ---")

class BankAccount:
    """ Manages balance with validation logic """
    def __init__(self, initial_balance):
        self.balance = initial_balance 

    def deposit(self, amount):
        self.balance += amount
        print(f"✅ Deposit: +${amount:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"❌ Error: Insufficient funds for ${amount:.2f}. Balance: ${self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"💸 Withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"🏦 CURRENT BALANCE: ${self.balance:.2f}")


class StudyTracker:
    """ Tracks accumulated hours """
    def __init__(self, subject):
        self.hours = 0.0      
        self.subject = subject 

    def add_hours(self, amount):
        self.hours += amount
        print(f"📚 Added {amount}h to {self.subject}")

    def show_progress(self):
        print(f"📊 {self.subject} | Total: {self.hours}h")

# Final Tests
my_account = BankAccount(100)
my_account.withdraw(500) # Should fail
my_account.deposit(1000)

tracker = StudyTracker("Backend Python")
tracker.add_hours(6.5)
tracker.add_hours(4.5)
tracker.show_progress()