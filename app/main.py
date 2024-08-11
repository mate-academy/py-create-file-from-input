def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"

    with open(filename, "w") as file:
        while True:
            line = input("Enter new line of content: ")

            if line.lower() == "stop":
                break

            file.write(line + "\n")


if __name__ == "__main__":
    main()
