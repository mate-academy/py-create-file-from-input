def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    with open(file_name, "w") as f:
        content_list = []
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            content_list.append(line)
        f.write("\n".join(content_list))

    return


if __name__ == "__main__":
    main()
