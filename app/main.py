def main() -> None:
    file_name = input("Enter name of the file: ")
    is_true = True
    content = ""
    while is_true:
        phrase = input("Enter new line of content: ")
        if phrase == "stop":
            is_true = False
        else:
            content += (phrase + "\n")

    with open(file_name + ".txt", "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
