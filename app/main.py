def user_file():
    usercontent = []
    filename = ""
    while len(filename) == 0 :
        filename = input("Enter name of the file: ")
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        usercontent.append(content)
    with open(f"{filename}.txt", "a") as f:
        for cont in usercontent:
            f.write(f"{cont}\n")


if __name__ == '__main__':
    user_file()
