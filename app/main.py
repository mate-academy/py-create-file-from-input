def main() -> None:
    file_name = input("Enter name of the file: ")
    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content_lines.append(line)
    full_file_name = f"{file_name}.txt"
    try:
        with open(full_file_name, "w") as file:
            file.write("\n".join(content_lines))
        print(f"File '{full_file_name}' created successfully.")
    except IOError as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    main()
