def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"

    with open(file_name, "w") as file_name:
        while True:
            line = input("Enter new line of content: ")

            if line.lower() == "stop":
                break

            file_name.write(line + "\n")


if __name__ == "__main__":
    main()
