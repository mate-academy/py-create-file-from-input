def main():
    name_file = input("Enter name of the file: ")
    with open(name_file + ".txt", "w") as f:
        str_file = input("Enter new line of content: ")
        f.write(str_file)
    with open(name_file + ".txt", "w") as f:
        while str_file != "stop":
            f.write(str_file + "\n")
            str_file = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
