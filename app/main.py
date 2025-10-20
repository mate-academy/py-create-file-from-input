def main():
    file_name = input("Enter name of the file: ")
    content_lines = []
    print("Enter your content. Type 'stop' on a new line to finish.")
    while True:
        line = input("Enter new line of content: ")

        if line == "stop":
            break
        else:
            content_lines.append(line)

    full_file_name = f"{file_name}.txt"

    with open(full_file_name, "w") as file:
        for content_line in content_lines:
            file.write(f"{content_line}\n")

    print(f"File '{full_file_name}' created successfully")


if __name__ == "__main__":
    main()
