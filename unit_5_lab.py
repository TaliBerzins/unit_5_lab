print("""Lab 5
Tali Berzins
Dice rolling simulation that outputs special names for rolls
02/12/2026""")

import random
print("Rolling the dice...")


dice_roll = random.randint(1, 6)
dice_roll_2 = random.randint(1, 6)
print("You rolled a", dice_roll, "and a", dice_roll_2)

# Outputting the rolls and print results

if dice_roll + dice_roll_2 == 2:
    print("Snake Eyes")
elif dice_roll + dice_roll_2 == 3:
    print("Ace Caught a Deuce")
elif dice_roll ==2 and dice_roll_2 == 2:
    print("Little Joe From Kokomo")
elif (dice_roll ==1 and dice_roll_2 == 4) or (dice_roll ==4 and dice_roll_2 == 1): 
    print("Little Phoebe") 
elif (dice_roll ==2 and dice_roll_2 == 3) or (dice_roll ==3 and dice_roll_2 == 2):
    print("Little Phoebe") 
elif dice_roll ==3 and dice_roll_2 == 3:
    print(" Jimmy Hicks from the Sticks")
elif (dice_roll ==1 and dice_roll_2 == 6) or (dice_roll ==6 and dice_roll_2 == 1):
    print("Six Ace")
elif (dice_roll ==4 and dice_roll_2 == 4):
    print("Eight from Decatur")
elif (dice_roll ==3 and dice_roll_2 == 6) or (dice_roll ==6 and dice_roll_2 == 3):
    print("Nina from Pasadena")
elif (dice_roll ==4 and dice_roll_2 == 5) or (dice_roll ==5 and dice_roll_2 == 4):
    print("Nina from Pasadena")
elif (dice_roll ==5 and dice_roll_2 == 5):
    print("Puppy Paws")
elif (dice_roll ==5 and dice_roll_2 == 6) or (dice_roll ==6 and dice_roll_2 == 5):
    print("Six five no Jive")
elif (dice_roll ==6 and dice_roll_2 == 6):
    print("Boxcars")
else:
    print("No special name for this roll")