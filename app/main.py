def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    full_file_name = f"{file_name}.txt"
    with open(full_file_name, "w") as file:
        for line in lines:
            file.write(line + "\n")

    print(f'File "{full_file_name}" created successfully.')


if __name__ == "__main__":
    main()
