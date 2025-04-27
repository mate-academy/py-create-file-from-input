def main() -> None:
    try:
        file_name = input("Enter name of the file: ")
        file_name_with_extension = file_name + ".txt"
        content_lines = []

        print("Enter the content for the file.  Enter 'stop' when finished. ")
        while True:
            line = input("Enter new line of content: ")
            if line.lower() == "stop":
                break
            content_lines.append(line + "\n")

        with open(file_name_with_extension, "w", encoding="utf-8") as file:
            file.writelines(content_lines)

        print(f"File '{file_name_with_extension}' created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Failed to create the file.")


if __name__ == "__main__":
    main()
