# Ali Jackson
# IT 140
# October 18th 2024

#
# dictionary links a room to other rooms and assigns an item to each room
rooms = {
    'Collapsed Bridge': {'South': 'Abandoned Hospital', 'North': 'Safehouse', 'East': 'Sewer', 'West': 'Gas Station',
                         'item': 'Rope'},
    'Safehouse': {'South': 'Collapsed Bridge', 'East': 'Library'},
    'Library': {'West': 'Safehouse', 'item': 'Map'},
    'Gas Station': {'East': 'Collapsed Bridge', 'item': 'Gas Mask'},
    'Sewer': {'West': 'Collapsed Bridge', 'South': 'Mutant Lair', 'item': 'Water Bottle'},
    'Abandoned Hospital': {'North': 'Collapsed Bridge', 'East': 'Supermarket', 'item': 'First Aid Kit'},
    'Supermarket': {'West': 'Abandoned Hospital', 'item': 'Flashlight'},
    'Mutant Lair': {'North': 'Sewer'}  # Villain's room, no items
}


# Function to show game instructions
def show_instructions():
    """Print the main menu and available commands."""
    print("Post-Apocalyptic City Adventure Game")
    print("Goal: Collect 6 items to escape the city and avoid the mutant.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to inventory: get 'item name'")
    print("Type 'exit' to quit the game.")


# Function to display the player's current status
def show_status(current_room, inventory):
    """Display the player's current status: location, inventory, and any item in the room."""
    print(f"\nYou are in the {current_room}.")
    print(f"Inventory: {inventory}")

    # Check if there's an item in the current room
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("----------------------")


# Main function with the game loop
def main():
    # Start the player in the Collapsed Bridge
    current_room = 'Collapsed Bridge'

    # Initialize player's inventory (empty at the start)
    inventory = []

    # Main game loop
    while True:
        # Show the player's status
        show_status(current_room, inventory)

        # Get the player's input for the next move
        action = input("Enter your move: ").strip().lower()

        # Handle 'exit' command to quit the game
        if action == 'exit':
            print("Thanks for playing! Goodbye.")
            break

        # Handle 'get [item]' command to collect items
        elif action.startswith('get '):
            item = action[4:]

            # Check if the item exists in the current room
            if 'item' in rooms[current_room] and rooms[current_room]['item'].lower() == item:
                inventory.append(item)  # Add the item to the player's inventory
                print(f"{item.capitalize()} has been added to your inventory.")
                del rooms[current_room]['item']  # Remove the item from the room
            else:
                print(f"There is no {item} here.")

        # Handle 'go [direction]' command to move between rooms
        elif action.startswith('go '):
            direction = action[3:].capitalize()  # Capitalize the direction to match the dictionary

            # Check if the direction is valid in the current room
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]  # Move to the new room
            else:
                print("You can't go that way!")

        # Check if the player enters the Mutant Lair
        if current_room == 'Mutant Lair':
            print("NOM NOM...GAME OVER! You were caught by the mutant.")
            break

        # Check if the player has collected all 6 items
        if len(inventory) == 6:
            print("Congratulations! You've collected all the items and escaped the city!")
            print("Thanks for playing! Hope you enjoyed the game.")
            break


# Run the game
if __name__ == "__main__":
    show_instructions()  # Show instructions at the start of the game
    main()  # Start the main game loop
