def create_file_line():
    file_name = input("Please, enter the file name: ")

    while True:
        line = input("Please, enter new line of content: ")
        if line == "stop":
            break
        else:
            with open(file_name + ".txt", "a") as f:
                f.write(f"{line}\n")


if __name__ == "__main__":
    create_file_line()
