def main() -> None:
    file_basename = input("Enter name of the file: ")
    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    file_name = f"{file_basename}.txt"
    with open(file_name, "w") as output_file:
        output_file.write("\n".join(content_lines))


if __name__ == "__main__":
    main()
