def main() -> None:
    file_name = str(input("Enter name of the file: ")) + ".txt"
    context = ""
    while True:
        new_line = input("Enter new line of content: ")
        if new_line != "stop":
            context += new_line + "\n"
        else:
            break
    with open(file_name, "w") as f:
        f.write(context)


if __name__ == "__main__":
    main()
