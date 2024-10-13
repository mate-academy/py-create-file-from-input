def main() -> None:
    name_of_file = input("Enter name of the file: ")
    stop_word = "stop"

    with open(name_of_file + ".txt", "w") as file:
        while True:
            line = input("Enter new line of content: ")
            if line == stop_word:
                break
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
