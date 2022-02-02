def create_files():
    while True:
        file_name = input("Enter name of the file: ")
        if file_name:
            with open(file_name + ".txt", "a") as f:
                content = input("Enter new line of content: ")
                while content != "stop":
                    content = input("Enter new line of content: ")
                    f.write(content + "\n")
                print("Have a nice day!")
                break


if __name__ == '__main__':
    create_files()
