def main() -> None:
    file_name = input("Enter name of the file: ")
    text = ""
    while True:
        next_line = input("Enter new line of content: ")
        if next_line == "stop":
            break
        text += next_line + "\n"

    with open(f"{file_name}.txt", "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
