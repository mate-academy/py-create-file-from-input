def main():
    content = ""
    file_name = input("Enter name of the file: ")

    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        else:
            content += new_line + "\n"

    with open(file_name + ".txt", "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
