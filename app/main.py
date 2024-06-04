def main() -> None:
    name_file = input("Enter name of the file: ")
    content = []
    while True:
        line_text = input("Enter new line of content: ")
        if line_text == "stop":
            break
        content.append(line_text)
    new_file = f"{name_file}.txt"
    with open(new_file, "w") as file1:
        for line in content:
            file1.write(f"{line}\n")


if __name__ == "__main__":
    main()
