def main() -> None:

    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    with open(file_name, "w") as f:
        stop_word = "stop"
        while True:
            file_line = input("Enter new line of content: ")
            if file_line.lower() != stop_word:
                file_line += "\n"
                f.write(file_line)
            else:
                break
    f.close()


if __name__ == "__main__":
    main()
