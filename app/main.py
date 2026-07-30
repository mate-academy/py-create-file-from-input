def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    result_text = ""
    while True:
        string = input("Enter new line of content: ")
        if string == "stop":
            break
        result_text += string + "\n"
    result_file = open(filename, "w")
    result_file.write(result_text)


if __name__ == "__main__":
    main()
