def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = ""
    while True:
        entered_data = input("Enter new line of content: ")
        if entered_data == "stop":
            break
        else:
            content += entered_data + "\n"
    with open(file_name, "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
