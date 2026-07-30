def main() -> None:
    name_file = input("Enter name of the file: ")

    if name_file == "":
        name_file = "new_file"

    if name_file.endswith("."):
        name_file = name_file[:-1]

    if not name_file.endswith(".txt"):
        name_file += ".txt"

    with open(name_file, "a", encoding="utf-8") as new:

        while True:
            context = input("Enter new line of content: ")

            if context.strip().lower() == "stop":
                break

            new.write(context + "\n")


if __name__ == "__main__":
    main()
