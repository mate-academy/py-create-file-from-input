def main() -> None:
    f_le = input("Enter name of the file: ")
    line, text = "", ""
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        text += line + "\n"

    with open(f"{f_le}.txt", "w") as main_file:
        main_file.write(text)


if __name__ == "__main__":
    main()
