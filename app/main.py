def main():
    file_name = input("Enter name of the file: ")

    lines_of_content = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines_of_content.append(line)

    file_name_with_extension = file_name + ".txt"

    with open(file_name_with_extension, "w") as file:
        for line in lines_of_content:
            file.write(line + "\n")

    print(f"File '{file_name_with_extension}' created successfully.")


if __name__ == "__main__":
    main()
