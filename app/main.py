def main():
    name = input("Enter name of the file: ")

    temp_list = [input("Enter new line of content: ")]
    while temp_list[-1] != "stop":
        temp_list.append(input("Enter new line of content: "))
    del temp_list[-1]

    with open(f"{name}.txt", "w") as f:
        for word in temp_list:
            f.write(f"{word}\n")


if __name__ == "__main__":
    main()
