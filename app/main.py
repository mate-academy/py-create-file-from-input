def main() -> None:
    name = input("Enter name of the file: ")
    file_path = f"{name}.txt"

    with open(file_path, "w") as file:
        pass

    while True:
        newline = input("Enter new line of content: ")
        if newline == "stop":
            break

        with open(file_path, "a") as file:
            file.write(newline + "\n")


if __name__ == "__main__":
    main()
