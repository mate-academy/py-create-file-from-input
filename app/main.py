def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    if not file_name:
        print("File name cannot be empty.")
        return

    file_name += ".txt"
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    with open(file_name, "w") as file:
        file.write("\n".join(lines))

    print(f"File '{file_name}' has been created.")


if __name__ == "__main__":
    main()
