def main() -> None:
    name = input("Enter name of the file: ")
    path_to_file = name + ".txt"
    is_exit = False
    created_file = open(path_to_file, "a")
    while not is_exit:
        content = input("Enter new line of content: ")
        if content == "stop":
            created_file.close()
            is_exit = True
        else:
            created_file.write(f"{content}\n")


if __name__ == "__main__":
    main()
