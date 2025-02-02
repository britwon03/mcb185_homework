import random

def roll_d20():
    return random.randint(1, 20)

def saving_throw(dc, advantage=False, disadvantage=False):
    if advantage:
        roll = max(roll_d20(), roll_d20())
    elif disadvantage:
        roll = min(roll_d20(), roll_d20())
    else:
        roll = roll_d20()
    
    return roll, roll >= dc

dcs = [5, 10, 15]  # Renamed the list to avoid variable conflict

for dc in dcs:
    roll, success = saving_throw(dc)
    print(roll, "Success" if success else "Failure")
