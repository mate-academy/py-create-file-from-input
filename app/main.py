def main():
    file_name = input("Enter name of the file: ")
    file_name += ".txt"

    file_content = ""
    while True:
        new_line = input("Enter new line of content: ")
        if not new_line == "stop":
            file_content += new_line + "\n"
        else:
            break

    with open(file_name, "w") as f:
        f.write(file_content)


if __name__ == "__main__":
    main()
