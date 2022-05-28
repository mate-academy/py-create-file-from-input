def file_creator():
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "w") as f:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                exit()
            else:
                f.write(line + "\n")


if __name__ == "__main__":
    file_creator()
