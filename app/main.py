def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = f"{file_name}.txt"

    file_content = []
    content_input = input("Enter new line of content: ")
    while content_input.lower() != "stop":
        file_content.append(f"{content_input}\n")
        content_input = input("Enter new line of content: ")

    final_file = open(file_name, "w")
    final_file.write("".join(file_content))
    final_file.close()


if __name__ == "__main__":
    main()
