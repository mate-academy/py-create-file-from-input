def main() -> None:
    file_name = input("Enter name of the file: ")
    list_string = []
    while True:
        text = input("Enter new line of content: ")
        if text.lower() == "stop":
            break
        list_string.append(text)

    with open(file_name + ".txt", "w") as file:
        file.write(("\n").join(list_string))


if __name__ == "__main__":
    main()
