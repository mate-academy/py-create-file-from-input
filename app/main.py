def main():
    file_name = input("Enter name of the file: ")
    content = ''
    result = []
    while content != "stop":
        content = input("Enter new line of content: ")
        if content != "stop":
            result.append(content + "\n")
    with open(file_name + ".txt", "w") as file:
        file.writelines(result)


if __name__ == "__main__":
    main()
