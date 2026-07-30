def main() -> None:
    # write your code here
    name_of_file = input("Enter name of the file: ")
    new_file = open(f"{name_of_file}.txt", "a")
    line_content = ""
    while True:
        line_content = input("Enter new line of content: ")
        if line_content == "stop":
            break
        new_file.write(f"{line_content}\n")
    new_file.close()


if __name__ == "__main__":
    main()
