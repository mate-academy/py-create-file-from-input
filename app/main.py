def main() -> None:
    text = input("Enter name of the file: ")

    with open(f"{text}.txt", "w") as file:
        while True:
            user_input = input("Enter new line of content: ")
            if user_input.lower() == "stop":
                break
            file.write(user_input + "\n")


if __name__ == "__main__":
    main()
