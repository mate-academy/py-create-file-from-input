def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = ""
    while True:
        temp_content = (input("Enter new line of content: "))
        if temp_content != "stop":
            content += temp_content + "\n"
        else:
            break

    with open(file=file_name, mode="w") as f:
        f.write(content)
        f.close()


if __name__ == "__main__":
    main()
