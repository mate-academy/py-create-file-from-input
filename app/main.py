def main():
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    content_line = input("Enter new line of content: ")
    with open(file_name, "a") as f:
        while content_line != "stop":
            f.write(content_line + "\n")
            content_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
