def main():
    result = ""
    my_list = []
    file_name = input("Enter name of the file: ")
    while result != "stop":
        result = input("Enter new line of content: ")
        if result != "stop":
            my_list.append(result)

    with open(file_name + ".txt", "a") as f:
        for i in range(len(my_list)):
            f.write(f"{my_list[i]}\n")


if __name__ == "__main__":
    main()
