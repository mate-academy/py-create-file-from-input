def main() -> None:
    file_name_input = input("Enter name of the file: ")
    file_name = file_name_input + ".txt"
    text = input("Enter new line of content: ")
    ls = []
    while text != "stop":
        ls.append(text)
        text = input("Enter new line of content: ")
    fl = open(file_name, "w")
    fl.write("\n".join(ls))
    fl.close()


if __name__ == "__main__":
    main()
