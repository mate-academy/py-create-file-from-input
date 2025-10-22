def main() -> None:
    filename = input("Enter name of the file: ")
    if not filename.endswith(".txt"):
        filename += ".txt"
    print("Enter lines of content. Type 'stop' to finish.")
    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join(content_lines))
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    main()
