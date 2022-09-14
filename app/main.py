def main():
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    text = ""
    while True:
        next_line = input("Enter new line of content: ")
        if next_line == "stop":
            break
        text += (next_line + "\n")

    with open(file_name, "w") as file:
        file.write(text)


if __name__ == "__main__":
    main()
