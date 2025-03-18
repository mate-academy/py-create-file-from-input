def main() -> None:
    file_name = input("Enter name of the file: ")
    string = ""
    string_full = []
    while string != "stop":
        string = input("Enter new line of content: ")
        string_full.append(string)
    string_full.remove("stop")

    with open(f"{file_name}.txt", "w") as f:
        f.write("\n".join(string_full))
    # write your code here
    pass


if __name__ == "__main__":
    main()
