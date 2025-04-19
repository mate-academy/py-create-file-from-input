def main() -> None:
    file_name = input("Enter name of the file: ")
    text_to_file = []

    while True:
        text = input("Enter new line of content: ")
        if text.lower() == "stop":
            break
        text_to_file.append(text + "\n")

    with open(f"{file_name}.txt", "w") as f:
        f.writelines(text_to_file)


if __name__ == "__main__":
    main()
