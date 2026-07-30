def main() -> None:
    file_name = input("Enter name of the file: ")
    text = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            new_file = open(file_name + ".txt", "w")
            new_file.write("\n".join(text))
            new_file.close()
            break
        text.append(line)


if __name__ == "__main__":
    main()
