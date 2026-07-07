# Following a tutotrial by: 'Programming with Mosh' on YT.
import random
while True:
    choice = input("Would like you like to roll the dice? (y/n): ").lower()
    if choice == 'y':
        die1 = random.randit(1,6)
        die2 = random.randint(1,6)
        print(f"({die1}, {die2})")
    
    elif choice == 'n':
        print("Thank you for playing. ")
        break
    
    else:
        print("Invalid choice! ")