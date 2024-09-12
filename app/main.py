def main():
    content = []
    filename = input("Enter name of the file: ")
    line_string = ""
    while line_string != "stop":
        line_string = input("Enter new line of content: ")
        if line_string == "stop":
            break
        content.append(line_string + "\n")
    with open(filename + ".txt", "w") as file:
        for line in content:
            file.write(line)
    return 0


if __name__ == "__main__":
    main()
