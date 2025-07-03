def main() -> None:
    file_name = input("Enter name of the file: ")
    file = file_name + ".txt"
    with open(file, "w") as f:
        content = input("Enter new line of content: ")
        while content != "stop":
            f.write(f"{content}\n")
            content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
