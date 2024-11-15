def main():
    file_name = input("Enter name of the file: ") + ".txt"

    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(file_name, "w") as file:
        file.write("\n".join(content_lines))

if __name__ == "__main__":
    main()
