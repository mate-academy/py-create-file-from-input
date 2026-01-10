def main() -> None:
    # write your code here
    file_name = input("Enter name of the file: ")
    new_file = open(f"{file_name}.txt", "a")

    while True:
        content = input("Enter new line of content: ")
        if content != "stop":
            new_file.write(f"{content}\n")
        else:
            break


if __name__ == "__main__":
    main()
