def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    text = ""
    while True:
        tmp = input("Enter new line of content: ")
        if tmp == "stop":
            break
        text += tmp + "\n"

    with open(file_name, "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
