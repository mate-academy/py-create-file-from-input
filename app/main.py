def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    text = ""
    while True:
        input_str = input("Enter new line of content: ")
        if input_str.strip() == "stop":
            break
        text += input_str + "\n"
    with open(file_name, "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
