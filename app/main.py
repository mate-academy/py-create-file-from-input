def main() -> None:
    file_name = input("Enter name of the file: ")
    content = ""
    while True:
        input_cont = input("Enter new line of content: ")
        if input_cont == "stop":
            break
        content = f"{content}\n{input_cont}" if content else input_cont
    with open(file_name + ".txt", "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
