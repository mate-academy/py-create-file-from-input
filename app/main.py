def main() -> None:
    file_name = input("Enter name of the file: ")
    fi = open(file_name + ".txt", "a")
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        else:
            fi.write(new_line + "\n")
    fi.close()


if __name__ == "__main__":
    main()
