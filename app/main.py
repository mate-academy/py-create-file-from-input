def main() -> None:
    name_of_file = input("Enter name of the file: ")
    list_of_text = []
    while True:
        text_to_file = input("Enter new line of content: ")
        if text_to_file.casefold() == "stop":
            break
        list_of_text.append(text_to_file)
    with open(f"{name_of_file}.txt", "w") as file:
        file.write("\n".join(list_of_text))


if __name__ == "__main__":
    main()
