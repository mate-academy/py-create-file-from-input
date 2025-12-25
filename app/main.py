def main() -> None:
    def create_file() -> None:
        file_name = input("Enter name of the file: ")
        content = []
        while True:
            line = input("Enter new line of content: ")
            if line.lower() == "stop":
                break
            content.append(line)

        file_name += ".txt"
        with open(file_name, "w") as file:
            for line in content:
                file.write(line + "\n")

    create_file()


if __name__ == "__main__":
    main()
