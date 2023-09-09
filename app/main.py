def main():
    file_name = input("Enter name of the file: ")
    lines = []
    while true:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(f"{line}\n")
    with open(f"{file_name}.txt", "w") as f:
        for line in lines:
            f.write(line)


if __name__ == "__main__":
    main()
