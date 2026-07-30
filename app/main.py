def main() -> any:
    file_name = input("Enter name of the file: ")
    file_name_txt = file_name + ".txt"

    with open(file_name_txt, "a") as f:
        row = input("Enter new line of content: ")
        while row != "stop":
            f.writelines(row + "\n")
            row = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
