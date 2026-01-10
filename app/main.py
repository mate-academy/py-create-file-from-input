def main() -> None:
    file_name = input("Enter name of the file: ")
    text = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        text.append(new_line)

    with open(f"{file_name}.txt", "w") as file:
        file.write("\n".join(text))


if __name__ == "__main__":
    main()
