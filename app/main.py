def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as f:
        while True:
            file_content = input("Enter new line of content: ")
            print(file_content)
            if file_content == "stop":
                break
            f.write(file_content + "\n")


if __name__ == "__main__":
    main()
