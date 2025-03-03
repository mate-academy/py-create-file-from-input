def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as file_stream:
        stop = False
        while stop is False:
            new_line = input("Enter new line of content: ")
            if new_line != "stop":
                file_stream.write(new_line + "\n")
            else:
                stop = True
    pass


if __name__ == "__main__":
    main()
