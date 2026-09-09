def main() -> None:
    name_file = input("Enter name of the file: ").strip()
    if not name_file:
        return
    text = ""
    while True:
        line = input("Enter new line of content: ")
        if not line:
            continue

        if line == "stop":
            break

        text += line + "\n"

    print(text)

    with open(name_file + ".txt", "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
