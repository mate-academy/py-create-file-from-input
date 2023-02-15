
def main() -> None:
    file_name = input("Enter name of the file: ")
    data = ""
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        data += content + "\n"
    with open(file_name + ".txt", "w") as f:
        f.write(data)


if __name__ == "__main__":
    main()

