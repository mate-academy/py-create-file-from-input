def main() -> None:
    file_name = input("Enter name of the file: ")
    inpt = ""
    content = ""
    while inpt != "stop":
        inpt = input("Enter new line of content: ")
        if inpt != "stop":
            content += inpt + "\n"
    with open(f"{file_name}.txt", "w") as f:
        f.writelines(content)


if __name__ == "__main__":
    main()
