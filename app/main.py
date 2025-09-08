def main() -> None:
    file_name = input("Enter name of the file: ")

    result = ""
    while True:
        inp = input("Enter new line of content (or 'stop' to finish): ")
        if inp == "stop":
            break
        if result == "":
            result = inp
        else:
            result += "\n" + inp

    with open(file_name, "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()
