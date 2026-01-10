def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = f"{file_name}.txt"
    file_content = []

    while True:
        line = input("Enter new line of content: ")

        if line.strip().lower() == "stop":
            break

        file_content.append(line)

    with open(file_name, "w") as file:
        file.write("\n".join(file_content))


if __name__ == "__main__":
    main()
