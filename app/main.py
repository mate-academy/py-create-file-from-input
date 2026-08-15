def main():
    file_name = input("Enter name of the file: ")
    file_name += ".txt"

    file_content = ""
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        file_content += new_line + "\n"

    with open(file_name, "a") as new_file:
        new_file.write(file_content)

if __name__ == "__main__":
    main()
