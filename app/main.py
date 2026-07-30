def main() -> None:
    name = input("Enter name of the file: ")
    new_file = open(f"{name}.txt", "a")
    while True:
        user_input = (input("Enter new line of content: "))
        if user_input == "stop":
            new_file.close()
            break
        new_file.write(user_input + "\n")


if __name__ == "__main__":
    main()
