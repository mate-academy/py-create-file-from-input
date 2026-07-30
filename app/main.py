def main() -> None:
    work_line = ""
    while True:
        if work_line == "stop":
            break

        work_str = input("Enter name of the file: ")

        if work_str == "stop":
            break
        else:
            with open(work_str + ".txt", "w") as work_file:
                while True:
                    work_line = input("Enter new line of content: ")
                    if work_line == "stop":
                        break
                    else:
                        work_file.write(work_line + "\n")


if __name__ == "__main__":
    main()
