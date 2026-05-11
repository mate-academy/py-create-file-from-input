def main() -> None:
    filename = input("Enter name of the file: ").strip()

    if not filename.endswith(".txt"):
        filename += ".txt"

    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    try:
        with open(filename, "w") as file:
            file.write("\n".join(content_lines))

        print(f"\n--- File '{filename}' created successfully! ---")
    except IOError as e:
        print(f"An error occurred while writing the file: {e}")


if __name__ == "__main__":
    main()
