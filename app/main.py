def main():
    name = input("Enter name of the file: ")
    file_name = name + ".txt"
    content = ""
    while True:
        next_line = input("Enter new line of content: ")
        if next_line == "stop":
            with open(file_name, "a") as f:
                f.write(content)
            break
        content += next_line + "\n"


if __name__ == "__main__":
    main()
