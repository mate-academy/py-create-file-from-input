def main() -> None:
    file_name = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    with open(file_name, "w") as a:
        while True:
            file_content = input("Enter new line of content: ")
            if file_content == "stop":
                break
            a.write(file_content + "\n")
    with open(file_name, "r") as r:
        print("File name: ", file_name)
        print("File content: ")
        print(r.read().rstrip(), end="")


if __name__ == "__main__":
    main()
