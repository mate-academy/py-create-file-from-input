def file_from_input():
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "a") as f:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            else:
                f.write(f"{content}\n")


if __name__ == '__main__':
    file_from_input()
