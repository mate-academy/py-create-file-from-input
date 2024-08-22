def main() -> None:
    file_name = input("Enter name of the file: ")
    text = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        text.append(line + "\n")
    with open(file_name + ".txt", "w") as f:
        f.writelines(text)


if __name__ == "__main__":
    main()
