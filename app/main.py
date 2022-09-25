def main():
    file_name = input("Enter name of the file: ")
    file_content = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        file_content.append(new_line + "\n")
    with open(f"{file_name}.txt", "w") as f:
        for line in file_content:
            f.write(line)


if __name__ == "__main__":
    main()
