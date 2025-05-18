def main():
    file_name = input("Enter name of the file: ") + ".txt"
    my_str = ""

    while (True):
        temp_str = input("Enter new line of content: ")
        if temp_str == "stop":
            break
        my_str += temp_str + "\n"

    new_file = open(file_name, "w")
    new_file.write(my_str)
    new_file.close()


if __name__ == "__main__":
    main()
