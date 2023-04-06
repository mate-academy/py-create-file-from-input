def main():
    file_name = input("Enter name of the file: ")
    text = []
    line = input("Enter new line of content: ")
    while line != "stop":
        text.append(line)
        line = input("Enter new line of content: ")

    with open(f"{file_name}.txt", "w") as f:
        for i in text:
            f.write(i + "\n")


if __name__ == "__main__":
    main()
