def main() -> None:
    name_file = str(input("Enter name of the file: ")) + ".txt"
    with open(name_file, "w") as file:
        while True:
            user_input = str(input("Enter new line of content: "))
            if user_input.lower() == "stop":
                break
            file.write(user_input + "\n")


if __name__ == "__main__":
    main()
