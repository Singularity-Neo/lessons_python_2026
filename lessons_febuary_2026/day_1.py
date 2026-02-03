"""
JEFFERSON'S OOP JOURNEY PORTFOLIO
Collection of Object-Oriented Programming exercises in Python.
Topics: Classes, Methods, State Management, Object Interaction, and Logic.
"""

# ==========================================
# 1. BANKING SYSTEM (Logic & Interaction)
# ==========================================
class BankAccount:
    def __init__(self, owner, initial_balance=0.0):
        self.owner = owner
        self.balance = initial_balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"✅ {self.owner}: Received €{amount}. New Balance: €{self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"💸 {self.owner}: Withdrew €{amount}. Remaining: €{self.balance}")
            return True # Returns True if successful
        else:
            print(f"❌ {self.owner}: Denied! Tried €{amount}, but only has €{self.balance}")
            return False

    def show_balance(self):
        print(f"📊 Account: {self.owner} | Current Balance: €{self.balance}")
    
    def transfer(self, amount, target_account):
        print(f"\n--- Starting Transfer of €{amount} to {target_account.owner} ---")
        # Reuse the withdraw logic to ensure funds exist
        if self.withdraw(amount): 
            # Reuse the deposit logic of the target account
            target_account.deposit(amount)
            print("🔄 Transfer Completed Successfully!")
        else:
            print("❌ Transfer Failed: Insufficient funds.")

# --- TESTING BANK ---
jeff_acc = BankAccount("Jefferson", 100)
luiz_acc = BankAccount("Luiz")

jeff_acc.deposit(100)       # Total 200
jeff_acc.transfer(70, luiz_acc) # Sends 70 to Luiz

print("\n--- FINAL BALANCES ---")
jeff_acc.show_balance()
luiz_acc.show_balance()


# ==========================================
# 2. RPG COMBAT SYSTEM (Object Interaction)
# ==========================================
class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100 # Default health
        print(f"⚔️ {self.name} entered the arena with {self.health} HP.")

    def take_damage(self, damage):
        self.health -= damage
        print(f"🩸 {self.name} took {damage} damage! HP left: {self.health}")
        
        if self.health <= 0:
            print(f"💀 {self.name} DIED!")

    def attack(self, enemy):
        damage = 15
        print(f"\n👊 {self.name} attacked {enemy.name}!")
        # Interaction: Triggering the method of the OTHER object
        enemy.take_damage(damage)

# --- TESTING RPG ---
hero = Warrior("Jeff")
orc = Warrior("Ugly Orc")

hero.attack(orc)
orc.attack(hero)
hero.attack(orc)


# ==========================================
# 3. PAYMENT SYSTEM (Dependency Injection)
# ==========================================
class CreditCard:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.balance = initial_balance
    
    def deduct(self, amount):
        self.balance -= amount

class PaymentTerminal:
    def charge(self, target_card, amount):
        # The terminal commands the card to deduct the value
        target_card.deduct(amount)

# --- TESTING PAYMENTS ---
my_card = CreditCard("Jefferson", 100)
coffee_machine = PaymentTerminal()

print(f"\n💳 Card Balance Before: €{my_card.balance}")
coffee_machine.charge(my_card, 5) 
print(f"💳 Card Balance After: €{my_card.balance}")


# ==========================================
# 4. GAS STATION (Delegation Logic)
# ==========================================
class Car:
    def __init__(self):
        self.gas_level = 0

    def refuel(self, liters):
        self.gas_level += liters
        print(f"🚗 Car refueled. Tank: {self.gas_level}L")

class GasPump:
    def fill_car(self, client_car):
        # The pump triggers the car's refuel method
        client_car.refuel(20)

# --- TESTING GAS STATION ---
my_car = Car()          # Fixed: Removed arguments as __init__ takes none
station = GasPump()

station.fill_car(my_car) # The pump fills the car


# ==========================================
# 5. NINJA (State Logic & Limits)
# ==========================================
class Ninja:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        print(f"\n🥷 Ninja {self.name} created with {self.health} HP.")

    def take_damage(self, damage):
        self.health -= damage
        print(f"😫 {self.name} got hurt! HP: {self.health}")
        
    def vanish_in_shadows(self):
        print(f"💨 {self.name} threw a smoke bomb and escaped with {self.health} HP!")

    def eat_ramen(self):
        self.health += 30
        # Logic to cap health at 100
        if self.health > 100:
            self.health = 100
        print(f"🍜 {self.name} ate Ramen. HP recovered to: {self.health}")

    def show_status(self):
        print(f"ℹ️ Status: {self.name} has {self.health} HP.")

# --- TESTING NINJA ---
sasuke = Ninja("Sasuke", 100, 15)
sasuke.take_damage(20)      # HP 80
sasuke.vanish_in_shadows()
sasuke.eat_ramen()          # HP 100 (Capped)
sasuke.show_status()