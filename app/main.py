def main():
    file_name = input("Enter name of the file: ") + ".txt"
    text = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        text.append(line + "\n")
    with open(file_name, "w") as file:
        file.writelines(text)


if __name__ == "__main__":
    main()
