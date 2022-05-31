def main():
    name = input("Enter name of the file: ")
    data = ""
    new_line = input("Enter new line of content: ")
    while new_line != "stop":
        if data != "":
            data += "\n" + new_line
        else:
            data += new_line
        new_line = input("Enter new line of content: ")

    with open(f"{name}.txt", "w") as f:
        f.writelines(data)


if __name__ == "__main__":
    main()
