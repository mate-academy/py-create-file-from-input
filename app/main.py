def main() -> None:
    file_name = input("Enter name of the file: ")
    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    try:
        with open(f"{file_name}.txt", "w") as file:
            for line in content_lines:
                file.write(line + "\n")
        print(f"File name: \"{file_name}.txt\"")
        print("File content:")
        for line in content_lines:
            print(f"# {line}")
    except Exception as e:
        print(f"Error creating the file: {e}")


if __name__ == "__main__":
    main()
