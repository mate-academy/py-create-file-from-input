def main() -> None:
    name_of_file = input("Enter file name: ")
    new_text = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == ".stop":
            break
        else:
            new_text.append(new_line)
    with open(f"{name_of_file}.txt", "w") as text_file:
        for text in new_text:
            text_file.write(f"{text}\n")
    pass


if __name__ == "__main__":
    main()
