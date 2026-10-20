def main():
    file_name = input("Enter name of the file: ")
    line = ""
    file = open(file_name + ".txt", "a")
    while line != "stop":
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        file.write(line + "\n")


if __name__ == "__main__":
    main()
