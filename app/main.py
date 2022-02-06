def create_file():
    file_name = input("Input the name of file: ")
    print("File content: ")

    with open(file_name + ".txt", "a") as f:
        while True:
            content = input()

            if content.lower() == "stop":
                break
            else:
                f.write(content + "\n")


if __name__ == "__main__":
    create_file()
