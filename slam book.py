def write_entry():
    print("\n--- Fill the Slam Book ---")
    name = input("Your Name: ")
    nickname = input("Your Nickname: ")
    hobby = input("Your Hobby: ")
    favorite_color = input("Favorite Color: ")
    best_friend = input("Your Best Friend: ")
    dream = input("Your Dream: ")

    with open("slambook.txt", "a") as file:
        file.write(f"\n--- New Entry ---\n")
        file.write(f"Name: {name}\n")
        file.write(f"Nickname: {nickname}\n")
        file.write(f"Hobby: {hobby}\n")
        file.write(f"Favorite Color: {favorite_color}\n")
        file.write(f"Best Friend: {best_friend}\n")
        file.write(f"Dream: {dream}\n")
        file.write("----------------------\n")

    print("✅ Your entry has been saved!")

def read_entries():
    print("\n--- Slam Book Entries ---")
    try:
        with open("slambook.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("❌ No entries found yet!")

# Main program loop
while True:
    print("\nWhat do you want to do?")
    print("1. Fill Slam Book")
    print("2. Read All Entries")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        write_entry()
    elif choice == "2":
        read_entries()
    elif choice == "3":
        print("👋 Goodbye!")
        break
    else:
        print("❗ Please enter a valid choice.")