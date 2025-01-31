def main():
    file_name = input("Enter name of the file: ")
    content = ''
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content += line + "\n"
    with open(file_name + ".txt", "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
