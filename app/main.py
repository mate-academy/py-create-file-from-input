def main() -> None:
    file_name = input("Enter name of the file: ")

    stopped = False
    lines = []

    while not stopped:
        line = input("Enter new line of content: ")
        if line == "stop":
            stopped = True
        else:
            lines.append(line + "\n")

    file_out = open(file_name + ".txt", "w")
    file_out.writelines(lines)
    file_out.close()


if __name__ == "__main__":
    main()
