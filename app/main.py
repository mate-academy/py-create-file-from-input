def main() -> None:
    file_name = input("Enter name of the file: ")
    text_file = []
    close_app = True
    while close_app:
        interact_text = input("Enter new line of content: ")
        if interact_text.lower() == "stop":
            close_app = False
        else:
            text_file.append(interact_text + "\n")

    with open(f"{file_name}.txt", "w") as file:
        for line in text_file:
            file.write(line)


if __name__ == "__main__":
    main()
