def create_files():
    file_name = input("Enter name of the file: ")
    if file_name:
        with open(file_name + ".txt", "a") as f:
            while True:
                content = input("Enter new line of content: ")
                if content != "stop":
                    f.write(content + "\n")
                else:
                    print("Have a nice day!")
                    break


if __name__ == '__main__':
    create_files()
