def main():
    file_name = input("Enter name of the file: ") + ".txt"
    text = []
    while True:
        new_line = input("Enter new line of content: ") + "\n"
        if new_line == "stop\n":
            break
        text.append(new_line)

    with open(file_name, "w") as file:
        file.writelines(text)


if __name__ == "__main__":
    main()
