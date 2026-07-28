def main() -> None:
    filename = input("Enter name of the file: ").strip()

    if not filename.endswith(".txt"):
        full_filename = f"{filename}.txt"
    else:
        full_filename = filename

    content_lines = []
    while True:
        line = input("Enter new line of content: ")

        if line.lower() == "stop":
            break

        content_lines.append(line)

    try:
        with open(full_filename, "w") as file:
            file.write("\n".join(content_lines))

        print(f"\n--- File '{full_filename}' created successfully! ---")

    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    main()
