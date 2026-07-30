def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    with open(name, "x") as file:
        while True:
            user_input = input("Enter new line of content: ")
            if user_input.lower() == "stop":
                break
            file.write(f"{user_input}\n")


if __name__ == "__main__":
    main()
