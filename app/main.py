def main() -> None:
    file_name = input("Enter name of the file: ")
    user_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        user_lines.append(line + "\n")
    user_file = open(f"{file_name}.txt", "w")
    for lin in user_lines:
        user_file.write(lin)
    user_file.close()


if __name__ == "__main__":
    main()
