def main() -> None:
    stop_word = ""
    new_file = open(input("Enter name of the file: ") + ".txt", "a")
    while stop_word != "stop":
        stop_word = input("Enter new line of content: ")
        if stop_word != "stop":
            new_file.write(stop_word + "\n")
    new_file.close()


if __name__ == "__main__":
    main()
