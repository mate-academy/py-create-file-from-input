def main():
    file_name = input("Enter name of the file: ")
    content_line = input("Enter new line of content: ")
    with open(f"{file_name}.txt", "a") as f:
        while content_line != "stop":
            f.write(content_line + "\n")
            content_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
