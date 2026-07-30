def main() -> None:
    filename = input("Enter name of the file: ").strip()
    if not filename:
        print("Wrong filename!")
        return
    filename = filename + ".txt"

    with open(filename, "a") as file:
        while True:
            line = input("Enter new line of content: ")
            if line.strip().lower() == "stop":
                break
            file.write(line + "\n")


if __name__ == "__main__":
    main()
