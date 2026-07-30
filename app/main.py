def main() -> None:
    file_name = input("Enter name of the file: ")

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    content_lines = []
    while True:
        line = input("Enter new line of content: ")

        if line.lower() == "stop":
            break

        content_lines.append(line)

    try:
        with open(file_name, "w") as file:
            file.write("\n".join(content_lines))

        print(f"\nSuccess! File '{file_name}' has been created.")

    except IOError as e:
        print(f"AN error occurred while creating the file: {e}")


if __name__ == "__main__":
    main()
