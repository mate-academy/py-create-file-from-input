def main() -> None:
    name_of_file = input("Enter name of the file: ")
    text_for_file = ""
    while True:
        next_string = input("Enter new line of content: ")
        if next_string == "stop":
            break
        text_for_file += f"{next_string}\n"
    with open(f"{name_of_file}.txt", "w") as file:
        file.write(text_for_file)


if __name__ == "__main__":
    main()
