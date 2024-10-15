def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"

    with open(filename, "w") as file:
        while True:
            input_from_user = input("Enter new line of content: ")
            if input_from_user.lower() == "stop":
                break
            file.write(f"{input_from_user}\n")


if __name__ == "__main__":
    main()
