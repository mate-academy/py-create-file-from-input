def main() -> None:
    file_name = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    with open(file_name, "w") as file:
        pass

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        with open(file_name, "a") as file:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
