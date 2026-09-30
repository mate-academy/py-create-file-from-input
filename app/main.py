def main() -> None:
    filename = input("Enter name of the file: ")

    file_contents = ""
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        else:
            file_contents += f"{content}\n"

    new_file = open(f"{filename}.txt", "w")
    new_file.write(file_contents)
    new_file.close()


if __name__ == "__main__":
    main()
