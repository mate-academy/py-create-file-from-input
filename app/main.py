def main() -> None:
    filename = input("Enter name of the file: ")

    with open(filename + ".txt", "w") as file:
        while True:
            line = input("Enter new line of content: ")

            if line == "stop":
                break

            file.write(line + "\n")


if __name__ == "__main__":
    main()
