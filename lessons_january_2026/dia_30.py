import time

print(">>> STARTING SYSTEM... <<<\n")

# ==========================================
# MODULE 1: LISTS & BASIC LOOPS
# ==========================================
print("--- 1. INVENTORY CHECK (Lists) ---")

materials = ["Cement", "Brick", "Sand"]
print(f"Second item in list: {materials[1]}")

print("Full list:")
for item in materials:
    print(f"* {item}")


# ==========================================
# MODULE 2: DICTIONARY BASICS
# ==========================================
print("\n--- 2. TRANSLATOR (Simple Dict) ---")

english_dictionary = {
    "gato": "Cat",
    "cachorro": "Dog",
    "programador": "Developer"
}

# Accessing keys
animal = english_dictionary["gato"]
job = english_dictionary["programador"]

print(f"The {animal} belongs to the {job}.")


# ==========================================
# MODULE 3: DATA MANIPULATION & MATH
# ==========================================
print("\n--- 3. STOCK & INFLATION ---")

# 3.1 Summing values
inventory_counts = {"Cement": 10, "Sand": 50, "Brick": 500, "Gravel": 20}

# Fast way (Pythonic)
total_items = sum(inventory_counts.values())
print(f"Total Items (Fast): {total_items}")

# Loop way (Manual)
total_manual = 0
for quantity in inventory_counts.values():
    total_manual += quantity
print(f"Total Items (Loop): {total_manual}")

# 3.2 Applying Inflation (10%)
prices = {"Cement": 10.0, "Sand": 20.0, "Brick": 0.50}

print(f"Old Prices: {prices}")

for product in prices:
    old_price = prices[product]
    new_price = old_price * 1.10 # Adding 10%
    prices[product] = new_price

print(f"New Prices (+10%): {prices}")


# ==========================================
# MODULE 4: FILTERING DATA
# ==========================================
print("\n--- 4. STUDENT GRADES (Filtering) ---")

grades = {"John": 12, "Mary": 18, "Peter": 8, "Anne": 9, "Leo": 15}
approved_students = {} 

for student in grades:
    grade = grades[student] 
    if grade >= 10:
        approved_students[student] = grade

print(f"Approved List: {approved_students}")


# ==========================================
# MODULE 5: COMPLEX STRUCTURES (List of Dicts)
# ==========================================
print("\n--- 5. PAYROLL SYSTEM ---")

employees = [
    {"name": "Jefferson", "role": "Dev", "salary": 2000},
    {"name": "Leo", "role": "Scrum Master", "salary": 1800},
    {"name": "Anne", "role": "Designer", "salary": 2500}
]

total_payroll = 0

for person in employees:
    total_payroll += person["salary"]

print(f"Monthly Company Cost: {total_payroll}€")


# ==========================================
# MODULE 6: CURRENCY CONVERSION
# ==========================================
print("\n--- 6. CURRENCY CONVERTER (EUR -> BRL) ---")

prices_europe = {"Coffee": 1.50, "Pastry": 2.00, "Lunch": 10.00}
prices_brazil = {} 

for item in prices_europe:
    value_euro = prices_europe[item]
    value_real = value_euro * 6.0 # Exchange rate
    prices_brazil[item] = value_real

print(f"Menu Europe (€): {prices_europe}")
print(f"Menu Brazil (R$): {prices_brazil}")


# ==========================================
# MODULE 7: UBER/DELIVERY LOGIC
# ==========================================
print("\n--- 7. DELIVERY EARNINGS ---")

trip_prices = {
    "Short": 3.00, 
    "Long": 7.00
}

qty_short = 5
qty_long = 2

# Calculating total earnings based on quantity
# FIX: The original code didn't multiply by quantity. Corrected here:
total_short_earnings = trip_prices["Short"] * qty_short
total_long_earnings = trip_prices["Long"] * qty_long

daily_total = total_short_earnings + total_long_earnings
print(f"Total Earnings Today: {daily_total:.2f}€")


# ==========================================
# MODULE 8: NET SALARY CALCULATION
# ==========================================
print("\n--- 8. NET SALARY (After Taxes) ---")

gross_salaries = {"Jefferson": 2000, "Leo": 1500, "Anne": 3000}
net_salaries = {}

for name in gross_salaries:
    gross_value = gross_salaries[name]
    # FIX: Original was (salary - 0.8). Correct logic is (salary * 0.8) for 20% tax.
    net_value = gross_value * 0.8 
    net_salaries[name] = net_value

print(f"Net Salaries: {net_salaries}")


# ==========================================
# MODULE 9: INTERACTIVE STORE (The App)
# ==========================================
print("\n" + "="*40)
print(">>> ENTERING INTERACTIVE STORE <<<")
print("="*40)

# Initial Setup
client_balance = 100.0
price_table = {"Cement": 10, "Brick": 5, "Sand": 20}

# User Input
client_name = input("Enter client name: ")
print(f"Welcome {client_name}, your balance is {client_balance}€")

while True:
    print(f"\n--- AVAILABLE PRODUCTS: {list(price_table.keys())} ---")
    choice = input("What do you want to buy? (or type 'exit'): ").capitalize()

    if choice == "Exit":
        print(f"Thank you, {client_name}! Final Balance: {client_balance}€")
        break 

    if choice in price_table:
        price = price_table[choice] 
        
        if client_balance >= price:
            client_balance -= price
            print(f"✅ Purchase successful: {choice}.")
            print(f"💰 Remaining Balance: {client_balance}€")
        else:
            missing = price - client_balance
            print(f"❌ Insufficient funds. You need {missing}€ more.")
            
    else:
        print("🚫 Product not found. Please try again.")

print("\n>>> SYSTEM SHUTDOWN <<<")