def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "w") as f:
        while True:
            content = input("Enter new line of content: ")
            if content != "stop":
                f.write(f"{content}\n")

            else:
                break


if __name__ == "__main__":
    main()
