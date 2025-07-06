def main() -> None:
    filename = input("Enter name of the file: ")
    filename += ".txt"

    with open(filename, "w") as file:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            else:
                file.write(line + "\n")


if __name__ == "__main__":
    main()
