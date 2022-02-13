"""Camel game"""
"""Trevor Egbert"""

import random


def main():
    print("Welcome to Camel")
    print("You have stolen a camel to make you way across the Mobi Desert.")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and out run the natives")

    """Variables """
    # Users variables
    player_miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    canteen = 3

    # Natives Variables
    natives_miles_traveled = -20

    """Main Program Loop"""
    # Checks to see if the program is done
    done = False
    # Players choice's and check for input
    while not done:
        print("\nA. Drink from your canteen. ")
        print("B. Ahead moderate speed. ")
        print("C. Ahead full speed. ")
        print("D. Stop for the night")
        print("E. Status check. ")
        print("Q. Quite")
        user_input = input("What is your choice? ")

        # If the input is Q for quite
        if user_input.lower() == "q":
            done = True
            print("Thank you for playing have a nice day!")

        # if the input is D rest for the night set's the camel tiredness to zero and informs the player of natives
        elif user_input.lower() == "d":
            camel_tiredness = 0
            print("The camel looks happy")
            natives_miles_traveled = natives_miles_traveled + random.randrange(7, 14)
            if player_miles_traveled - natives_miles_traveled >= 0:
                print("The natives are", player_miles_traveled - natives_miles_traveled, "miles behind you")

        # If the input is E status check.
        elif user_input.lower() == "e":
            print("Miles traveled:", player_miles_traveled)
            print("Drinks in canteen:", canteen)
            print("natives distance:", player_miles_traveled - natives_miles_traveled)

        # If the input is C ahead at full speed. Adjust parameters and prints out how far the player travel
        elif user_input.lower() == "c":
            player_miles_traveled = player_miles_traveled + random.randrange(10, 20)
            thirst = thirst + 1
            camel_tiredness = camel_tiredness + random.randrange(1, 3)
            natives_miles_traveled = natives_miles_traveled + random.randrange(7, 14)
            # 1/15 chance of find an oasis. Sets canteen back to 3 and camel_tiredness to 0
            if random.randrange(15) == 0:
                print("You found an oasis!")
                print("You refilled your canteen, and your camel looks well rested")
                canteen = 3
                camel_tiredness = 0
            if player_miles_traveled < 200:
                print("You have traveled:", player_miles_traveled, "miles")

        # If the input is B Ahead at moderate speed.  Adjust parameters and prints out how far the player travel
        elif user_input.lower() == "b":
            player_miles_traveled = player_miles_traveled + random.randrange(5, 12)
            thirst = thirst + 1
            camel_tiredness = camel_tiredness + 1
            # 1/15 chance of find an oasis. Sets canteen back to 3 and camel_tiredness to 0
            if random.randrange(15) == 0:
                print("You found an oasis!")
                print("You refilled your canteen, and your camel looks well rested")
                canteen = 3
                camel_tiredness = 0
            if player_miles_traveled < 200:
                print("You have traveled:", player_miles_traveled, "miles")

        # If the input is A drink from canteen.  Checks to see if canteen is equal to zero if not takes a drink and -1
        elif user_input.lower() == "a":
            if canteen == 0:
                print("Your canteen is empty")
            elif canteen != 0:
                canteen = canteen - 1
                print("You take a drink from your canteen", canteen, "drinks remaining")
                thirst = 0

        # Checks to see if the equal to 6 for a game over
        if thirst == 6:
            done = True
            print("You died of thirst! Game over!")

        # Checks to see if thirst is greater than 4 to print warning message
        elif thirst >= 4:
            print("You are thirsty")

        # Checks to see if camel_tiredness is greater than or equal to 8 for a game over
        if camel_tiredness >= 8:
            done = True
            print("Your camel is dead! Game over")

        # Checks to see if the camel_tiredness is greater than of equal to 5 to print a warning message
        elif camel_tiredness >= 5:
            if not done:
                print("Your camel is getting tired")

        # Checks to see if the player_miles_traveled is less than or equal to natives_miles traveled
        if player_miles_traveled <= natives_miles_traveled:
            done = True
            print("The natives have caught up, and you are going to jail! Game over!")
        # Checks to see if the natives_miles_traveled is less or equal to 15 of the player_miles_traveled
        elif player_miles_traveled - natives_miles_traveled <= 15:
            print("The natives are getting closer")

        # Checks to see if player has traveled of 200 miles for win condition
        if player_miles_traveled >= 200:
            done = True
            print("You escape the natives to live another day!")


main()
