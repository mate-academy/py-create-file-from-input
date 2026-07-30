def main() -> None:
    name_file = input("Enter name of the file: ")

    with open(f"{name_file}.txt", "w"):
        pass

    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break

        with open(f"{name_file}.txt", "a") as file:
            file.write(f"{text}\n")


if __name__ == "__main__":
    main()
