def main() -> None:
    with open(f"{input('Enter name of the file: ')}.txt", "w") as file:
        user_text = input("Enter new line of content: ")

        while user_text != "stop":
            file.write(f"{user_text}\n")
            user_text = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
