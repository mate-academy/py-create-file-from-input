def main() -> None:
    file_name = ""
    lines = []
    while True:
        if file_name == "":
            file_name = input("Enter name of the file: ")
        line = input("Enter new line of content: ")
        if line != "stop":
            lines.append(line)
        else:
            file_ = open(f"{file_name}.txt", "a")
            for i in lines:
                file_.write(f"{i}\n")
            file_.close()
            break


if __name__ == "__main__":
    main()
