def main() -> None:
    file_name = input("Enter name of the file: ")
    text = []
    while True:
        new_string = input("Enter new line of content: ")
        if new_string == "stop":
            break
        text.append(new_string + "\n")
    with open(file_name + ".txt", "w") as file:
        file.writelines(text)


if __name__ == "__main__":
    main()
