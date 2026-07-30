def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    list_text = []
    print("Enter new line of content(type 'stop' to finish):")
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        list_text.append(line)

    with open(file_name, "w") as f:
        for line in list_text:
            f.write(line + "\n")
    print(f"file name: '{file_name}'")
    print("file text:")
    for line in list_text:
        print(f"{line}")


if __name__ == "__main__":
    main()
