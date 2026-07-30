def main() -> None:
    name_file = (input("Enter name of the file: ") + ".txt")
    with open(name_file, "a") as file:
        while True:
            user_choice = input("Enter new line of content: ")
            if user_choice == "stop":
                break
            file.write(user_choice + "\n")

    return name_file


if __name__ == "__main__":
    main()
# Enter name of the file: name1
# Enter new line of content: This is the first line of content
# Enter new line of content: This is the second
# Enter new line of content: stop
# File name: "name1.txt"
# File content:
# This is the first line of content
# This is the second
