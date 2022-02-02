def create_a_file_from_input():
    file_name = input("Please, enter the file name: ")

    while True:
        next_line = input("Please, enter new line of content: ")
        if next_line == "stop":
            break
        else:
            with open(file_name+".txt", "a") as f:
                f.write(next_line)


if __name__ == "__main__":
    create_a_file_from_input()
