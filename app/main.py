def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []
    while True:
        temp = input("Enter new line of content: ")
        if temp == "stop":
            break
        content.append(temp + "\n")
    with open(f"{file_name}.txt", "w") as file:
        file.writelines(content)


if __name__ == "__main__":
    main()
