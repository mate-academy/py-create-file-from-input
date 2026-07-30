def main() -> None:
    # 1. Get the base filename from the user
    file_base_name = input("Enter name of the file: ")
    filename = f"{file_base_name}.txt"

    # 2. Collect lines of content until 'stop' is entered
    lines = []
    while True:
        line = input("Enter new line of content: ")
        # Check if the user wants to end the interaction
        if line.lower() == "stop":
            break
        lines.append(line)

    # 3. Create the .txt file and write the collected content
    try:
        with open(filename, "w") as file:
            # Join the list into a single string with newlines
            file.write("\n".join(lines))

        # 4. Display the required result format
        print(f"\nResult:\n\nFile created: {filename}")
        print("File content:")
        for content_line in lines:
            print(content_line)

    except Exception as e:
        print(f"An error occurred while creating the file: {e}")


if __name__ == "__main__":
    main()
