import os
import time

# ==========================================
# PART 1: CLASSES (Bank Account System)
# ==========================================

class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance
        self.history = []
        self.history.append(f"Account created with: ${initial_balance}")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} successful!")
        self.history.append(f"Deposit: +${amount}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient funds!")
        else:
            self.balance -= amount
            print(f"You withdrew ${amount}.")
            self.history.append(f"Withdrawal: -${amount}")
    
    def view_statement(self):
        print(f"\n--- STATEMENT FOR {self.name.upper()} ---")
        print(f"Current Balance: ${self.balance}")
        print("-" * 40)
        
        for line in self.history:
            print(line)
            
        print("-" * 40 + "\n")

    def apply_fee(self):
        self.balance -= 5
        self.history.append("Monthly fee: -$5")


# ==========================================
# PART 2: EXECUTING CONCEPTS (Automated)
# ==========================================

print(">>> STARTING AUTOMATED DEMOS <<<\n")

# --- 1. BANK DEMO ---
print("--- 1. BANK SYSTEM DEMO ---")
my_account = BankAccount("Jefferson", 500)
my_account.deposit(200)
my_account.withdraw(50)
my_account.withdraw(1000) # Testing error
my_account.deposit(100)
my_account.apply_fee()
my_account.view_statement()


# --- 2. GREETINGS & STRINGS ---
print("--- 2. GREETING ---")
name = "Dovahkiin"
title = "Partner"
print(f"Greetings {title} {name}, welcome to Skyrim!")


# --- 3. MATH LOGIC ---
print("\n--- 3. BRICK CALCULATOR (Math) ---")
width = 10 
height = 5
result = width * height
print(f"Total Area: {result} m².")
print(f"You need {result} bricks.") 


# --- 4. CONDITIONAL LOGIC ---
print("\n--- 4. THE BOUNCER (If/Else) ---")
age = 20 
if age >= 18:
    print("Allowed to enter the party.")
else:
    print("Access Denied!")


# --- 5. LOOPS (For & Range) ---
print("\n--- 5. MULTIPLICATION TABLE (7) ---")
for i in range(1, 11): 
    print(f"7 x {i} = {7 * i}")


# --- 6. LOOPS (While) ---
print("\n--- 6. COUNTDOWN ---")
number = 10
while number > 0: 
    print(number)
    number -= 1 
    # time.sleep(0.1) # Reduced time for faster testing
print("FUS RO DAH!")


# --- 7. LISTS ---
print("\n--- 7. SHOPPING LIST ---")
materials = ["Cement", "Sand", "Brick"]
for item in materials:
    print(f"- {item}") 


# --- 8. ACCUMULATOR ---
print("\n--- 8. SUMMATION ---")
prices = [10, 20, 30, 40]
total = 0 
for num in prices:
    total += num 
print(f"Total Price: {total}")


# --- 9. DICTIONARIES ---
print("\n--- 9. RPG HERO ---")
hero = {
  "name": "Jefferson", 
  "hp": 100, 
  "level": 5 
}
print(f"Initial Level: {hero['level']}")

hero["hp"] -= 10 
hero["weapon"] = "Iron Sword" 

print(f"Updated Status: {hero}")


# --- 10. FILTERING ---
print("\n--- 10. LIST FILTER ---")
numbers_list = [1, 5, 12, 6, 20, 3]
print("Numbers greater than 10:")
for i in numbers_list:
    if i > 10:
        print(i)


# --- 11. STRING MANIPULATION ---
print("\n--- 11. STRING CLEANING ---")
sentence = "Look at this, interesting thing"
raw_phrases_list = sentence.split(",")

clean_phrases = []
for i, phrase in enumerate(raw_phrases_list):
    clean_phrases.append(raw_phrases_list[i].strip())
  
joined_phrases = ', '.join(clean_phrases)
print(f"Original: '{sentence}'")
print(f"Cleaned:  '{joined_phrases}'")


# ==========================================
# PART 3: INTERACTIVE APP (List Manager)
# ==========================================

print("\n" + "="*40)
print("ENTERING INTERACTIVE MODE (PRESS ENTER)")
input() # Pause so user can read above before clearing screen

items_list = []

while True:
    # Cross-platform clear command
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('--- LIST MANAGER 3000 ---')
    print('Current items:', items_list)
    print('-' * 20)
    print('Select an option:')
    # Added [q]uit to allow exiting the loop
    option = input('[i]nsert  [d]elete  [l]ist  [q]uit: ').lower()

    if option == 'i':
        value = input('Value to insert: ')
        items_list.append(value)
        
    elif option == 'd': # changed 'a' (apagar) to 'd' (delete)
        if len(items_list) == 0:
            print("List is empty!")
            time.sleep(1)
            continue
            
        print("\nChoose index to delete:")
        for index, item in enumerate(items_list):
            print(f"{index}: {item}")
            
        index_str = input('Index: ')

        try:
            index = int(index_str)
            del items_list[index]
            print("Item deleted.")
        except ValueError:
            print('Error: Please type an integer number.')
        except IndexError:
            print('Error: Index does not exist.')
        except Exception as e:
            print(f'Unknown error: {e}')
        
        time.sleep(1) # Pause to let user read error/success

    elif option == 'l':
        # List is already shown at the top of loop, but we can pause here
        if len(items_list) == 0:
            print('Nothing to list.')
        else:
            for i, value in enumerate(items_list):
                print(f"{i}: {value}")
        
        input("\nPress Enter to continue...")

    elif option == 'q':
        print("Closing application...")
        break
        
    else:
        print('Invalid option.')
        time.sleep(1)

print("System shutdown. Goodbye!")