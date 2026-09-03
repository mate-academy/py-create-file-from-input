def main() -> None:
    string = input("Enter name of the file: ")
    result = []
    while True:
        new_string = input("Enter new line of content: ")
        if new_string != "stop":
            result.append(new_string)
        else:
            break
    with open(string + ".txt", "w") as file:
        file.write("\n".join(result))


if __name__ == "__main__":
    main()
