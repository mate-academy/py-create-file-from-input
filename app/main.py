def main():
    file_name = input("Enter name of the file: ")
    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content_lines.append(line)

    with open(f"{file_name}.txt", "w") as file:
        file.write("\n".join(content_lines))


if __name__ == "__main__":
    main()
