def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "w") as fw:
        while (new_str := input("Enter new line of content: ")) != "stop":
            fw.write(new_str + "\n")


if __name__ == "__main__":
    main()
