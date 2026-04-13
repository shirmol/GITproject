import random

def roll_dice():
    # הגרלת מספר רנדומלי בין 1 ל-6
    result = random.randint(1, 6)
    return result

print("--- Welcome to the Dice Roller ---")
roll = roll_dice()
print(f"You rolled a: {roll}")

if roll == 6:
    print("Amazing! You got the maximum score!")
elif roll == 1:
    print("Better luck next time...")