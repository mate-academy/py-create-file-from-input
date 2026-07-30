def main() -> None:
    file_name = input("Enter name of the file: ")

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    content_lines = []
    print("Enter lines of content")
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    try:
        with open(file_name, "w") as file:
            file.write("\n".join(content_lines))
        print("\nFile created successfully!")
        print("File content:")
        print("\n".join(content_lines))
    except Exception as e:
        print(f"Error creating file: {e}")


if __name__ == "__main__":
    main()
