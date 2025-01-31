def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(file_name, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    print(f"File '{file_name}' has been created successfully.")


if __name__ == "__main__":
    main()
