def main() -> None:
    file_name = input("Enter name of the file: ")
    file = open(file_name + ".txt", "a")
    while True:
        new_string = input("Enter new line of content: ")
        if new_string == "stop":
            break
        file.write(new_string + '\n')
    file.close()


if __name__ == "__main__":
    main()
