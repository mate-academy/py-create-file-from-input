def create_text_file():
    file_name = input("Enter name of the file: ")

    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    file_path = f"{file_name}.txt"
    with open(file_path, "w") as file:
        for line in content_lines:
            file.write(line + "\n")

    print(f"file {file_path} created successfully with {len(content_lines)} lines of content")


def main():

    create_text_file()


if __name__ == "__main__":
    main()
