def main():
    filename = input("Enter name of the file: ")
    if not filename.endswith(".txt"):
        filename += ".txt"
    content_writen = False

    while True:
        fileinfo = input("Enter new line of content: ")

        if fileinfo.lower() == "stop":
            break
        with open(filename, "a", newline="") as file:
            file.write(fileinfo + "\n")
        content_writen = True

    if not content_writen:
        open(filename, "w").close()


if __name__ == "__main__":
    main()
