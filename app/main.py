def main() -> None:
    file_name = input("Enter name of the file: ")
    text = ""

    while True:
        line = input("Enter new line of content: ")

        if line == "stop":
            break

        text += line + "\n"

    with open(f"{file_name}.txt", "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
