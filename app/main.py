def main():
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    all_text = []
    text = input("Enter new line of content: ")
    while text != "stop":
        all_text.append(text)
        text = input("Enter new line of content: ")
    with open(file_name, 'a') as f:
        f.writelines("%s\n" % line for line in all_text)


if __name__ == "__main__":
    main()
