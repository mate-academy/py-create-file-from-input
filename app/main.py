def main() -> None:

    file_name = input("Enter name of the file: ")
    file_name += ".txt"  # Ensure the file has a .txt extension

    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    # Write content to file
    with open(file_name, "w") as file:
        file.write("\n".join(content_lines))

    print(f"File '{file_name}' created successfully!")


if __name__ == "__main__":
    main()
