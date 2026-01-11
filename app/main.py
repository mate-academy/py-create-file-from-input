def main() -> None:
    # Ask the user for the file name
    file_name = input("Enter name of the file: ")
    file_name = file_name.strip() + ".txt"  # Ensure the extension is .txt

    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":  # Stop condition
            break
        content_lines.append(line)

    # Write the content to the file
    with open(file_name, "w") as file:
        file.write("\n".join(content_lines))

    print(f"File '{file_name}' has been created successfully.")


if __name__ == "__main__":
    main()
