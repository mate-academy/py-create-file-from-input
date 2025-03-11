def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    content_lines = []

    while True:
        line = input("Enter new line of content: ").strip()
        if line.lower() == "stop":
            break
        content_lines.append(line)

    file_path = f"{file_name}.txt"
    with open(file_path, "w") as file:
        file.write("\n".join(content_lines))

    print(f"File '{file_path}' has been created successfully!")


if __name__ == "__main__":
    main()
