def main():
    file_name = input("Enter name of the file: ")
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line + "\n")

    file_fullName = f"{file_name}.txt"
    with open(file_fullName, "w") as f:
        f.writelines(lines)

if __name__ == "__main__":
    main()
