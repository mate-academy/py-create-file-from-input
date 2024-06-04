def main() -> None:
    filename = input("Enter name of the file: ")
    created_file = open(f"{filename}.txt", "w")
    created_file.close()
    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        with open(f"{filename}.txt", "a") as file:
            file.write(user_input + "\n")


if __name__ == "__main__":
    main()
