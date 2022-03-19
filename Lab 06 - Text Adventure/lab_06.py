""" Trevor Egbert """
""" Lab 6 """


class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []
    done = False

    # Sets the different parameters  for the room using the class Room
    room = Room("You find yourself in a dungeon with skeletons hanging from chains on the wall.\nThere's a door to the "
                "north.",
                1,
                None,
                None,
                None)
    room_list.append(room)

    room = Room("You are in torcher chamber there's still blood on the floor.\nThere's are doors to the "
                "north, south, and west.",
                9,
                None,
                0,
                2)
    room_list.append(room)

    room = Room("You are in a dinning room there's a table with food.\nThere's doors leading north, south, east, and, "
                "west.",
                3,
                1,
                7,
                6)
    room_list.append(room)

    room = Room("The kitchen has signs of a meal that was just prepared.  There’s a light coming from the north.\n"
                "There’s doors leading north, south, east, and west.",
                4,
                9,
                2,
                5,)
    room_list.append(room)

    room = Room("",
                None,
                None,
                3,
                None,)
    room_list.append(room)

    room = Room("A lounge room with a billiards table and a table for cards. There's light coming from the north\n"
                "There's doors leading north, south, and east",
                10,
                3,
                6,
                None,)
    room_list.append(room)

    room = Room("A living room there's couches and chairs.\nThere's doors leading north, south, and east",
                5,
                2,
                8,
                None,)
    room_list.append(room)

    room = Room("A bathroom that's low on toilet paper, horrifying!\nThere's doors leading north, and west",
                2,
                None,
                None,
                8,)
    room_list.append(room)

    room = Room("An observatory covered in dust from little use.\nThere's doors leading north, and east",
                6,
                7,
                None,
                None)
    room_list.append(room)

    room = Room("The room is empty but it feels like someone is watching you.\nThere's doors leading south,"
                "and west",
                None,
                None,
                1,
                3)
    room_list.append(room)

    room = Room("",
                None,
                None,
                5,
                None)
    room_list.append(room)

    current_room = 0

    while not done:
        # Updates room info and check for win / lose contentions
        print(room_list[current_room].description)
        print("To quite type q or quite")
        print()

        # checks if player can go north and moves to new room if able
        user_input = input("What way should you go: ")
        if user_input.lower() == "north" or user_input.lower() == "n":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way")
            else:
                current_room = next_room

        # Checks if the player can go east and moves to new room if able
        elif user_input.lower() == "east" or user_input.lower() == "e":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way")
            else:
                current_room = next_room

        # check if the player can go south moves to new room if able
        elif user_input.lower() == "south" or user_input.lower() == "s":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way")
            else:
                current_room = next_room

        # checks if the player can go west move to new room if able
        elif user_input.lower() == "west" or user_input.lower() == "w":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way")
            else:
                current_room = next_room

        # checks if the player wants to quite the game
        elif user_input.lower() == "quite" or user_input.lower() == "q":
            done = True
            print("Thanks for playing!")

        else:
            print("Please use a valid input")

        if current_room == 4:
            done = True
            print("You fell into a spike pit and died!  Game over!")
        elif current_room == 10:
            done = True
            print("You escaped! You Win!")


main()
