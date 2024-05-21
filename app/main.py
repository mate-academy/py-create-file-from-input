def main():
    # Get the file name from the user
    file_name = input("Enter name of the file: ")

    # Initialize an empty list to store content lines
    content_lines = []

    # Prompt the user for content lines until they enter "stop"
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    # Create the file with the specified name and write content to it
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
