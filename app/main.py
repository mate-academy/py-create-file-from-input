def create_file():
    file_name = input("Enter file name: ")
    with open(f"{file_name}.txt", "a") as f:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            f.write(f"{line}\n")


if __name__ == "__main__":
    create_file()
