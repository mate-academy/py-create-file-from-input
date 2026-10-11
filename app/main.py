def main() -> None:
    name_file = input("Enter name of the file: ")
    with open(f"{name_file}.txt", "w") as file:
        while True:
            text = input("Enter new line of content: ")
            if text.lower() == "stop":
                break
            file.write(f"{text}\n")


if __name__ == "__main__":
    main()
