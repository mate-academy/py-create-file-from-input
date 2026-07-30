def main() -> None:

    spis = []

    file_name = input("Enter name of the file: ")
    while True:
        data = input("Enter new line of content: ")
        if data == "stop":
            break
        spis.append(data)

    with open(f"{file_name}.txt", "w") as f:
        for i in spis:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
