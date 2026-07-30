def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    fl = open(file_name, "w")
    content = input("Enter new line of content: ")
    while content != "stop":
        fl.write(content + "\n")
        content = (input("Enter new line of content: "))
    fl.close()
    fl = open(file_name, "r")
    print(f'File name: "{file_name}"')
    print("File content:")
    print(fl.read())
    fl.close()


if __name__ == "__main__":
    main()
