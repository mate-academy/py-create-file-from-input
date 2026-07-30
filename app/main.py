def main():
    file_name = input("Enter name of the file: ") + ".txt"
    content = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line + "\n")

    file = open(file_name, "w")
    file.writelines(content)
    file.close()


if __name__ == "__main__":
    main()
