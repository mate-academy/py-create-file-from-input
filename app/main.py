def main():
    file_name = input("Enter name of the file: ")
    usr_text = ""
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        else:
            usr_text += new_line + "\n"
    with open(file_name + ".txt", "w") as text_file:
        text_file.write(usr_text)


if __name__ == "__main__":
    main()
