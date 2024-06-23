def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "w") as file:
        if_new_content_line = True
        while if_new_content_line:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                if_new_content_line = False
            else:
                file.write(new_line + "\n")


if __name__ == "__main__":
    main()
