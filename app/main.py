def main() -> None:
    file_name = input("Enter name of the file: ")
    file_user = open(file_name + ".txt", "w")
    while True:
        message = input("Enter new line of content: ")
        if message == "stop":
            break
        file_user.write(message + "\n")
    file_user.close()


if __name__ == "__main__":
    main()
