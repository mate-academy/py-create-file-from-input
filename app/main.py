def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "w") as file:
        stop_not_entered = True
        while stop_not_entered:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                stop_not_entered = False
            else:
                file.write(new_line + "\n")


if __name__ == "__main__":
    main()
