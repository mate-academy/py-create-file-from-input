def main():
    file_name = input("Enter name of the file: ")
    text = ""
    new_line = ""
    while new_line.lower() != "stop":
        new_line = input("Enter new line of content: ")
        if new_line != "stop":
            text += f"{new_line}\n"
    file = open(f"{file_name}.txt", 'a')
    file.write(text)
    file.close()


if __name__ == "__main__":
    main()
