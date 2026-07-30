def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "w") as file:
        while True:
            line = input("Enter new line of content: ")
            if line.lower() == "stop":
                break
            file.write(line + "\n")


if __name__ == "__main__":
    main()
