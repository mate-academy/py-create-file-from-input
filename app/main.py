def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    my_str = ""


    while (True):
        temp_str = input("Enter new line of content: ")
        if temp_str == "stop":
            break
        my_str += temp_str + "\n"

    with open(file_name, "w") as new_file:
        new_file.write(my_str)


if __name__ == "__main__":
    main()
