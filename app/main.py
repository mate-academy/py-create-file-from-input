def main() -> None:
    name_file = input("Enter name of the file: ")
    file_used = open(name_file + ".txt", "w")
    while True:
        messege = input("Enter new line of content: ")
        if messege == "stop":
            break
        else:
            file_used.write(messege + "\n")
    file_used.close()


if __name__ == "__main__":
    main()
