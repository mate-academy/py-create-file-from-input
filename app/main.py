def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "w") as file:

        file_content = []
        while True:
            line = input("Enter new line of content: ")
            if line.lower() == "stop":
                break
            file_content.append(line)

        for line in file_content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
