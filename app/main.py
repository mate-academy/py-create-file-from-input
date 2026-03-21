def create_file_from_input() -> None:
    file_name = input("Enter name of the file: ")

    full_path = f"{file_name}.txt"

    content_lines = []

    while True:
        line = input("Enter new line of content: ")

        if line.lower() == "stop":
            break

        content_lines.append(line)

    with open(full_path, "w") as file:
        file.write("\n".join(content_lines))

    print(f"File '{full_path}' has been created successfully.")


if __name__ == "__main__":
    create_file_from_input()