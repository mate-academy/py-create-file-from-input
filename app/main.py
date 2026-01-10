def main():
    name = input("Enter name of the file: ")
    content = []
    while True:
        content.append(input("Enter new line of content: "))
        if content[-1] == "stop":
            content.pop(-1)
            break
    name += ".txt"
    with open(name, 'a') as file_name:
        for line in content:
            line += "\n"
            file_name.write(line)


if __name__ == "__main__":
    main()
