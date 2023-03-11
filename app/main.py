def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    if len(file_name) > 0:
        new_line = ""
        arr = []
        while new_line != "stop":
            new_line = input("Enter new line of content: ")
            if new_line != "stop":
                arr.append(new_line + "\n")
        with open(file_name, "w") as f:
            f.writelines(arr)


if __name__ == "__main__":
    main()
